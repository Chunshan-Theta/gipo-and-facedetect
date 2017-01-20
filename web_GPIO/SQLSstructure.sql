-- phpMyAdmin SQL Dump
-- version 4.5.1
-- http://www.phpmyadmin.net
--
-- 主機: 127.0.0.1
-- 產生時間： 2017-01-20 04:44:00
-- 伺服器版本: 10.1.10-MariaDB
-- PHP 版本： 5.6.15

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 資料庫： `gpio`
--

-- --------------------------------------------------------

--
-- 資料表結構 `config`
--

CREATE TABLE `config` (
  `id` int(11) NOT NULL,
  `time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `setting` varchar(9999) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- 資料表的匯出資料 `config`
--

INSERT INTO `config` (`id`, `time`, `setting`) VALUES
(3, '2017-01-17 02:28:45', '[{"id":"0","pin":"7","GPIO":"4","Cost":"50","Device":"é¢¨æ‰‡"},{"id":"1","pin":"11","GPIO":"17","Cost":"null","Device":"null"},{"id":"2","pin":"12","GPIO":"18","Cost":"null","Device":"null"},{"id":"3","pin":"13","GPIO":"21","Cost":"null","Device":"null"},{"id":"4","pin":"15","GPIO":"22","Cost":"null","Device":"null"},{"id":"5","pin":"16","GPIO":"23","Cost":"null","Device":"null"},{"id":"6","pin":"18","GPIO":"24","Cost":"null","Device":"null"},{"id":"7","pin":"19","GPIO":"10","Cost":"null","Device":"null"},{"id":"8","pin":"21","GPIO":"9","Cost":"null","Device":"null"},{"id":"9","pin":"23","GPIO":"11","Cost":"null","Device":"null"},{"id":"10","pin":"24","GPIO":"8","Cost":"null","Device":"null"},{"id":"11","pin":"26","GPIO":"7","Cost":"null","Device":"null"}]'),
(4, '2017-01-17 02:28:49', '[{"id":"0","pin":"7","GPIO":"4","Cost":"50","Device":"é¢¨æ‰‡"},{"id":"1","pin":"11","GPIO":"17","Cost":"null","Device":"null"},{"id":"2","pin":"12","GPIO":"18","Cost":"null","Device":"null"},{"id":"3","pin":"13","GPIO":"21","Cost":"null","Device":"null"},{"id":"4","pin":"15","GPIO":"22","Cost":"null","Device":"null"},{"id":"5","pin":"16","GPIO":"23","Cost":"null","Device":"null"},{"id":"6","pin":"18","GPIO":"24","Cost":"null","Device":"null"},{"id":"7","pin":"19","GPIO":"10","Cost":"null","Device":"null"},{"id":"8","pin":"21","GPIO":"9","Cost":"null","Device":"null"},{"id":"9","pin":"23","GPIO":"11","Cost":"null","Device":"null"},{"id":"10","pin":"24","GPIO":"8","Cost":"null","Device":"null"},{"id":"11","pin":"26","GPIO":"7","Cost":"null","Device":"null"}]'),
(5, '2017-01-17 02:34:20', '[{"id":"0","pin":"7","GPIO":"4","Cost":"50","Device":"é¢¨æ‰‡"},{"id":"1","pin":"11","GPIO":"17","Cost":"null","Device":"null"},{"id":"2","pin":"12","GPIO":"18","Cost":"null","Device":"null"},{"id":"3","pin":"13","GPIO":"21","Cost":"null","Device":"null"},{"id":"4","pin":"15","GPIO":"22","Cost":"null","Device":"null"},{"id":"5","pin":"16","GPIO":"23","Cost":"null","Device":"null"},{"id":"6","pin":"18","GPIO":"24","Cost":"null","Device":"null"},{"id":"7","pin":"19","GPIO":"10","Cost":"null","Device":"null"},{"id":"8","pin":"21","GPIO":"9","Cost":"null","Device":"null"},{"id":"9","pin":"23","GPIO":"11","Cost":"null","Device":"null"},{"id":"10","pin":"24","GPIO":"8","Cost":"null","Device":"null"},{"id":"11","pin":"26","GPIO":"7","Cost":"null","Device":"null"}]'),
(6, '2017-01-17 02:36:21', '[{"id":"0","pin":"7","GPIO":"4","Cost":"50","Device":"é¢¨æ‰‡"},{"id":"1","pin":"11","GPIO":"17","Cost":"null","Device":"null"},{"id":"2","pin":"12","GPIO":"18","Cost":"null","Device":"null"},{"id":"3","pin":"13","GPIO":"21","Cost":"null","Device":"null"},{"id":"4","pin":"15","GPIO":"22","Cost":"null","Device":"null"},{"id":"5","pin":"16","GPIO":"23","Cost":"null","Device":"null"},{"id":"6","pin":"18","GPIO":"24","Cost":"null","Device":"null"},{"id":"7","pin":"19","GPIO":"10","Cost":"null","Device":"null"},{"id":"8","pin":"21","GPIO":"9","Cost":"null","Device":"null"},{"id":"9","pin":"23","GPIO":"11","Cost":"null","Device":"null"},{"id":"10","pin":"24","GPIO":"8","Cost":"null","Device":"null"},{"id":"11","pin":"26","GPIO":"7","Cost":"null","Device":"null"}]'),
(7, '2017-01-17 02:36:59', '[{"id":"0","pin":"7","GPIO":"4","Cost":"50","Device":"é¢¨æ‰‡"},{"id":"1","pin":"11","GPIO":"17","Cost":"null","Device":"null"},{"id":"2","pin":"12","GPIO":"18","Cost":"null","Device":"null"},{"id":"3","pin":"13","GPIO":"21","Cost":"null","Device":"null"},{"id":"4","pin":"15","GPIO":"22","Cost":"null","Device":"null"},{"id":"5","pin":"16","GPIO":"23","Cost":"null","Device":"null"},{"id":"6","pin":"18","GPIO":"24","Cost":"null","Device":"null"},{"id":"7","pin":"19","GPIO":"10","Cost":"null","Device":"null"},{"id":"8","pin":"21","GPIO":"9","Cost":"null","Device":"null"},{"id":"9","pin":"23","GPIO":"11","Cost":"null","Device":"null"},{"id":"10","pin":"24","GPIO":"8","Cost":"null","Device":"null"},{"id":"11","pin":"26","GPIO":"7","Cost":"null","Device":"null"}]'),
(8, '2017-01-17 02:41:34', '[{"id":"0","pin":"7","GPIO":"4","Cost":"50","Device":"é¢¨æ‰‡"},{"id":"1","pin":"11","GPIO":"17","Cost":"null","Device":"null"},{"id":"2","pin":"12","GPIO":"18","Cost":"null","Device":"null"},{"id":"3","pin":"13","GPIO":"21","Cost":"null","Device":"null"},{"id":"4","pin":"15","GPIO":"22","Cost":"null","Device":"null"},{"id":"5","pin":"16","GPIO":"23","Cost":"null","Device":"null"},{"id":"6","pin":"18","GPIO":"24","Cost":"null","Device":"null"},{"id":"7","pin":"19","GPIO":"10","Cost":"null","Device":"null"},{"id":"8","pin":"21","GPIO":"9","Cost":"null","Device":"null"},{"id":"9","pin":"23","GPIO":"11","Cost":"null","Device":"null"},{"id":"10","pin":"24","GPIO":"8","Cost":"null","Device":"null"},{"id":"11","pin":"26","GPIO":"7","Cost":"null","Device":"null"}]'),
(9, '2017-01-17 02:42:14', '[{"id":"0","pin":"7","GPIO":"4","Cost":"50","Device":"é¢¨æ‰‡"},{"id":"1","pin":"11","GPIO":"17","Cost":"null","Device":"null"},{"id":"2","pin":"12","GPIO":"18","Cost":"null","Device":"null"},{"id":"3","pin":"13","GPIO":"21","Cost":"null","Device":"null"},{"id":"4","pin":"15","GPIO":"22","Cost":"null","Device":"null"},{"id":"5","pin":"16","GPIO":"23","Cost":"null","Device":"null"},{"id":"6","pin":"18","GPIO":"24","Cost":"null","Device":"null"},{"id":"7","pin":"19","GPIO":"10","Cost":"null","Device":"null"},{"id":"8","pin":"21","GPIO":"9","Cost":"null","Device":"null"},{"id":"9","pin":"23","GPIO":"11","Cost":"null","Device":"null"},{"id":"10","pin":"24","GPIO":"8","Cost":"null","Device":"null"},{"id":"11","pin":"26","GPIO":"7","Cost":"null","Device":"null"}]'),
(10, '2017-01-17 02:43:39', '[{"id":"0","pin":"7","GPIO":"4","Cost":"50","Device":"é¢¨æ‰‡"},{"id":"1","pin":"11","GPIO":"17","Cost":"200","Device":"å†·æ°£"},{"id":"2","pin":"12","GPIO":"18","Cost":"null","Device":"null"},{"id":"3","pin":"13","GPIO":"21","Cost":"null","Device":"null"},{"id":"4","pin":"15","GPIO":"22","Cost":"null","Device":"null"},{"id":"5","pin":"16","GPIO":"23","Cost":"null","Device":"null"},{"id":"6","pin":"18","GPIO":"24","Cost":"null","Device":"null"},{"id":"7","pin":"19","GPIO":"10","Cost":"null","Device":"null"},{"id":"8","pin":"21","GPIO":"9","Cost":"null","Device":"null"},{"id":"9","pin":"23","GPIO":"11","Cost":"null","Device":"null"},{"id":"10","pin":"24","GPIO":"8","Cost":"null","Device":"null"},{"id":"11","pin":"26","GPIO":"7","Cost":"null","Device":"null"}]');

--
-- 已匯出資料表的索引
--

--
-- 資料表索引 `config`
--
ALTER TABLE `config`
  ADD PRIMARY KEY (`id`);

--
-- 在匯出的資料表使用 AUTO_INCREMENT
--

--
-- 使用資料表 AUTO_INCREMENT `config`
--
ALTER TABLE `config`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
