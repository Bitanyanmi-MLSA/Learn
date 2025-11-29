#!/usr/bin/env python3
import csv
from datetime import date, timedelta

products = [
    ("Widget A","Widgets",19.99),
    ("Widget B","Widgets",24.50),
    ("Gadget C","Gadgets",9.99),
    ("Gadget D","Gadgets",14.75),
    ("Thingamajig E","Thingamajigs",49.99),
    ("Doohickey F","Accessories",5.50),
    ("Accessory G","Accessories",3.25),
    ("Tool H","Tools",29.95),
]
payment_methods = ["Credit Card","PayPal","Cash","Wire"]
regions = ["North","South","East","West"]

start = date(2025, 1, 1)
rows = []

for i in range(1, 101):
    idx = (i - 1) % len(products)
    product, category, unit_price = products[idx]
    quantity = ((i - 1) % 5) + 1
    discount = ((i - 1) % 4) * 1.5
    total_price = round(quantity * unit_price - discount, 2)
    sale_date = (start + timedelta(days=i - 1)).isoformat()
    customer_id = f"CUST{1000 + i}"
    payment = payment_methods[(i - 1) % len(payment_methods)]
    region = regions[(i - 1) % len(regions)]
    rows.append({
        "sale_id": i,
        "date": sale_date,
        "product": product,
        "category": category,
        "quantity": quantity,
        "unit_price": f"{unit_price:.2f}",
        "discount": f"{discount:.2f}",
        "total_price": f"{total_price:.2f}",
        "customer_id": customer_id,
        "region": region,
        "payment_method": payment,
    })

out_path = "sales_data.csv"
with open(out_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["sale_id","date","product","category","quantity","unit_price","discount","total_price","customer_id","region","payment_method"])
    writer.writeheader()
    for r in rows:
        writer.writerow(r)

print(f"Wrote {len(rows)} rows to {out_path}")
