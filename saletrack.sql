-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 26, 2025 at 07:55 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ai chotu`
--

-- --------------------------------------------------------

--
-- Table structure for table `saletrack`
--

CREATE TABLE `saletrack` (
  `SL_No` int(11) NOT NULL,
  `Date_of_Purchase` date DEFAULT NULL,
  `No_of_Item_Sold` int(11) DEFAULT NULL,
  `Date_of_Item_Sold` date DEFAULT NULL,
  `Payment_Method` varchar(50) DEFAULT NULL,
  `Product_No` int(11) DEFAULT NULL,
  `Product_Name` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `saletrack`
--

INSERT INTO `saletrack` (`SL_No`, `Date_of_Purchase`, `No_of_Item_Sold`, `Date_of_Item_Sold`, `Payment_Method`, `Product_No`, `Product_Name`) VALUES
(1, '2023-03-15', 2, '2023-03-15', 'Credit Card', 1001, 'Laptop'),
(2, '2023-03-16', 1, '2023-03-16', 'Cash', 1002, 'Keyboard'),
(3, '2023-03-17', 3, '2023-03-17', 'Debit Card', 1003, 'Mouse'),
(4, '2023-03-18', 2, '2023-03-18', 'Online Payment', 1004, 'Monitor'),
(5, '2023-03-19', 1, '2023-03-19', 'Cash', 1005, 'Printer'),
(6, '2023-03-20', 4, '2023-03-20', 'Credit Card', 1006, 'T-shirt'),
(7, '2023-03-21', 2, '2023-03-21', 'Debit Card', 1008, 'Jeans'),
(8, '2023-03-22', 3, '2023-03-22', 'Online Payment', NULL, NULL),
(9, '2023-03-23', 1, '2023-03-23', 'Cash', 1009, 'Novel'),
(10, '2023-03-24', 5, '2023-03-24', 'Credit Card', 1010, 'Backpack'),
(11, '2023-03-25', 2, '2023-03-25', 'Debit Card', 1011, 'Headphones'),
(12, '2023-03-26', 3, '2023-03-26', 'Online Payment', 1012, 'Smartphone'),
(13, '2023-03-27', 1, '2023-03-27', 'Cash', 1013, 'Tablet'),
(14, '2023-03-28', 4, '2023-03-28', 'Credit Card', 1014, 'Jacket'),
(15, '2023-03-29', 2, '2023-03-29', 'Debit Card', 1015, 'Sunglasses');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `saletrack`
--
ALTER TABLE `saletrack`
  ADD PRIMARY KEY (`SL_No`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `saletrack`
--
ALTER TABLE `saletrack`
  MODIFY `SL_No` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
