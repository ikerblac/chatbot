-- phpMyAdmin SQL Dump
-- version 4.6.6deb5
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost:3306
-- Tiempo de generación: 19-01-2020 a las 13:34:12
-- Versión del servidor: 5.7.28-0ubuntu0.18.04.4
-- Versión de PHP: 7.2.24-0ubuntu0.18.04.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `chatbot`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `request`
--

CREATE TABLE `request` (
  `id` int(255) NOT NULL,
  `request` varchar(255) NOT NULL,
  `response` varchar(255) NOT NULL,
  `action` int(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `request`
--

INSERT INTO `request` (`id`, `request`, `response`, `action`) VALUES
(1, 'Hello', 'Hello, ', 0),
(2, 'Wikipedia', '', 1),
(3, 'Bye', 'Bye, ', 2),
(4, 'Goodbye', 'Goodbye, ', 2),
(5, 'Hi', 'Hi, ', 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `unnecessaries`
--

CREATE TABLE `unnecessaries` (
  `id` int(255) NOT NULL,
  `unnecessary` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `unnecessaries`
--

INSERT INTO `unnecessaries` (`id`, `unnecessary`) VALUES
(1, 'to'),
(2, 'at'),
(3, 'in'),
(4, 'search'),
(5, 'look'),
(6, 'Wikipedia');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `request`
--
ALTER TABLE `request`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `unnecessaries`
--
ALTER TABLE `unnecessaries`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `request`
--
ALTER TABLE `request`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
--
-- AUTO_INCREMENT de la tabla `unnecessaries`
--
ALTER TABLE `unnecessaries`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
