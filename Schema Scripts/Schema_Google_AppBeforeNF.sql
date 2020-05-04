Create Database KaggleApp;
Use KaggleApp;

#App table

CREATE TABLE `App` (
  `App_Id` varchar(50) NOT NULL,
  `App_Name` varchar(150) NOT NULL,
  `Category` varchar(100) NOT NULL,
  `Rating` varchar(45) DEFAULT NULL,
  `Reviews` int(11) DEFAULT NULL,
  `Size` varchar(45) DEFAULT NULL,
  `Installs` varchar(45) DEFAULT NULL,
  `Type` varchar(45) DEFAULT NULL,
  `Price` varchar(45) DEFAULT NULL,
  `Content` varchar(45) DEFAULT NULL,
  `Genres` varchar(45) DEFAULT NULL,
  `LastUpdated` varchar(45) DEFAULT NULL,
  `CurrentVersion` varchar(45) DEFAULT NULL,
  `AndroidVersion` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`App_Id`),
  UNIQUE KEY `App_Id_UNIQUE` (`App_Id`),
  UNIQUE KEY `App_Name_UNIQUE` (`App_Name`)
) 

