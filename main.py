price = {"Soap": 90.00, "washing powder": 150.00, 
"Drinking water": 60.00, "Toothbrush": 30.00, "Toothpaste": 45.00,"Baby powder": 100.00,
"Noodle" : 10.00,"Rice": 450.00,"Vegetable oil" :50.00,"Shampoo" : 290.00 }
shopping_basket = {}
costumer_name = input("costumer Name : ")

print ("Welcome to the ponmak store!\n1. Soap : 90.00 \n2.washing powder : 150.00\n3. Drinking water : 60.00\n4. Toothbrush : 30.00\n5.Toothpaste: 45.00\n6.Baby powder: 100.00\n7.Noodle : 10.00\n8.Rice: 450.00\n9.Vegetable oil :50.00\n10.Shampoo : 290.00 ")

buy_another_flag = 1
total_cost, total = 0, 0

while buy_another_flag != 0:
        option = int(input("What would you like to purchase?: "))
    
        if option == 1:
            qnty = int(input("Enter the quantity: "))
            total = qnty * 90.00
            print("The price is: " + str(total))
        elif option == 2:
            qnty = int(input("Enter the quantity: "))
            total = qnty * 150.00
            print("The price is: " + str(total))
        elif option == 3:
            qnty = int(input("Enter the quantity: "))
            total = qnty * 60.00
            print("The price is: " + str(total))
        elif option == 4:
            qnty = int(input("Enter the quantity: "))
            total = qnty * 30.00
            print("The price is: " + str(total))
        elif option == 5:
            qnty = int(input("Enter the quantity: "))
            total = qnty * 45.00
            print("The price is: " + str(total))
        elif option == 6:
            qnty = int(input("Enter the quantity: "))
            total = qnty * 100.00
            print("The price is: " + str(total))
        elif option == 7:
            qnty = int(input("Enter the quantity: "))
            total = qnty * 10.00
            print("The price is: " + str(total))
        elif option == 8:
            qnty = int(input("Enter the quantity: "))
            total = qnty * 450.00
            print("The price is: " + str(total))
        elif option == 9:
            qnty = int(input("Enter the quantity: "))
            total = qnty * 50.00
            print("The price is: " + str(total))
        elif option == 10:
            qnty = int(input("Enter the quantity: "))
            total = qnty * 290.00
            print("The price is: " + str(total))

        total_cost += total

        buy_another_flag = int(input("Would you like another item? enter Yes (1) or No (0):"))
print("The total price of your basket is: ", total_cost)