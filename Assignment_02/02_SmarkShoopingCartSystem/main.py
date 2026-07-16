# Create a user-defined function called shopping_cart() that:

# 1. Allows the user to enter 5 product prices.
# 2. Stores the prices in a list.
# 3. Uses a loop to calculate the total bill.
# 4. Applies discounts using conditional statements:
#     * Total ≥ 5000 → 15% discount
#     * Total ≥ 3000 → 10% discount
#     * Total ≥ 1000 → 5% discount
#     * Otherwise → No discount
# 5. Displays:
#     * Product list
#     * Total amount
#     * Discount amount
#     * Final payable amount

def shooping_cart():
    prices = []
    products = []
    for i in range(5):
        prod = input("Enter the name of the product: ")
        price = float(input("Enter the product price: "))
        prices.append(price)
        products.append(prod)

        
    total = 0
    for price in prices:
        total+=price

    if (total >= 5000):
        discount = "15%"
        dis_amt = (0.15*total)
        final_pay = total - dis_amt
    elif(total>=3000):
        discount = "10%"
        dis_amt = (0.1*total)
        final_pay = total - dis_amt
    elif(total>=1000):
        discount = "5%"
        dis_amt = (0.05*total)
        final_pay = total - dis_amt
    else:
        discount = "No discount"
        dis_amt = 0
        final_pay = total

    print("\n----- Shopping Cart -----")
    print("Product Lists: ", products)
    print("Product prices: ",prices)
    print("Total amount = ",total)
    print("Discounted % = ",discount)
    print("Discounted Amount = ",dis_amt)
    print("Final Payable Amount= ",final_pay)
    

shooping_cart()