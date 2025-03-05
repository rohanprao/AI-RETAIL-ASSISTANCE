-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 26, 2025 at 07:54 AM
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
-- Table structure for table `product_detail`
--

CREATE TABLE `product_detail` (
  `SI_No` int(11) NOT NULL,
  `Product_No` int(11) DEFAULT NULL,
  `Product_Name` varchar(255) DEFAULT NULL,
  `MFD` date DEFAULT NULL,
  `EFD` date DEFAULT NULL,
  `Quantity` int(11) DEFAULT NULL,
  `Price` decimal(10,2) DEFAULT NULL,
  `Lot_Price` decimal(10,2) DEFAULT NULL,
  `Category` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `product_detail`
--

INSERT INTO `product_detail` (`SI_No`, `Product_No`, `Product_Name`, `MFD`, `EFD`, `Quantity`, `Price`, `Lot_Price`, `Category`) VALUES
(1, 1001, 'Laptop', '2023-03-01', '2024-03-01', 100, 1000.00, 10000.00, 'Electronics'),
(2, 1002, 'Keyboard', '2023-04-01', '2024-04-01', 200, 50.00, 1000.00, 'Electronics'),
(3, 1003, 'Mouse', '2023-05-01', '2024-05-01', 300, 20.00, 600.00, 'Electronics'),
(4, 1004, 'Monitor', '2023-06-01', '2024-06-01', 50, 500.00, 25000.00, 'Electronics'),
(5, 1005, 'Printer', '2023-07-01', '2024-07-01', 100, 150.00, 15000.00, 'Electronics'),
(6, 1006, 'T-shirt', '2023-08-01', '2024-08-01', 500, 10.00, 5000.00, 'Clothing'),
(7, 1007, 'Jeans', '2023-09-01', '2024-09-01', 300, 25.00, 7500.00, 'Clothing'),
(8, 1008, 'Shoes', '2023-10-01', '2024-10-01', 200, 50.00, 10000.00, 'Clothing'),
(9, 1009, 'Novel', '2023-11-01', '2024-11-01', 150, 15.00, 2250.00, 'Books'),
(10, 1010, 'Backpack', '2023-12-01', '2024-12-01', 80, 30.00, 2400.00, 'Accessories'),
(11, 1011, 'Headphones', '2023-01-01', '2024-01-01', 120, 75.00, 9000.00, 'Electronics'),
(12, 1012, 'Smartphone', '2023-02-01', '2024-02-01', 60, 800.00, 48000.00, 'Electronics'),
(13, 1013, 'Tablet', '2023-03-15', '2024-03-15', 90, 300.00, 27000.00, 'Electronics'),
(14, 1014, 'Jacket', '2023-04-15', '2024-04-15', 150, 60.00, 9000.00, 'Clothing'),
(15, 1015, 'Sunglasses', '2023-05-15', '2024-05-15', 200, 20.00, 4000.00, 'Accessories'),
(19, NULL, 'Lays Chips', NULL, NULL, NULL, 50.00, NULL, NULL),
(20, 0, 'Samsung TV', '2022-01-01', '2022-01-31', 100, 400.00, 40000.00, 'Electronics'),
(21, NULL, 'Kurkure', NULL, NULL, 100, 5.00, 500.00, 'Snacks'),
(22, NULL, 'Maggie', NULL, NULL, 10, 10.00, 10.00, 'Food'),
(24, NULL, 'umbrella', '2022-01-01', '2022-01-01', 0, 250.00, 250.00, 'Accessories'),
(25, NULL, 'Umbrella', NULL, NULL, NULL, 250.00, NULL, NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `product_detail`
--
ALTER TABLE `product_detail`
  ADD PRIMARY KEY (`SI_No`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `product_detail`
--
ALTER TABLE `product_detail`
  MODIFY `SI_No` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
