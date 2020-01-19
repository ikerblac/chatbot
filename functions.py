import custom_constants
import speech_recognition as sr
import connection
from gtts import gTTS
from io import BytesIO
import pygame
import pyaudio
from googletrans import Translator

def receive_request(code_lang, lang):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        result = r.recognize_google(audio, language = code_lang, show_all = False, key = None)
    except sr.UnknownValueError:
        result = custom_constants.NOT_UNDERSTAND
    except sr.RequestError as e:
        result = custom_constants.ERROR

    return result
    

def search_request(request):

    mycursor = connection.mydb.cursor()
    query = "SELECT * FROM request WHERE request = '{0}'".format(request)
    mycursor.execute(query)
    myresult = mycursor.fetchone()

    if myresult != None:
        return myresult
    else:
        request = request.split()
        num = 0
        len_request = len(request)
        len_request += -1

        while(myresult == None):
            mycursor = connection.mydb.cursor()
            query = "SELECT * FROM request WHERE request = '{0}'".format(request[num])
            mycursor.execute(query)
            myresult = mycursor.fetchone() 

            if mycursor.rowcount == 1:
                return myresult

            if num == len_request:
                myresult = custom_constants.NOT_UNDERSTAND
                return myresult
                break

            num+=1

        return myresult

def traslate(response, lang):

    translator = Translator()

    traslate = translator.translate(response, dest=lang)

    return traslate.text

def remove_unnecessary(request):

    request = request.split()
    num = 0
    len_request = len(request)
    myresult = ''

    while(num != len_request):
        mycursor = connection.mydb.cursor()
        query = "SELECT * FROM unnecessaries WHERE unnecessary = '{0}'".format(request[num])
        mycursor.execute(query)
        myresult_db = mycursor.fetchone() 

        if myresult_db == None:
            myresult += request[num] + ' '

        if num == len_request and myresult == '':
            myresult = custom_constants.NOT_UNDERSTAND

        num += 1    
    
    myresult = myresult.strip()
    return myresult

def wikipedia(response, manual, code_lang, lang):
    import wikipedia

    #Search the wikipedia
    search = wikipedia.search(response, results=3)

    #It does not show different options if an exact match appears
    if search[0] != response and search[1] != response and search[2] != response:

        #Show 3 results of wikipedia
        print(search)

        #If there is no result, suggest any
        if len(search) == 0:
            search = wikipedia.suggest(response)
            print(search)

        #Answer which one want
        traslate_question = traslate('Which do you mean?', lang)
        if manual == True:
            search = input(traslate_question + '\n')
        else:
            send_response(traslate_question, lang)
            search = receive_request(code_lang, lang)

    #Search the summary 
    try:
        if search[0] != response and search[1] != response and search[2] != response:
            search = wikipedia.summary(search, sentences=1)
        else:
            search = wikipedia.summary(search[search.index(response)], sentences=1)
        
        #Remove brackets of summary
        if '(' in search and ')' in search:
            search_1 = search.split('(')
            search_2 = search.split(')')
            search = search_1[0] + search_2[1]

    except wikipedia.PageError:
        search = custom_constants.ERROR

    search = traslate(search, lang)
    return search
        
def send_response(response, lang):

    pygame.init()

    tts = gTTS(text=response, lang=lang)
    fp = BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)

    pygame.mixer.init()
    pygame.mixer.music.load(fp)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)