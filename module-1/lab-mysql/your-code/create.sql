-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`cars`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`cars` (
  `VIN` INT NOT NULL,
  `manufacturer` VARCHAR(45) NOT NULL,
  `years` VARCHAR(45) NOT NULL,
  `colour` VARCHAR(45) NOT NULL,
  `model` VARCHAR(45) NOT NULL)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`salespersons`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`salespersons` (
  `staff ID` INT NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `store` VARCHAR(45) NOT NULL)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`invoices`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`invoices` (
  `invoice n/` INT NOT NULL,
  `date` DATE NOT NULL,
  `car` VARCHAR(45) NOT NULL,
  `n/ customers` INT NOT NULL,
  `n/ salespeople` INT NOT NULL)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`customers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`customers` (
  `customer ID` INT NOT NULL,
  `name` VARCHAR(45) NULL,
  `phone n/` INT NULL,
  `email` VARCHAR(45) NULL,
  `address` VARCHAR(45) NULL,
  `city` VARCHAR(45) NULL,
  `state` VARCHAR(45) NULL,
  `country` VARCHAR(45) NULL,
  `zip code` INT NULL,
  PRIMARY KEY (`customer ID`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;


-- -----------------------------------------------------
-- INSERTS
-- -----------------------------------------------------

INSERT INTO cars (VIN, manufacturer, years, colour, model) VALUES(3K096, Volkswagen, 2019, Blue, Tiguan);

INSERT INTO cars (VIN, manufacturer, years, colour, model) VALUES(45T96, Ford, 2019, Blue, Fusion);

INSERT INTO cars (VIN, manufacturer, years, colour, model) VALUES(45T96, Ford, - , Blue, Fusion);





















