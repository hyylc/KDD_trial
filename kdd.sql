CREATE DATABASE  IF NOT EXISTS `kdd` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `kdd`;
-- MySQL dump 10.13  Distrib 8.0.20, for Win64 (x86_64)
--
-- Host: localhost    Database: kdd
-- ------------------------------------------------------
-- Server version	5.7.24

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admin` (
  `idadmin` int(11) NOT NULL,
  `admin_name` varchar(45) NOT NULL,
  `admin_password` varchar(45) NOT NULL,
  PRIMARY KEY (`idadmin`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ans`
--

DROP TABLE IF EXISTS `ans`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ans` (
  `idans` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `q_id` int(11) NOT NULL,
  `ans_one` int(11) NOT NULL,
  `ans_two` int(11) NOT NULL,
  `pf` decimal(20,0) NOT NULL,
  `b` decimal(20,0) NOT NULL,
  PRIMARY KEY (`idans`),
  KEY `fk2_idx` (`user_id`),
  KEY `fk3_idx` (`q_id`),
  CONSTRAINT `fk2` FOREIGN KEY (`user_id`) REFERENCES `user` (`iduser`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk3` FOREIGN KEY (`q_id`) REFERENCES `q` (`idq`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ans`
--

LOCK TABLES `ans` WRITE;
/*!40000 ALTER TABLE `ans` DISABLE KEYS */;
/*!40000 ALTER TABLE `ans` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `option`
--

DROP TABLE IF EXISTS `option`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `option` (
  `idoption` int(11) NOT NULL,
  `q_id` int(11) NOT NULL,
  `option_description` varchar(45) NOT NULL,
  `option_num` int(11) NOT NULL,
  PRIMARY KEY (`idoption`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `option`
--

LOCK TABLES `option` WRITE;
/*!40000 ALTER TABLE `option` DISABLE KEYS */;
/*!40000 ALTER TABLE `option` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `q`
--

DROP TABLE IF EXISTS `q`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `q` (
  `idq` int(11) NOT NULL,
  `q_id_of_setq` int(11) NOT NULL,
  `q_description` varchar(250) NOT NULL,
  `q_MV_one` int(11) DEFAULT NULL,
  `q_MV_two` int(11) DEFAULT NULL,
  `q_TD_one` int(11) DEFAULT NULL,
  `q_TD_two` int(11) DEFAULT NULL,
  `q_num_of_ans` int(11) NOT NULL,
  PRIMARY KEY (`idq`),
  KEY `fk1_idx` (`q_id_of_setq`),
  CONSTRAINT `fk1` FOREIGN KEY (`q_id_of_setq`) REFERENCES `setq` (`idsetQ`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `q`
--

LOCK TABLES `q` WRITE;
/*!40000 ALTER TABLE `q` DISABLE KEYS */;
/*!40000 ALTER TABLE `q` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `setq`
--

DROP TABLE IF EXISTS `setq`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `setq` (
  `idsetQ` int(11) NOT NULL,
  `setQ_description` varchar(250) NOT NULL,
  `setQ_pf` varchar(45) NOT NULL,
  `setQ_b` varchar(45) NOT NULL,
  PRIMARY KEY (`idsetQ`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `setq`
--

LOCK TABLES `setq` WRITE;
/*!40000 ALTER TABLE `setq` DISABLE KEYS */;
/*!40000 ALTER TABLE `setq` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `iduser` int(11) NOT NULL,
  `user_name` varchar(45) NOT NULL,
  `user_password` varchar(45) NOT NULL,
  PRIMARY KEY (`iduser`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'hyy','hyy19990907'),(2,'lcj','lcj19961119'),(3,'hy','h'),(4,'hy','hh');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `weight`
--

DROP TABLE IF EXISTS `weight`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `weight` (
  `idweight` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `setq_id` int(11) NOT NULL,
  `weight_one` decimal(20,0) NOT NULL,
  `weight_two` decimal(20,0) DEFAULT NULL,
  PRIMARY KEY (`idweight`),
  KEY `fk4_idx` (`user_id`),
  KEY `fk5_idx` (`setq_id`),
  CONSTRAINT `fk4` FOREIGN KEY (`user_id`) REFERENCES `user` (`iduser`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk5` FOREIGN KEY (`setq_id`) REFERENCES `setq` (`idsetQ`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `weight`
--

LOCK TABLES `weight` WRITE;
/*!40000 ALTER TABLE `weight` DISABLE KEYS */;
/*!40000 ALTER TABLE `weight` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-03-08 10:28:14
