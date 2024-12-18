-- MySQL dump 10.13  Distrib 5.5.20, for Win64 (x86)
--
-- Host: localhost    Database: result
-- ------------------------------------------------------
-- Server version	5.5.20

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `details`
--

DROP TABLE IF EXISTS `details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `details` (
  `mother_name` varchar(20) DEFAULT NULL,
  `father_name` varchar(20) DEFAULT NULL,
  `d_o_b` varchar(20) DEFAULT NULL,
  `roll` int(11) NOT NULL,
  `name` char(20) DEFAULT NULL,
  PRIMARY KEY (`roll`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `details`
--

LOCK TABLES `details` WRITE;
/*!40000 ALTER TABLE `details` DISABLE KEYS */;
INSERT INTO `details` VALUES ('abcd','efghi','12/13/2252',1,'ram kumar'),('kiran','rajesh','14-09-2003',2,'shivam'),('abcd','efgh','09-09-2003',3,'utkarsh'),('abc','defc','09-09-2004',5,'shashwat');
/*!40000 ALTER TABLE `details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `marks`
--

DROP TABLE IF EXISTS `marks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `marks` (
  `english` int(11) DEFAULT NULL,
  `hindi` int(11) DEFAULT NULL,
  `maths` int(11) DEFAULT NULL,
  `science` int(11) DEFAULT NULL,
  `sst` int(11) DEFAULT NULL,
  `computer` int(11) DEFAULT NULL,
  `roll` int(11) DEFAULT NULL,
  KEY `roll` (`roll`),
  CONSTRAINT `marks_ibfk_1` FOREIGN KEY (`roll`) REFERENCES `details` (`roll`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `marks`
--

LOCK TABLES `marks` WRITE;
/*!40000 ALTER TABLE `marks` DISABLE KEYS */;
INSERT INTO `marks` VALUES (99,90,99,98,98,90,1),(99,98,90,98,97,99,3),(45,44,33,23,32,99,5);
/*!40000 ALTER TABLE `marks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `result`
--

DROP TABLE IF EXISTS `result`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `result` (
  `percentage` char(20) DEFAULT NULL,
  `total_marks` int(11) DEFAULT NULL,
  `roll` int(11) DEFAULT NULL,
  `status` char(20) DEFAULT NULL,
  KEY `roll` (`roll`),
  CONSTRAINT `result_ibfk_1` FOREIGN KEY (`roll`) REFERENCES `details` (`roll`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `result`
--

LOCK TABLES `result` WRITE;
/*!40000 ALTER TABLE `result` DISABLE KEYS */;
INSERT INTO `result` VALUES ('44.0',220,1,'FAIL'),('116.2',581,3,'PASS'),('55.2',276,5,'PASS');
/*!40000 ALTER TABLE `result` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-03-05 11:04:25
