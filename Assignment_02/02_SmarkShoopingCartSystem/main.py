#Creating a user-defined function
def shooping_cart():
    prices = []
    products = []

    #Entering the five product prices
    for i in range(5):
        prod = input("Enter the name of the product: ")
        price = float(input("Enter the product price: "))
        prices.append(price)
        products.append(prod)

    #Using loop to calculate total bill  
    total = 0
    for price in prices:
        total+=price

    #Using the conditional statement to apply discount
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

   #Displaying the product list, product prices, discount, and final payable amount
    print("\n----- Shopping Cart -----")
    print("Product Lists: ", products)
    print("Product prices: ",prices)
    print("Total amount = ",total)
    print("Discounted % = ",discount)
    print("Discounted Amount = ",dis_amt)
    print("Final Payable Amount= ",final_pay)
    
#Calling the function
shooping_cart()