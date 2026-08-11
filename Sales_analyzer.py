sales = [120, 250, 90, 300, 175, 80, 260]

def analyze_sales(sales):
    highest_sale = sales[0]
    lowest_sale = sales[0]
    total_sales = 0
    above_200 = 0

    for sale in sales:
        total_sales += sale

        if sale > highest_sale:
            highest_sale = sale

        if sale < lowest_sale:
            lowest_sale = sale
        if sale > 200:
            above_200 += 1
    average_sales = total_sales / len(sales)

    return highest_sale, lowest_sale, average_sales, above_200
highest_sale, lowest_sale, average_sales, above_200 = analyze_sales(sales)
print(f"Highest sale: {highest_sale}") 
print(f"Lowest sale: {lowest_sale}")
print(f"Average sale: {average_sales:.2f}")
print(f"Number of sales above $200: {above_200}")
