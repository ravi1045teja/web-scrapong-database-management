Create database DAL_1;
USE DAL_1;
#DEPARTMENT TABLE

CREATE TABLE `Department` (
  `DepartmentId` varchar(5) NOT NULL,
  `DepartmentName` varchar(45) NOT NULL,
  PRIMARY KEY (`DepartmentId`),
  UNIQUE KEY `DepartmentId_UNIQUE` (`DepartmentId`)
) ;

#UNDERGRADUATE PROGRAMS

CREATE TABLE `UnderGraduatePrograms` (
  `UGID` varchar(5) NOT NULL,
  `UgName` varchar(45) DEFAULT NULL,
  `DepartmentId` varchar(5) DEFAULT NULL,
  PRIMARY KEY (`UGID`),
  UNIQUE KEY `UGID_UNIQUE` (`UGID`),
  KEY `DepartmentU_idx` (`DepartmentId`),
  CONSTRAINT `DepartmentU` FOREIGN KEY (`DepartmentId`) REFERENCES `Department` (`DepartmentId`)
) ;

#GRADUATE PROGRAMS

CREATE TABLE `GraduatePrograms` (
  `GraduateId` varchar(5) NOT NULL,
  `GraduateProgramName` varchar(45) DEFAULT NULL,
  `DepartmentId` varchar(5) DEFAULT NULL,
  PRIMARY KEY (`GraduateId`),
  KEY `DepartmentG_idx` (`DepartmentId`),
  CONSTRAINT `DepartmentG` FOREIGN KEY (`DepartmentId`) REFERENCES `Department` (`DepartmentId`)
) ;

#EMPLOYEES

CREATE TABLE `Employee` (
  `EmpId` varchar(5) NOT NULL,
  `FirstName` varchar(45) DEFAULT NULL,
  `LastName` varchar(45) DEFAULT NULL,
  `DepartmentId` varchar(5) DEFAULT NULL,
  PRIMARY KEY (`EmpId`),
  UNIQUE KEY `EmpId_UNIQUE` (`EmpId`),
  KEY `DepartmentE_idx` (`DepartmentId`),
  CONSTRAINT `DepartmentE` FOREIGN KEY (`DepartmentId`) REFERENCES `Department` (`DepartmentId`)
) ;

#COURSES

CREATE TABLE `Course` (
  `CourseId` varchar(5) NOT NULL,
  `CourseName` varchar(45) DEFAULT NULL,
  `ProgramId` varchar(5) DEFAULT NULL,
  PRIMARY KEY (`CourseId`),
  UNIQUE KEY `CourseId_UNIQUE` (`CourseId`),
  KEY `CourseSpecific_idx` (`ProgramId`),
  CONSTRAINT `CourseSpecific` FOREIGN KEY (`ProgramId`) REFERENCES `GraduatePrograms` (`GraduateId`),
  CONSTRAINT `CourseSpecificU` FOREIGN KEY (`ProgramId`) REFERENCES `UnderGraduatePrograms` (`UGID`)
) ;

#BUILDINGS

CREATE TABLE `Buildings` (
  `BuildingId` varchar(5) NOT NULL,
  `BuildingName` varchar(45) DEFAULT NULL,
  `Location` varchar(2) DEFAULT NULL,
  `LoungeArea` varchar(2) DEFAULT NULL,
  `StudySpace` varchar(2) DEFAULT NULL,
  `FoodServices` varchar(2) DEFAULT NULL,
  `Wifi` varchar(2) DEFAULT NULL,
  PRIMARY KEY (`BuildingId`),
  UNIQUE KEY `BuildingId_UNIQUE` (`BuildingId`)
) ;

#RESIDENCIES

CREATE TABLE `Residencies` (
  `ResidencyId` varchar(5) NOT NULL,
  `ResidencyBuildingName` varchar(45) DEFAULT NULL,
  `RoomTypeId` varchar(45) DEFAULT NULL,
  `ResidencyType` varchar(45) DEFAULT NULL,
  `Location` varchar(45) DEFAULT NULL,
  `FallFees` int(11) DEFAULT NULL,
  `WinterFees` int(11) DEFAULT NULL,
  `TotalFees` int(11) DEFAULT NULL,
  PRIMARY KEY (`ResidencyId`),
  UNIQUE KEY `ResidencyId_UNIQUE` (`ResidencyId`)
) ;



#RESEARCH
CREATE TABLE `Research` (
  `ResearchId` varchar(5) NOT NULL,
  `ResearchInstitute` varchar(150) NOT NULL,
  `ResearchAreas` varchar(150) NOT NULL,
  PRIMARY KEY (`ResearchId`,`ResearchInstitute`,`ResearchAreas`),
  UNIQUE KEY `ResearchId_UNIQUE` (`ResearchId`)
) ;


#FUNDING OPPORTUNITIES

CREATE TABLE `FundingOpportunities` (
  `FundingId` varchar(5) NOT NULL,
  `FundingName` varchar(45) NOT NULL,
  `FundingValue` int(11) DEFAULT NULL,
  `DeadlineDate` datetime DEFAULT NULL,
  PRIMARY KEY (`FundingId`),
  UNIQUE KEY `FundingId_UNIQUE` (`FundingId`)
) ;

#BOOK STORE

CREATE TABLE `BookStore` (
  `Location` varchar(25) DEFAULT NULL,
  `StoreId` varchar(5) NOT NULL,
  `Timings` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`StoreId`),
  UNIQUE KEY `StoreId_UNIQUE` (`StoreId`)
);







