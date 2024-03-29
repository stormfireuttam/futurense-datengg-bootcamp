-- Drop table if already exists
Drop table sales;

-- Create Table and Define Schema
CREATE OR REPLACE TABLE sales(
Region varchar(80),Country varchar(80),Item_Type varchar(80),Sales_Channel varchar(80),Order_Priority varchar(80),
Order_Date varchar(25),Order_ID varchar(80),Ship_Date varchar(25),
Units_Sold int,Unit_Price int,Unit_Cost int,Total_Revenue int,Total_Cost int,Total_Profit int
);

-- Stage the data 
put file://C:\Users\miles.MILE-BL-3968-LA\Downloads\Sales_Records.csv @MILES.PUBLIC.%sales;
put file://C:\Users\miles.MILE-BL-3968-LA\Downloads\Sales_Records.csv @~/staged;

-- Copy the data from stage into sales table
COPY INTO sales FROM '@MILES.PUBLIC.%sales/Sales_Records.csv.gz' FILE_FORMAT=(TYPE=CSV, COMPRESSION = GZIP, SKIP_HEADER=1, FIELD_DELIMITER=',');
COPY INTO sales FROM '@~/staged/Sales_Records.csv.gz' FILE_FORMAT=(TYPE=CSV, COMPRESSION = GZIP, SKIP_HEADER=1, FIELD_DELIMITER=',');

-- View the data
select * from sales;
