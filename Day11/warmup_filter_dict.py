orders = [
    {"order_id": 1, "customer_name": "Bob", "total_amount": 250.00, "status": "completed"},
    {"order_id": 2, "customer_name": "Alice", "total_amount": 150.00, "status": "pending"},
    {"order_id": 3, "customer_name": "Charlie", "total_amount": 350.00, "status": "completed"},
    {"order_id": 4, "customer_name": "Davis", "total_amount": 100.00, "status": "shipped"},
]

dollars = "{:2f}"

# total_amount >= 200 and status == "completed"
print(f"Amounts greater than 200 and completed:")
print(f"ID\t\tCustomer\tAmount\t\tStatus")
      
for order in orders:
    if order['total_amount'] >= 200 and order['status'] == 'completed':
        print(f"{order['order_id']}\t\t{order['customer_name']}\t\t$ {format(order['total_amount'], ",.2f")}\t{order['status'].capitalize()}")


print(f"\n\nA second attempt using filter:\n\n")


results = list(filter(lambda o: o['total_amount'] >= 200 and o['status'] == 'completed', orders ))

print(f"Amounts greater than 200 and completed:")
print(f"ID\t\tCustomer\tAmount\t\tStatus")

for order in results:
    print(f"{order['order_id']}\t\t{order['customer_name']}\t\t$ {format(order['total_amount'], ",.2f")}\t{order['status'].capitalize()}")

#print(results)
