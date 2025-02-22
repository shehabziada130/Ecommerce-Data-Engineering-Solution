# PostgreSQL Staging Data Warehouse Design

## Introduction

This document outlines the design of a staging data warehouse using PostgreSQL, which will integrate sales data from MySQL and catalog data from MongoDB. The warehouse will facilitate data transformation and loading into a production data warehouse running on IBM Db2 for generating various reports.

## Data Warehouse Schema Design

### Star Schema Overview

The data warehouse schema will be designed using a star schema to optimize query performance and facilitate reporting requirements. The star schema includes:

#### Fact Table

**softcartFactSales**
- **orderid**: PRIMARY KEY
- **dateid**: FOREIGN KEY
- **categoryid**: FOREIGN KEY
- **countryid**: FOREIGN KEY
- **itemid**: FOREIGN KEY
- **amount**: Numeric measure of sales

#### Dimension Tables

**softcartDimDate**
- **dateid**: PRIMARY KEY
- **date**: Date value
- **Year**: Year of the date
- **Quarter**: Quarter of the year
- **QuarterName**: Name of the quarter (Q1, Q2, etc.)
- **Month**: Month of the year
- **MonthName**: Name of the month
- **Day**: Day of the month
- **Weekday**: Day of the week (1 for Monday, 7 for Sunday)
- **WeekdayName**: Name of the weekday

**softcartDimCategory**
- **categoryid**: PRIMARY KEY
- **category**: Category of the item

**softcartDimCountry**
- **countryid**: PRIMARY KEY
- **country**: Country of sale

**softcartDimItem**
- **itemid**: PRIMARY KEY
- **item**: Item identifier

### ER Diagram
![softcartRelationships](https://github.com/shehabziada130/Ecommerce-Data-Engineering-Solution/assets/84864669/b6a5dc4f-63d9-4834-a33d-cb03e5361e11)


### Sample Order Data
![sample_order_data](https://github.com/shehabziada130/Ecommerce-Data-Engineering-Solution/assets/84864669/31c68853-eb34-4f30-b4c9-a0fdc09cbb3f)

## Reporting Requirements

The schema design supports the following reporting requirements:

- Total sales per year per country
- Total sales per month per category
- Total sales per quarter per country
- Total sales per category per country

## 2. Export Schema SQL and Create Staging Database

### Export Schema SQL

The following SQL script defines the star schema tables for the PostgreSQL staging data warehouse. This script was generated using the pgAdmin ERD tool.

```sql
-- This script was generated by a beta version of the ERD tool in pgAdmin 4.
-- Please log an issue at https://redmine.postgresql.org/projects/pgadmin4/issues/new if you find any bugs, including reproduction steps.
BEGIN;

CREATE TABLE public."DimCategory"
(
    categoryid smallint NOT NULL,
    category character varying(32)[] NOT NULL,
    PRIMARY KEY (categoryid)
);

CREATE TABLE public."DimCountry"
(
    countryid smallint NOT NULL,
    country character varying(32)[] NOT NULL,
    PRIMARY KEY (countryid)
);

CREATE TABLE public."DimDate"
(
    dateid smallint NOT NULL,
    date date NOT NULL,
    "Year" smallint NOT NULL,
    "Quarter" smallint NOT NULL,
    "QuarterName" character varying(2)[] NOT NULL,
    "Month" smallint NOT NULL,
    "Monthname" character varying(9)[] NOT NULL,
    "Day" smallint NOT NULL,
    "Weekday" smallint NOT NULL,
    "WeekdayName" character varying(9)[] NOT NULL,
    PRIMARY KEY (dateid)
);

CREATE TABLE public."FactSales"
(
    orderid bigint NOT NULL,
    dateid smallint NOT NULL,
    countryid smallint NOT NULL,
    categoryid smallint NOT NULL,
    amount bigint NOT NULL,
    PRIMARY KEY (orderid)
);

ALTER TABLE public."FactSales"
    ADD FOREIGN KEY (dateid)
    REFERENCES public."DimDate" (dateid)
    NOT VALID;

ALTER TABLE public."FactSales"
    ADD FOREIGN KEY (countryid)
    REFERENCES public."DimCountry" (countryid)
    NOT VALID;

ALTER TABLE public."FactSales"
    ADD FOREIGN KEY (categoryid)


    REFERENCES public."DimCategory" (categoryid)
    NOT VALID;

END;
```
## 4. Aggregation Queries

### ROLLUP Query for Total Sales per Year per Country

Execute the following ROLLUP query to calculate total sales per year per country:

```sql
SELECT co.country, d.year, SUM(s.amount) AS totalsales
FROM public."FactSales" AS s
JOIN public."DimCountry" AS co ON co.countryid = s.countryid
JOIN public."DimDate" AS d ON d.dateid = s.dateid
GROUP BY ROLLUP (d.year, co.country)
ORDER BY d.year, co.country;
```

This query produces aggregated total sales data grouped by year and country. See the [full output](https://github.com/shehabziada130/Ecommerce-Data-Engineering-Solution/tree/main/PostgreSQL%20Data%20Warehouse/rollup_data.csv) for details.

### CUBE Query for Average Sales per Year per Country

Execute the following CUBE query to calculate average sales per year per country:

```sql
SELECT co.country, d.year, AVG(s.amount) AS averagesales
FROM public."FactSales" AS s
JOIN public."DimCountry" AS co ON co.countryid = s.countryid
JOIN public."DimDate" AS d ON d.dateid = s.dateid
GROUP BY CUBE (d.year, co.country)
ORDER BY d.year, co.country;
```

This query calculates the average sales grouped by year and country. See the [full output](https://github.com/shehabziada130/Ecommerce-Data-Engineering-Solution/tree/main/PostgreSQL%20Data%20Warehouse/cube.csv) for details.

## 5. Materialized Query Table (MQT)

### Create and Query Materialized Query Table

Create a Materialized Query Table (MQT) named `total_sales_per_country` to store total sales per country:

```sql
CREATE TABLE total_sales_per_country (country VARCHAR, total_sales BIGINT) AS
SELECT co.country, SUM(s.amount) AS totalsales
FROM public."FactSales" AS s
JOIN public."DimCountry" AS co ON co.countryid = s.countryid
GROUP BY co.country;

-- Query the MQT
SELECT * FROM total_sales_per_country;
```

This creates a table `total_sales_per_country` with aggregated total sales data by country. See the sample output below:

| COUNTRY          | TOTAL_SALES |
|------------------|-------------|
| Argentina        | 21755581    |
| Australia        | 21522004    |
| Austria          | 21365726    |
| ...              | ...         |


See the [full output](https://github.com/shehabziada130/Ecommerce-Data-Engineering-Solution/tree/main/PostgreSQL%20Data%20Warehouse/mqt.csv) for details.

