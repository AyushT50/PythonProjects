# Define the menu of restaurant
menu = {
    'Pizza' : 40, 
    'Pasta' : 50, 
    'Burger' : 60, 
    'Salad' : 70, 
    'Coffe' : 80

}

#Greet
print("Welcome to our restaurant. Here's the menu: ")
print("Pizza : Rs40 \nPasta : Rs50 \nBurger : Rs60 \nSalad : Rs70 \nCoffe : Rs80\n")

order_total = 0

item_1 = input("Enter the name of item you want to order : ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order!!")

else:
    print("Please choose item from the menu!")

another_order = input("Do your want to add another item? (Yes/No)")
if another_order == "yes" or another_order =="Yes":
    item_2 = input("Enter the name of second item:")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Your item {item_2} has been added to your order!!")

    else:
        print("Please choose item from the menu!")

print(f"The total amount of order is {order_total}")
print("Thanks for comming!")

