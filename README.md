Supermarket Sales Power BI Project

A complete data analytics portfolio project based on a cleaned dataset of 500 supermarket sales transactions.

1. Project Overview

The objective of this project is to analyze supermarket sales data and create a professional dashboard that helps understand:

Overall sales performance

Transaction volume

Quantity sold

Average transaction value

Customer ratings

Product-wise sales

Branch-wise sales

Category-wise sales

City-wise sales

Payment method usage

Customer type behavior

Gender-wise performance

Interactive filtering and detailed product analysis

2. Dataset

The cleaned dataset contains 500 transactions and the following 13 columns:

Column

Description

Invoice ID

Unique transaction/invoice identifier

Date

Transaction date

Branch

Supermarket branch

City

City of the branch

Customer Type

Member or Normal

Gender

Customer gender

Product

Product purchased

Category

Product category

Quantity

Quantity purchased

Unit Price

Price per unit

Payment

Payment method

Rating

Customer rating

Sales

Total transaction sales

The Sales value is validated against:

Sales = Quantity × Unit Price

3. Data Cleaning and Validation

Before analysis, the dataset was cleaned and validated.

Checks performed:

Checked for blank/missing cells

Checked for duplicate rows

Checked for duplicate Invoice IDs

Checked Sales calculation consistency

Verified numeric fields

Verified date field

Applied appropriate Excel formatting

Added a data-quality check sheet to the cleaned workbook

Final validation:

Rows: 500

Columns: 13

Blank cells: 0

Duplicate rows: 0

Duplicate Invoice IDs: 0

Sales calculation mismatches: 0

4. Project Structure

Supermarket-Sales-Analysis/
│
├── Data/
│   └── Supermarket_Sales_Cleaned_Final.xlsx
│
├── Python/
│   └── supermarket_sales_analysis.py
│
├── Reports/
│   ├── Supermarket_Sales_Analysis.xlsx
│   └── Charts/
│       ├── branch_sales.png
│       ├── category_sales.png
│       ├── customer_type_average.png
│       ├── payment_methods.png
│       └── product_sales.png
│
├── PowerBI/
│   └── Power BI project files
│
├── requirements.txt
└── README.md

5. Technologies Used

Microsoft Excel

Python

Pandas

Matplotlib

Power BI

DAX

PBIP / PBIR / TMDL

6. Python Analysis

Python is used for:

Loading the cleaned Excel dataset

Validating the data

Calculating KPIs

Performing grouped analysis

Analyzing products

Analyzing branches

Analyzing categories

Analyzing payment methods

Analyzing customer types

Analyzing gender

Analyzing ratings

Analyzing cities

Exporting analysis results

Generating charts

Python packages

Install dependencies using:

pip install -r requirements.txt

The main packages are:

pandas
openpyxl
matplotlib

Run Python analysis

From the project root:

python Python/supermarket_sales_analysis.py

The script generates:

Reports/Supermarket_Sales_Analysis.xlsx

and the chart files inside:

Reports/Charts/

7. Key Performance Indicators

The completed analysis produced the following overall KPIs:

KPI

Value

Total Sales

₹244,411.08

Total Transactions

500

Total Quantity Sold

2,768

Average Transaction Value

₹488.82

Average Rating

3.99 / 5

8. Key Findings

Product Performance

Cheese recorded the highest product sales:

₹27,906.30

Branch Performance

Branch C (Mumbai) recorded the highest sales:

₹72,469.45

Category Performance

Beverages recorded the highest category sales:

₹56,108.24

Payment Methods

UPI was the most-used payment method:

127 transactions

Customer Type

Average transaction value:

Member: ₹483.14

Normal: ₹497.07

Customer Rating

Overall average rating:

3.99 / 5

These findings are descriptive results from the supplied dataset.

9. Power BI Dashboard

The Power BI dashboard is designed around the cleaned dataset.

Page 1 — Sales Dashboard

The main dashboard contains five KPI cards:

Total Sales

Total Transactions

Total Quantity Sold

Average Transaction Value

Average Rating

Main Visuals

Sales by Product

Sales by Branch

Sales by Category

Payment Method Distribution

Average Transaction by Customer Type

Sales by City

Page 2 — Filters & Details

The second page is designed for interactive analysis.

Slicers

Branch

City

Category

Payment

Customer Type

Gender

Detail Table

The product detail table contains:

Product

Category

Quantity

Sales

This allows users to filter the data and inspect individual product performance.

10. DAX Measures

The following measures are used for the dashboard.

Total Sales

Total Sales = SUM(Sales_Data_Cleaned[Sales])

Total Transactions

Total Transactions =
DISTINCTCOUNT(Sales_Data_Cleaned[Invoice ID])

Total Quantity Sold

Total Quantity Sold =
SUM(Sales_Data_Cleaned[Quantity])

Average Transaction Value

Average Transaction Value =
DIVIDE(
    [Total Sales],
    [Total Transactions]
)

Average Rating

Average Rating =
AVERAGE(Sales_Data_Cleaned[Rating])

11. Dashboard Visual Configuration

Sales by Product

Visual:

Clustered Bar Chart

Fields:

Y-axis → Product
X-axis → Total Sales

Sort:

Total Sales → Descending

Sales by Branch

Visual:

Column Chart

Fields:

X-axis → Branch
Y-axis → Total Sales

Sales by Category

Visual:

Donut Chart

Fields:

Legend → Category
Values → Total Sales

Payment Method Distribution

Visual:

Donut Chart

Fields:

Legend → Payment
Values → Total Transactions

Average Transaction by Customer Type

Visual:

Column Chart

Fields:

X-axis → Customer Type
Y-axis → Average Transaction Value

Sales by City

Visual:

Column Chart

Fields:

X-axis → City
Y-axis → Total Sales

12. Power BI Project Format

The Power BI project uses:

.pbip

.Report

.SemanticModel

PBIR report definitions

TMDL semantic model definitions

The semantic model embeds the supplied 500 source rows in the TMDL partition, so the dashboard does not depend on a fixed external Excel file path.

13. Opening the Power BI Project

Install/open a current Power BI Desktop.

If Power BI Project/PBIP or enhanced report format is not enabled, enable the corresponding Preview feature.

Open:

Supermarket_Sales_Dashboard.pbip

Allow the model to load/refresh if prompted.

Save the project from Power BI Desktop once it opens.

14. Important PBIP Compatibility Note

PBIP/PBIR is a Power BI project format and can be affected by Power BI Desktop version and schema compatibility.

The project files follow the documented PBIP/PBIR/TMDL project structure, but PBIP files generated outside Power BI Desktop should be validated in the Power BI Desktop version being used.

If Power BI reports a schema, report-definition, semantic-model, or compatibility error, use the error message to identify the incompatible project definition.

15. Excel Report

The analysis output workbook contains calculated analysis results and supporting tables generated from the cleaned dataset.

The cleaned workbook contains the source data and data-quality checks.

16. Generated Charts

The Python analysis generates:

branch_sales.png
category_sales.png
customer_type_average.png
payment_methods.png
product_sales.png

These charts provide a static view of the same analytical areas represented in the Power BI dashboard.

17. Business Questions Answered

This project answers questions such as:

What are the total sales?

How many transactions occurred?

How many products were sold?

What is the average transaction value?

Which product generated the highest sales?

Which branch generated the highest sales?

Which category generated the highest sales?

Which payment method is used most frequently?

How do Member and Normal customers compare?

What is the average customer rating?

How do cities compare in total sales?

How can sales be filtered by branch, city, category, payment, customer type, and gender?

18. Portfolio Value

This project demonstrates practical skills in:

Data Cleaning

Exploratory Data Analysis

Python

Pandas

Matplotlib

Excel

Data Validation

KPI Development

DAX

Power BI

Data Visualization

Dashboard Design

Business Insights

Analytical Reporting

19. Recommended GitHub Contents

A GitHub repository can contain:

README.md
requirements.txt

Data/
    Supermarket_Sales_Cleaned_Final.xlsx

Python/
    supermarket_sales_analysis.py

Reports/
    Supermarket_Sales_Analysis.xlsx
    Charts/

PowerBI/
    Supermarket_Sales_Dashboard.pbip
    Supermarket_Sales_Dashboard.Report/
    Supermarket_Sales_Dashboard.SemanticModel/

Do not upload confidential or private data to a public repository.

20. Project Summary

The Supermarket Sales Analysis project takes raw/cleaned transaction data through a complete analytics workflow:

Dataset
   ↓
Data Cleaning
   ↓
Data Validation
   ↓
Python Analysis
   ↓
KPI Calculation
   ↓
Charts & Analysis Report
   ↓
Power BI Data Model
   ↓
DAX Measures
   ↓
Interactive Dashboard
   ↓
Business Insights

The final project is intended to demonstrate an end-to-end Data Analytics workflow from structured sales data to an interactive business intelligence dashboard.
