-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: project_management
-- ------------------------------------------------------
-- Server version	8.0.28

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `class_work`
--

DROP TABLE IF EXISTS `class_work`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `class_work` (
  `sub_code` char(7) NOT NULL,
  `sub_name` varchar(10) DEFAULT NULL,
  `assignment_num` int DEFAULT NULL,
  `link_work` varchar(300) DEFAULT NULL,
  `date_given` date DEFAULT NULL,
  `due_date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `class_work`
--

LOCK TABLES `class_work` WRITE;
/*!40000 ALTER TABLE `class_work` DISABLE KEYS */;
INSERT INTO `class_work` VALUES ('CS3CO09','OS',4,'dhbs','2022-04-25','2022-09-04');
/*!40000 ALTER TABLE `class_work` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cp`
--

DROP TABLE IF EXISTS `cp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cp` (
  `assignment_num` int DEFAULT NULL,
  `enrollment_num` varchar(12) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cp`
--

LOCK TABLES `cp` WRITE;
/*!40000 ALTER TABLE `cp` DISABLE KEYS */;
/*!40000 ALTER TABLE `cp` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dbms`
--

DROP TABLE IF EXISTS `dbms`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dbms` (
  `assignment_num` int DEFAULT NULL,
  `enrollment_num` varchar(12) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dbms`
--

LOCK TABLES `dbms` WRITE;
/*!40000 ALTER TABLE `dbms` DISABLE KEYS */;
/*!40000 ALTER TABLE `dbms` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `os`
--

DROP TABLE IF EXISTS `os`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `os` (
  `assignment_num` int DEFAULT NULL,
  `enrollment_num` varchar(12) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `os`
--

LOCK TABLES `os` WRITE;
/*!40000 ALTER TABLE `os` DISABLE KEYS */;
/*!40000 ALTER TABLE `os` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `toc`
--

DROP TABLE IF EXISTS `toc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `toc` (
  `assignment_num` int DEFAULT NULL,
  `enrollment_num` varchar(12) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `toc`
--

LOCK TABLES `toc` WRITE;
/*!40000 ALTER TABLE `toc` DISABLE KEYS */;
/*!40000 ALTER TABLE `toc` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` varchar(15) DEFAULT NULL,
  `password` varchar(20) DEFAULT NULL,
  `status` char(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('admin','master','t'),('en20cs301061','en20cs301061','s'),('en20cs301062','en20cs301062','s'),('en20cs301063','en20cs301063','s'),('en20cs301064','en20cs301064','s'),('en20cs301065','en20cs301065','s'),('en20cs301066','en20cs301066','s'),('en20cs301067','en20cs301067','s'),('en20cs301068','en20cs301068','s'),('en20cs301069','en20cs301069','s'),('en20cs301070','en20cs301070','s'),('en20cs301071','en20cs301071','s'),('en20cs301072','en20cs301072','s'),('en20cs301073','en20cs301073','s'),('en20cs301074','en20cs301074','s'),('en20cs301075','en20cs301075','s'),('en20cs301076','en20cs301076','s'),('en20cs301077','en20cs301077','s'),('en20cs301078','en20cs301078','s'),('en20cs301079','en20cs301079','s'),('en20cs301080','en20cs301080','s'),('en20cs301081','en20cs301081','s'),('en20cs301082','en20cs301082','s'),('en20cs301083','en20cs301083','s'),('en20cs301084','en20cs301084','s'),('en20cs301085','en20cs301085','s'),('en20cs301086','en20cs301086','s'),('en20cs301087','en20cs301087','s'),('en20cs301088','en20cs301088','s'),('en20cs301089','en20cs301089','s'),('en20cs301090','en20cs301090','s'),('en20cs301091','en20cs301091','s'),('en20cs301092','en20cs301092','s'),('en20cs301093','en20cs301093','s'),('en20cs301094','en20cs301094','s'),('en20cs301095','en20cs301095','s'),('en20cs301096','en20cs301096','s'),('en20cs301097','en20cs301097','s'),('en20cs301098','en20cs301098','s'),('en20cs301099','en20cs301099','s'),('en20cs301100','en20cs301100','s'),('en20cs301101','en20cs301101','s'),('en20cs301102','en20cs301102','s'),('en20cs301103','en20cs301103','s'),('en20cs301104','en20cs301104','s'),('en20cs301105','en20cs301105','s'),('en20cs301106','en20cs301106','s'),('en20cs301107','en20cs301107','s'),('en20cs301108','en20cs301108','s'),('en20cs301109','en20cs301109','s'),('en20cs301110','en20cs301110','s'),('en20cs301111','en20cs301111','s'),('en20cs301112','en20cs301112','s'),('en20cs301113','en20cs301113','s'),('en20cs301114','en20cs301114','s'),('en20cs301115','en20cs301115','s'),('en20cs301116','en20cs301116','s'),('en20cs301117','en20cs301117','s'),('en20cs301118','en20cs301118','s'),('en20cs301119','en20cs301119','s'),('en20cs301120','en20cs301120','s'),('en20cs301121','en20cs301121','s'),('en20cs301122','en20cs301122','s'),('en20cs301123','en20cs301123','s'),('en20cs301124','en20cs301124','s'),('en20cs301125','en20cs301125','s'),('en20cs301126','en20cs301126','s'),('en20cs301127','en20cs301127','s');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-27  1:06:41
