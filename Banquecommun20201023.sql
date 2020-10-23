-- MySQL dump 10.13  Distrib 5.7.31, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: banque2
-- ------------------------------------------------------
-- Server version	5.7.31-0ubuntu0.18.04.1

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
-- Table structure for table `clients`
--

DROP TABLE IF EXISTS `clients`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `clients` (
  `identifiant` int(20) NOT NULL AUTO_INCREMENT,
  `numero_compte` char(50) NOT NULL,
  `nom` char(20) NOT NULL,
  `prenom` char(20) NOT NULL,
  `adresse` char(100) NOT NULL,
  PRIMARY KEY (`identifiant`)
) ENGINE=InnoDB AUTO_INCREMENT=107 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clients`
--

LOCK TABLES `clients` WRITE;
/*!40000 ALTER TABLE `clients` DISABLE KEYS */;
INSERT INTO `clients` VALUES (51,'FR4581954495321349960258136','Blin','Dominique','3, chemin de Klein 20557 Sainte Alicenec'),(52,'FR4720392324100766279940239','Gonzalez','Anne','86, rue Valérie Gilbert 83048 Boyer'),(53,'FR3528863872127646000249351','Le Gall','Denis','139, chemin Albert 41667 Vincentboeuf'),(54,'FR1390232512330303068483520','Nguyen','Élisabeth','332, chemin Laine 56179 Bourdonnec'),(61,'FR3682367961324792107181618','Loiseau','Nicolas','avenue Masson 97903 Leroux'),(62,'FR9187955360550069110387507','Raymond','Alexandre','48, rue Julien Gaillard 01700 Noel-sur-Poulain'),(63,'FR4498228345006196479020180','Vallet','Alix','45, boulevard Becker 44949 Perrot'),(64,'FR4380887477130031650551166','Marin','Susanne','11, chemin Adam 99087 Texier-les-Bains'),(65,'FR4323486793356893083930095','Moulin','Juliette','28, rue Adrien Vincent 72473 Carlier-sur-Dupuis'),(66,'FR4728592670987094423819670','Bonnin','William','rue David 09163 Sainte Dorothée-les-Bains'),(67,'FR6445336446478248485694040','Besnard','Charlotte','45, boulevard de Barbier 86648 Simon'),(68,'FR8338747372769043554060439','Valette','Dominique','44, rue de Ferrand 27038 Saint Denisdan'),(69,'FR2778887212699716768626604','Picard','Franck','2, avenue Laurent Martineau 67094 Mace-la-Forêt'),(70,'FR2794851178442630987804604','Klein','Maurice','437, chemin Weiss 05053 Saint Aurélieboeuf'),(71,'FR7590499685210535420101322','Gilbert','Alexandre','66, boulevard Paul 31822 Gilbert'),(72,'FR4125975843720805400439414','Merle','Arthur','657, rue de Lebreton 57120 Renault'),(73,'FR7849555031494024267992590','Humbert','Georges','rue de Poirier 80089 Diaz'),(74,'FR9386746760846823607077509','Guibert','Françoise','chemin Zoé Carpentier 02206 Colas'),(75,'FR6618653052320033364582319','Poulain','Céline','96, rue de Traore 06479 Saint Jeanne-sur-Mer'),(76,'FR0655603084557335926677307','Benoit','Laetitia','7, rue de Lefevre 61296 Dufour'),(77,'FR2680670572140634482461386','Launay','Émile','boulevard Jacquet 61813 Vidalboeuf'),(78,'FR5913271152513295307978523','Benard','Nicole','50, boulevard Rousseau 84992 Chevallier'),(79,'FR9538007629552974937711933','Lopez','Paulette','46, avenue Maurice 31087 Jourdan'),(80,'FR3699222232718543189991729','Marion','Julien','5, boulevard Boucher 58725 Saint Agnèsnec'),(81,'FR6301472518314090422880240','Rodrigues','Gabriel','avenue David 31182 Remy-la-Forêt'),(82,'FR0265482135992618806135836','Pires','Lucy','75, chemin de Dupuy 42365 Sainte Luc-la-Forêt'),(83,'FR5616009210330640069117077','Leroux','Gabrielle','16, rue Pires 79821 PruvostBourg'),(84,'FR7585023590588748533924123','Durand','Simone','717, boulevard de Leduc 15985 Peltier-sur-Dupuis'),(85,'FR5265425474709830368265451','Wagner','Vincent','18, boulevard de Gomez 58631 Legendre'),(86,'FR8948473806960176238730377','Gillet','Paul','105, avenue Michel Guillot 11728 Georges'),(87,'FR0665060519757868508082657','Ruiz','Stéphane','19, rue Brunel 84978 LeroyVille'),(88,'FR1170289332818496800320671','Guillot','Simone','21, chemin Pierre 95624 Bonneau'),(89,'FR7199530168227032875184869','Herve','Benoît','335, chemin de Mendes 09633 Chevalliernec'),(90,'FR9526218421472513302561174','Raymond','Nicole','199, rue Arthur Mahe 41745 Hamondan'),(91,'FR3771938702599661933678558','Guyot','Julie','85, chemin de Leveque 61016 Saint Jeannine'),(92,'FR9472184633311988499180013','Bazin','Henri','2, chemin Antoinette Rocher 10172 Fischer-les-Bains'),(93,'FR4584054967192501187356747','Clerc','Nicole','27, avenue Gay 33138 Rossi'),(94,'FR0856025117921875330333647','Clerc','Lorraine','4, avenue Lucie Cousin 17753 Fournier-sur-Chevallier'),(95,'FR5234055873834942987303639','Lemoine','Roger','840, chemin Henry 76127 Collin'),(96,'FR1076812136018510068175007','Lacombe','Adrienne','rue Xavier Pons 90932 PottierBourg'),(97,'FR7173392893521698283459548','Hamel','Christophe','43, avenue Teixeira 27215 Perrier'),(98,'FR9021271459413248166513494','Chretien','Margot','15, avenue André Chauveau 48088 Voisin-sur-Descamps'),(99,'FR7253004518702958168527921','Didier','Franck','83, avenue Delattre 44318 Saint Nicolas'),(100,'FR7263329422372907257535418','Diaz','Monique','47, rue Delahaye 63447 Dumas'),(101,'FR2783849313522110448607020','Gomes','Alexandre','42, rue Capucine Hamon 75469 Seguin-sur-Carlier'),(102,'FR0378474319369838664946708','Levy','David','97, rue Claire Gaudin 77923 Dupuy-les-Bains'),(103,'FR7539498007626359736809186','Royer','Gilles','boulevard Lopez 46259 Baillynec'),(104,'FR1687558942888530109210447','Sauvage','Xavier','30, rue de Bonneau 85162 Cordier'),(105,'FR2502600293293160214632468','Marechal','Luc','1, rue de Lemoine 03926 Dupuy'),(106,'FR3272567503818941383840178','Raymond','Antoine','avenue Nathalie Thibault 61933 Paul');
/*!40000 ALTER TABLE `clients` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `comptes`
--

DROP TABLE IF EXISTS `comptes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `comptes` (
  `id_compte` int(20) NOT NULL,
  `id_client` int(20) NOT NULL,
  `solde` float NOT NULL,
  PRIMARY KEY (`id_compte`),
  KEY `id_client` (`id_client`),
  CONSTRAINT `comptes_ibfk_1` FOREIGN KEY (`id_client`) REFERENCES `clients` (`identifiant`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comptes`
--

LOCK TABLES `comptes` WRITE;
/*!40000 ALTER TABLE `comptes` DISABLE KEYS */;
INSERT INTO `comptes` VALUES (1,51,4684.02),(2,52,1689.05),(3,53,7040.06),(4,54,-22.022),(5,101,2689.15),(6,102,-1229.78),(7,103,3382.37),(8,104,-1630.41),(9,105,5365.7),(10,106,-1442.3),(11,61,9359.14),(12,62,7355.73),(13,63,2708.69),(14,64,-2185.59),(15,65,2755.6),(16,66,3748.33),(17,67,3848.17),(18,68,6885.03),(19,69,3732.64),(20,70,3962.19),(21,71,5699.9),(22,72,5674.7),(23,73,9653.56),(24,74,-1390.22),(25,75,793.653),(26,76,8719.77),(27,77,4462.72),(28,78,8305.36),(29,79,8899.69),(30,80,1347.77),(31,81,8827.55),(32,82,9871.33),(33,83,4386.14),(34,84,-1721.15),(35,85,2621.18),(36,86,450.967),(37,87,6193.15),(38,88,-206.654),(39,89,5409.01),(40,90,9576.07),(41,91,9421.1),(42,92,-412.614),(43,93,3590.29),(44,94,7548.71),(45,95,5056.28),(46,96,5336.08),(47,97,-2573.5),(48,98,7511.54),(49,99,6892.56),(50,100,-4164.01);
/*!40000 ALTER TABLE `comptes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `operations`
--

DROP TABLE IF EXISTS `operations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `operations` (
  `id_operation` int(20) NOT NULL AUTO_INCREMENT,
  `id_compte` int(20) NOT NULL,
  `nb_operations` int(20) NOT NULL,
  `nb_decouverts_dans_lannee` int(20) NOT NULL,
  PRIMARY KEY (`id_operation`),
  KEY `id_compte` (`id_compte`),
  CONSTRAINT `operations_ibfk_1` FOREIGN KEY (`id_compte`) REFERENCES `comptes` (`id_compte`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `operations`
--

LOCK TABLES `operations` WRITE;
/*!40000 ALTER TABLE `operations` DISABLE KEYS */;
INSERT INTO `operations` VALUES (1,1,54,9),(2,2,67,1),(3,3,66,4),(4,4,65,6),(5,5,64,3),(6,6,57,8),(7,7,66,10),(8,8,56,0),(9,9,51,0),(10,10,55,0),(11,11,62,2),(12,12,57,2),(13,13,57,8),(14,14,69,0),(15,15,51,0),(16,16,56,4),(17,17,65,3),(18,18,66,3),(19,19,52,4),(20,20,57,3),(21,21,57,8),(22,22,53,0),(23,23,57,9),(24,24,50,6),(25,25,63,10),(26,26,52,3),(27,27,57,7),(28,28,58,9),(29,29,52,5),(30,30,60,7),(31,31,58,3),(32,32,60,9),(33,33,63,8),(34,34,56,7),(35,35,61,2),(36,36,58,3),(37,37,56,4),(38,38,60,3),(39,39,59,7),(40,40,50,10),(41,41,65,7),(42,42,56,1),(43,43,55,0),(44,44,61,6),(45,45,51,7),(46,46,55,2),(47,47,50,6),(48,48,50,3),(49,49,51,4),(50,50,54,0);
/*!40000 ALTER TABLE `operations` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-10-23 15:58:00
