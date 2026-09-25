# ============================================================
# SUPERMARKET SALES ANALYSIS
# Data Analytics Project
# ============================================================

import os
import pandas as pd
import matplotlib.pyplot as plt

# ------------------------------------------------------------
# 1. FILE PATH
# ------------------------------------------------------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

INPUT_FILE = os.path.join(
    BASE_DIR,
    "Data",
    "Supermarket_Sales_Cleaned_Final.xlsx"
)

OUTPUT_DIR = os.path.join(BASE_DIR, "Reports")
CHART_DIR = os.path.join(OUTPUT_DIR, "Charts")

os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(CHART_DIR, exist_ok=True)


# ------------------------------------------------------------
# 2. LOAD DATA
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("SUPERMARKET SALES ANALYSIS")
print("=" * 60)

print("\nLoading dataset...")

df = pd.read_excel(
    INPUT_FILE,
    sheet_name="Sales_Data_Cleaned"
)

print("Dataset loaded successfully!")
print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")


# ------------------------------------------------------------
# 3. BASIC DATA INFORMATION
# ------------------------------------------------------------

print("\n" + "-" * 60)
print("DATASET INFORMATION")
print("-" * 60)

print("\nColumns:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nFirst 5 Records:")
print(df.head())


# ------------------------------------------------------------
# 4. DATA QUALITY CHECK
# ------------------------------------------------------------

print("\n" + "-" * 60)
print("DATA QUALITY CHECK")
print("-" * 60)

missing_values = df.isnull().sum().sum()
duplicate_rows = df.duplicated().sum()
duplicate_invoice_ids = df["Invoice ID"].duplicated().sum()

print(f"\nMissing Values: {missing_values}")
print(f"Duplicate Rows: {duplicate_rows}")
print(f"Duplicate Invoice IDs: {duplicate_invoice_ids}")


# ------------------------------------------------------------
# 5. SALES VALIDATION
# ------------------------------------------------------------

df["Calculated Sales"] = (
    df["Quantity"] * df["Unit Price"]
).round(2)

sales_errors = (
    df["Calculated Sales"].round(2)
    != df["Sales"].round(2)
).sum()

print(f"Sales Calculation Errors: {sales_errors}")

# Remove helper column after validation
df.drop(columns=["Calculated Sales"], inplace=True)


# ------------------------------------------------------------
# 6. KEY PERFORMANCE INDICATORS
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("KEY PERFORMANCE INDICATORS")
print("=" * 60)

total_sales = df["Sales"].sum()
total_transactions = len(df)
total_quantity = df["Quantity"].sum()
average_transaction = df["Sales"].mean()
average_rating = df["Rating"].mean()

print(f"\nTotal Sales: ₹{total_sales:,.2f}")
print(f"Total Transactions: {total_transactions:,}")
print(f"Total Quantity Sold: {total_quantity:,}")
print(f"Average Transaction: ₹{average_transaction:,.2f}")
print(f"Average Rating: {average_rating:.2f}/5")


# ------------------------------------------------------------
# 7. PRODUCT ANALYSIS
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("PRODUCT ANALYSIS")
print("=" * 60)

product_sales = (
    df.groupby("Product")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\nProduct-wise Sales:")
print(product_sales)

highest_product = product_sales.idxmax()
highest_product_sales = product_sales.max()

print(
    f"\nHighest Selling Product: "
    f"{highest_product} "
    f"(₹{highest_product_sales:,.2f})"
)


# ------------------------------------------------------------
# 8. BRANCH ANALYSIS
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("BRANCH ANALYSIS")
print("=" * 60)

branch_sales = (
    df.groupby(["Branch", "City"])["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\nBranch-wise Sales:")
print(branch_sales)

best_branch = branch_sales.idxmax()
best_branch_sales = branch_sales.max()

print(
    f"\nHighest Sales Branch: "
    f"{best_branch[0]} - {best_branch[1]} "
    f"(₹{best_branch_sales:,.2f})"
)


# ------------------------------------------------------------
# 9. CATEGORY ANALYSIS
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("CATEGORY ANALYSIS")
print("=" * 60)

category_sales = (
    df.groupby("Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\nCategory-wise Sales:")
print(category_sales)

highest_category = category_sales.idxmax()
highest_category_sales = category_sales.max()

print(
    f"\nHighest Selling Category: "
    f"{highest_category} "
    f"(₹{highest_category_sales:,.2f})"
)


# ------------------------------------------------------------
# 10. PAYMENT METHOD ANALYSIS
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("PAYMENT METHOD ANALYSIS")
print("=" * 60)

payment_transactions = (
    df["Payment"]
    .value_counts()
    .sort_values(ascending=False)
)

print("\nPayment Method Transactions:")
print(payment_transactions)

most_used_payment = payment_transactions.idxmax()
most_used_payment_count = payment_transactions.max()

print(
    f"\nMost Used Payment Method: "
    f"{most_used_payment} "
    f"({most_used_payment_count} transactions)"
)


# ------------------------------------------------------------
# 11. CUSTOMER TYPE ANALYSIS
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("CUSTOMER TYPE ANALYSIS")
print("=" * 60)

customer_analysis = (
    df.groupby("Customer Type")
    .agg(
        Transactions=("Invoice ID", "count"),
        Total_Sales=("Sales", "sum"),
        Average_Transaction=("Sales", "mean")
    )
    .sort_values("Total_Sales", ascending=False)
)

print("\nCustomer Type Analysis:")
print(customer_analysis)


# ------------------------------------------------------------
# 12. GENDER ANALYSIS
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("GENDER ANALYSIS")
print("=" * 60)

gender_analysis = (
    df.groupby("Gender")
    .agg(
        Transactions=("Invoice ID", "count"),
        Total_Sales=("Sales", "sum"),
        Average_Sales=("Sales", "mean")
    )
    .sort_values("Total_Sales", ascending=False)
)

print("\nGender Analysis:")
print(gender_analysis)


# ------------------------------------------------------------
# 13. RATING ANALYSIS
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("RATING ANALYSIS")
print("=" * 60)

rating_average = df["Rating"].mean()

rating_distribution = (
    df["Rating"]
    .round(0)
    .value_counts()
    .sort_index()
)

print(f"\nAverage Rating: {rating_average:.2f}/5")

print("\nRating Distribution:")
print(rating_distribution)


# ------------------------------------------------------------
# 14. CITY ANALYSIS
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("CITY ANALYSIS")
print("=" * 60)

city_sales = (
    df.groupby("City")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\nCity-wise Sales:")
print(city_sales)


# ------------------------------------------------------------
# 15. EXPORT ANALYSIS RESULTS
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("EXPORTING RESULTS")
print("=" * 60)

output_file = os.path.join(
    OUTPUT_DIR,
    "Supermarket_Sales_Analysis.xlsx"
)

with pd.ExcelWriter(output_file, engine="openpyxl") as writer:

    df.to_excel(
        writer,
        sheet_name="Cleaned_Data",
        index=False
    )

    product_sales.to_frame(
        "Total Sales"
    ).to_excel(
        writer,
        sheet_name="Product Analysis"
    )

    branch_sales.to_frame(
        "Total Sales"
    ).to_excel(
        writer,
        sheet_name="Branch Analysis"
    )

    category_sales.to_frame(
        "Total Sales"
    ).to_excel(
        writer,
        sheet_name="Category Analysis"
    )

    payment_transactions.to_frame(
        "Transactions"
    ).to_excel(
        writer,
        sheet_name="Payment Analysis"
    )

    customer_analysis.to_excel(
        writer,
        sheet_name="Customer Analysis"
    )

    gender_analysis.to_excel(
        writer,
        sheet_name="Gender Analysis"
    )

    city_sales.to_frame(
        "Total Sales"
    ).to_excel(
        writer,
        sheet_name="City Analysis"
    )


# ------------------------------------------------------------
# 16. CHART 1 - PRODUCT SALES
# ------------------------------------------------------------

plt.figure(figsize=(12, 7))

product_sales.sort_values().plot(
    kind="barh"
)

plt.title("Product-wise Sales")
plt.xlabel("Sales (₹)")
plt.ylabel("Product")
plt.tight_layout()

plt.savefig(
    os.path.join(CHART_DIR, "product_sales.png"),
    dpi=300
)

plt.close()


# ------------------------------------------------------------
# 17. CHART 2 - BRANCH SALES
# ------------------------------------------------------------

plt.figure(figsize=(9, 6))

branch_chart = df.groupby("Branch")["Sales"].sum()

branch_chart.plot(
    kind="bar"
)

plt.title("Branch-wise Sales")
plt.xlabel("Branch")
plt.ylabel("Sales (₹)")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig(
    os.path.join(CHART_DIR, "branch_sales.png"),
    dpi=300
)

plt.close()


# ------------------------------------------------------------
# 18. CHART 3 - CATEGORY SALES
# ------------------------------------------------------------

plt.figure(figsize=(9, 6))

category_sales.plot(
    kind="bar"
)

plt.title("Category-wise Sales")
plt.xlabel("Category")
plt.ylabel("Sales (₹)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

plt.savefig(
    os.path.join(CHART_DIR, "category_sales.png"),
    dpi=300
)

plt.close()


# ------------------------------------------------------------
# 19. CHART 4 - PAYMENT METHODS
# ------------------------------------------------------------

plt.figure(figsize=(8, 6))

payment_transactions.plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title("Payment Method Distribution")
plt.ylabel("")
plt.tight_layout()

plt.savefig(
    os.path.join(CHART_DIR, "payment_methods.png"),
    dpi=300
)

plt.close()


# ------------------------------------------------------------
# 20. CHART 5 - CUSTOMER TYPE
# ------------------------------------------------------------

plt.figure(figsize=(8, 6))

customer_chart = df.groupby(
    "Customer Type"
)["Sales"].mean()

customer_chart.plot(
    kind="bar"
)

plt.title("Average Transaction by Customer Type")
plt.xlabel("Customer Type")
plt.ylabel("Average Transaction (₹)")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig(
    os.path.join(CHART_DIR, "customer_type_average.png"),
    dpi=300
)

plt.close()


# ------------------------------------------------------------
# 21. FINAL BUSINESS INSIGHTS
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("BUSINESS INSIGHTS")
print("=" * 60)

print(f"""
1. Highest-selling product:
   {highest_product} - ₹{highest_product_sales:,.2f}

2. Highest-performing branch:
   {best_branch[0]} ({best_branch[1]}) - ₹{best_branch_sales:,.2f}

3. Highest-selling category:
   {highest_category} - ₹{highest_category_sales:,.2f}

4. Most-used payment method:
   {most_used_payment} - {most_used_payment_count} transactions

5. Average customer rating:
   {average_rating:.2f}/5

6. Total supermarket sales:
   ₹{total_sales:,.2f}

7. Total transactions:
   {total_transactions:,}

8. Total quantity sold:
   {total_quantity:,}
""")


# ------------------------------------------------------------
# 22. COMPLETE
# ------------------------------------------------------------

print("=" * 60)
print("ANALYSIS COMPLETED SUCCESSFULLY!")
print("=" * 60)

print(f"\nExcel report created:")
print(output_file)

print(f"\nCharts created in:")
print(CHART_DIR)