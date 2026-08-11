 
sales = [120, 250, 90, 300, 175, 80, 260]

def filter_sales(sales):
    filtered_sales = []
    for sale in sales:
        if sale > 200:
            filtered_sales.append(sale)
    return filtered_sales

def total_sales(filtered_sales):
    total = 0
    for sale in filtered_sales:
        total += sale
    return total

def total_high_sales(filtered_sales):
    high_sales = 0
    for sale in filtered_sales:
        if high_sales < sale:
            high_sales = sale
    return high_sales


filtered_sales = filter_sales(sales)
total = total_sales(filtered_sales)
high_sales = total_high_sales(filtered_sales)
print(f"Sales above $200: {filtered_sales}")
print(f"Total of sales above $200: {total}")
print(f"Highest sale above $200: {high_sales}")