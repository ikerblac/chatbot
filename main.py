import functions
import custom_constants
import os
import sys

manual = False

while True:

    #Check if the data file exists
    exist_data = os.path.isfile('data.txt')

    #If the file does not exist, collect the necessary information to create it
    if exist_data == False:

        lang = os.getenv('LANG')[0:5]
        name = 'What is your name and your last name? \nEnter to default: Guest'
        language = 'What two-letter codes of ISO 639-1? \nEnter to default: '

        name = input(functions.traslate(name, lang) + '\n') or 'Guest' 
        language = input(functions.traslate(language + lang, lang) + '\n') or lang
        data = [name, language]

        #Create a file and write data.txt
        f = open('data.txt', 'w+')
        for i in data:
            f.write(i +'\n')
        f.close()

    #Set variables with data.txt
    f = open('data.txt', 'r')
    name = f.readline()
    code_lang = f.readline()
    lang = code_lang[0:2]
    f.close

    #Recognize the petition
    if manual == False:
        print(functions.traslate('Say something!!', lang))
        receive_request = functions.receive_request(code_lang, lang)
    else:
        receive_request = input(functions.traslate('Write something!!', lang) + '\n')
            
    if not receive_request.strip():
        continue

    #Process the petition
    if receive_request != custom_constants.NOT_UNDERSTAND and receive_request != custom_constants.ERROR:

        #Traslate to english if the receive_request is in other language
        if lang != 'en':
            receive_request = functions.traslate(receive_request, 'en')

        raw_request = receive_request 

        #Search in database
        receive_request = functions.search_request(receive_request)

        if receive_request != custom_constants.NOT_UNDERSTAND:

            request = receive_request[1]
            response = receive_request[2]
            action = receive_request[3]

            #Method of acting depending on 'action' in the database

                #0-> Only speak + name
                #1-> To search in x
                #2-> To exit

            if action == 0:
                response = response + name

            elif action == 1:
                remove_unnecessary = functions.remove_unnecessary(raw_request)

                if request == 'Wikipedia' or request == 'wikipedia':
                    response = functions.wikipedia(remove_unnecessary, manual, code_lang, lang)

            elif action == 2:
                response = response + name
                exit = True
        else:
            response = receive_request 

    #As the database is in english we translate the answer   
    if lang != 'en':
        response = functions.traslate(response, lang)

    #It depends if the developer mode is activated we output by tts or text
    if manual == True:   
        print(response)
    else:
        functions.send_response(response, lang)

    #Exit when end the bucle
    if exit == True:
        sys.exit()