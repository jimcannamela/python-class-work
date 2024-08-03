# Given a list of dictionaries containing sales data
# 1. Calculate the total sales for each product (units_sold * price_per_unit)
# 2. Determine the product with the highest sales (units sold)
# 3. Determine the product with the lowest sales (units sold)
# 4. Calculate the total sales for all products (units sold)
# 5. Print a summary report with the total sales for each product, the product with the highest sales, the total revenue, and the average sales per product

sales_data = [
    {"product_name": "Product A", "units_sold": 10, "price_per_unit": 15.0},
    {"product_name": "Product B", "units_sold": 5, "price_per_unit": 30.0},
    {"product_name": "Product C", "units_sold": 8, "price_per_unit": 12.5},
    {"product_name": "Product D", "units_sold": 15, "price_per_unit": 10.0},
]

sale_totals=[]
unit_totals=0

print("Sales report for Shahzad's widgets - July 2024\n")
print("Product\t\tUnits Sold\tPrice\t\tTotal")

for x in range(len(sales_data)):
    sales_per_product=sales_data[x].get("units_sold")*sales_data[x].get("price_per_unit")
    sale_totals.append(sales_per_product)
    units=sales_data[x].get("units_sold")
    unit_totals+=units
    print(f"{sales_data[x].get("product_name")}\t{units}\t\t{sales_data[x].get("price_per_unit")}\t\t{sales_per_product}")

print(f"Total Sales\t{unit_totals}\t\t\t\t{sum(sale_totals)}\n")
# from Joe's code
print(f"Highest Sales - {max(sales_data, key=lambda x: x['units_sold'])['product_name']}")
print(f"Lowest Sales  - {min(sales_data, key=lambda x: x['units_sold'])['product_name']}")

#### Joe Carroll's code

sales_data = [
    {"product_name": "Product A", "units_sold": 10, "price_per_unit": 15.0},
    {"product_name": "Product B", "units_sold": 5, "price_per_unit": 30.0},
    {"product_name": "Product C", "units_sold": 8, "price_per_unit": 12.5},
    {"product_name": "Product D", "units_sold": 15, "price_per_unit": 10.0},
]

for x in sales_data:
    print(f"Total sales for {x['product_name']} was ${x['units_sold'] * x['price_per_unit']}")
    
print(f"\n{max(sales_data, key=lambda x: x['units_sold'])['product_name']} had the highest sales")
print(f"\n{min(sales_data, key=lambda x: x['units_sold'])['product_name']} has the lowest sales")
print(f"\nThe total units sold for all products was {sum(item['units_sold'] for item in sales_data)}")

#### Madhavi's Code

sales_data = [
    {"product_name": "Product A", "units_sold": 10, "price_per_unit": 15.0},
    {"product_name": "Product B", "units_sold": 5, "price_per_unit": 30.0},
    {"product_name": "Product C", "units_sold": 8, "price_per_unit": 12.5},
    {"product_name": "Product D", "units_sold": 15, "price_per_unit": 10.0},
]
# Given is a list of dictionaries containing sales data
# 1. Calculate the total sales foe each product (units_sold * price_per_unit)#
# 2. Determine the product with the highest sales (units sold)
# 3. Determine the product with the lowest sales (units sold)
# 4. Calculate the total sales for all products (units sold)
# 5. Print a summary report with the total sales for each product, the product with the highest sales, the total revenue

for product in sales_data:
    total = product["units_sold"] * product["price_per_unit"]
    print(product["product_name"], total)

totalofallprod = sum(product["units_sold"] * product["price_per_unit"] for product in sales_data)
print()
print("Total sales for all products (units sold)" , totalofallprod)

def units_sold(sales_data):
    return sales_data["units_sold"]

highest = max(sales_data, key=units_sold) # produces a dictionary  {'product_name': 'Product D', 'units_sold': 15, 'price_per_unit': 10.0}
lowest = min(sales_data, key=units_sold)  # produces a dictionary  {'product_name': 'Product B', 'units_sold': 5, 'price_per_unit': 30.0}
print()

print("highest sales (units sold)" , highest)
print("Lowest sales (units sold)", lowest)

# Sam's code

# sales_data = [
#     {"product_name": "Product A", "units_sold": 10, "price_per_unit": 15.0},
#     {"product_name": "Product B", "units_sold": 5, "price_per_unit": 30.0},
#     {"product_name": "Product C", "units_sold": 8, "price_per_unit": 12.5},
#     {"product_name": "Product D", "units_sold": 15, "price_per_unit": 10.0},
# ]
# # Given is a list of dictionaries containing sales data
# # 1. Calculate the total sales foe each product (units_sold * price_per_unit)#
# # 2. Determine the product with the highest sales (units sold)
# # 3. Determine the product with the lowest sales (units sold)
# # 4. Calculate the total sales for all products (units sold)
# # 5. Print a summary report with the total sales for each product, the product with the highest sales, the total revenue

#Design

# Read list of dictionaries using for loop and do the operations as needed with in the loop and do the summary after.

#input data

sales_data = [
    {"product_name": "Product A", "units_sold": 10, "price_per_unit": 15.0},
    {"product_name": "Product B", "units_sold": 5, "price_per_unit": 30.0},
    {"product_name": "Product C", "units_sold": 8, "price_per_unit": 12.5},
    {"product_name": "Product D", "units_sold": 15, "price_per_unit": 10.0},
]

# 1. Calculate the total sales foe each product (units_sold * price_per_unit)#
# added a new key to the dictionary
for product in sales_data:
    product['total_sales'] = product['units_sold'] * product['price_per_unit']
    print(product)


# 2. Determine the product with the highest sales (units sold)
max_sales_product = max(sales_data, key=lambda x: x['units_sold'])
print("max dictionary", max_sales_product)

# 3. Determine the product with the lowest sales (units sold)
min_sales_product = min(sales_data, key=lambda x: x['units_sold'])
print("min dictionary", min_sales_product)

# 4. Calculate the total sales for all products (units sold)
total_revenue = sum(product['total_sales'] for product in sales_data)

# # 5. Print a summary report with the total sales for each product, the product with the highest sales, the total revenue

print("========================================")
print("Summary Report for the warmup excercise output ")
print("========================================")

for product in sales_data:
    print(f"Product: {product['product_name']}, Total Sales: ${product['total_sales']}")

print(f"\nProduct with highest sales: {max_sales_product['product_name']} ({max_sales_product['units_sold']} units)")
print(f"Product with lowest sales: {min_sales_product['product_name']} ({min_sales_product['units_sold']} units)")
print(f"\nTotal Revenue: ${total_revenue}")
