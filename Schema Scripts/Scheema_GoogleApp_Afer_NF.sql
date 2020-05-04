Create Database GooglePlayNF;
USE GooglePlayNF;
CREATE TABLE `Genre` (
  `Genre_Id` varchar(5) NOT NULL,
  `Genre_Name` varchar(45) NOT NULL,
  PRIMARY KEY (`Genre_Id`)
) ;
CREATE TABLE `Category` (
  `Category_Id` varchar(5) NOT NULL,
  `Category_Name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`Category_Id`)
); 
CREATE TABLE `App` (
  `App_Id` varchar(50) NOT NULL,
  `App_Name` varchar(50) NOT NULL,
  `Category_Id` varchar(5) NOT NULL,
  `Rating` varchar(45) DEFAULT NULL,
  `Reviews` int(11) DEFAULT NULL,
  `Size` varchar(45) DEFAULT NULL,
  `Installs` varchar(45) DEFAULT NULL,
  `Type` varchar(45) DEFAULT NULL,
  `Price` varchar(45) DEFAULT NULL,
  `ContentRating` varchar(45) DEFAULT NULL,
  `Genre_Id` varchar(5) NOT NULL,
  `LastUpdated` varchar(45) DEFAULT NULL,
  `CurrentVersion` varchar(45) DEFAULT NULL,
  `AndroidVersion` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`App_Id`),
  UNIQUE KEY `App_Id_UNIQUE` (`App_Id`),
  KEY `Genres_idx` (`Genre_Id`),
  KEY `Category_idx` (`Category_Id`),
  CONSTRAINT `Category` FOREIGN KEY (`Category_Id`) REFERENCES `Category` (`Category_Id`),
  CONSTRAINT `Genres` FOREIGN KEY (`Genre_Id`) REFERENCES `Genre` (`Genre_Id`)
) ;

