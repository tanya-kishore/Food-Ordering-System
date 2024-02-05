import db
global_variable_to_export = None 
quantity_= None
orders = [] 
def show_pizza_menu():
    global global_variable_to_export
    global quantity_
    pizza_data=db.menuTable()
    print("                                                           ")
    print("|   PRESS 1  ", 'Chicken Fazita Pizza', "Rs.200", "      |")
    print("|   PRESS 2  ", 'Chicken Bar BQ Pizza', "Rs.280", "      |")
    print("|   PRESS 3  ", 'Creamy Max Pizza', "Rs.180", "          |")
    print("                                                           ")
    pchoice=int(input("Please enter what would you like to have: "))
    quantity=int(input("Please enter the quantity: "))
    global_variable_to_export = pchoice
    quantity_=quantity
    place_order()


def show_burger_menu():
    global global_variable_to_export
    global quantity_
    burger_data=db.menuTable()
    print("                                                          ")
    print("|   PRESS 4  ", 'Zinger Burger', " Rs.180", "            |")
    print("|   PRESS 5  ", 'Chicken Burger', " Rs.150", "           |")
    print("|   PRESS 6  ", 'Mutton Burger', " Rs.200", "            |")
    print("                                                           ")
    pchoice=int(input("Please enter what would you like to have: "))
    quantity=int(input("Please enter the quantity: "))
    global_variable_to_export = pchoice
    quantity_=quantity
    place_order()



def show_sandwich_menu():
    global global_variable_to_export
    global quantity_

    sandwich_data=db.menuTable()
    print("                                                           ")
    print("|   PRESS 7  ", 'Club Sandwich', " Rs.150", "             |")
    print("|   PRESS 8  ", 'Chicken Crispy Sandwich', " Rs.180", "   |")
    print("|   PRESS 9  ", 'Extreme veg sandwich', " Rs.100", "      |")
    print("                                                           ")
    pchoice=int(input("Please enter what would you like to have: "))
    quantity=int(input("Please enter the quantity: "))
    global_variable_to_export = pchoice
    quantity_=quantity
    place_order()

 

def show_roll_menu():
    global global_variable_to_export
    global quantity_
    roll_data=db.menuTable()
    print("                                                           ")
    print("|   PRESS 10  ", 'Chicken Chatni Roll', " Rs.150", "       |")
    print("|   PRESS 11 ", 'Chicken Mayo Roll', " Rs.130", "          |")
    print("|   PRESS 12 ", 'Veg Roll With Fries', " Rs.100", "        |")
    print("                                                           ")
    pchoice=int(input("Please enter what would you like to have: "))
    quantity=int(input("Please enter the quantity: "))
    global_variable_to_export = pchoice
    quantity_=quantity
    place_order()



def show_biryani_menu():
    global global_variable_to_export
    global quantity_
    biryani_data=db.menuTable()
    print("                                                            ")
    print("|   PRESS 13  ", 'Chicken Biryani', " Rs.160", "            |")
    print("|   PRESS 14  ", 'Mutton Biryani', " Rs.200", "             |")
    print("|   PRESS 15  ", 'Veg Biryani', " Rs.140", "                |")
    print("                                                           ")
    pchoice=int(input("Please enter what would you like to have: "))
    quantity=int(input("Please enter the quantity: "))
    global_variable_to_export = pchoice
    quantity_=quantity
    place_order()


def place_order():
    global global_variable_to_export
    global quantity_
    global orders

    if global_variable_to_export == 1:
        dish_id, dish_type, dish_price= 1, 'Chicken Fazita Pizza', 200
        db.place_order(dish_id, dish_type, dish_price,quantity_)
        order_amount = dish_price * quantity_
        orders.append(order_amount)
        return order_amount
        
    
    elif global_variable_to_export == 2:
        dish_id, dish_type, dish_price = 2, 'Chicken Bar BQ Pizza', 280
        db.place_order(dish_id, dish_type, dish_price,quantity_)
        order_amount = dish_price * quantity_
        orders.append(order_amount)
        return order_amount
    
    elif global_variable_to_export == 3:
        dish_id, dish_type, dish_price = 3, 'Creamy Max Pizza', 180
        db.place_order(dish_id, dish_type, dish_price,quantity_)
        order_amount = dish_price * quantity_
        orders.append(order_amount)
        return order_amount

    elif global_variable_to_export == 4:
        dish_id, dish_type, dish_price = 4, 'Zinger Burger', 180
        db.place_order(dish_id, dish_type, dish_price, quantity_)
        order_amount = dish_price * quantity_
        orders.append(order_amount)
        return order_amount
    
    elif global_variable_to_export == 5:
        dish_id, dish_type, dish_price = 5, 'Chicken Burger', 150
        db.place_order(dish_id, dish_type, dish_price, quantity_)
        order_amount = dish_price * quantity_
        orders.append(order_amount)
        return order_amount
    
    elif global_variable_to_export == 6:
        dish_id, dish_type, dish_price = 6, 'Mutton Burger', 200
        db.place_order(dish_id, dish_type, dish_price, quantity_)
        order_amount = dish_price * quantity_
        orders.append(order_amount)
        return order_amount
    

    elif global_variable_to_export == 7:
        dish_id, dish_type, dish_price = 7, 'Club Sandwich', 150
        db.place_order(dish_id, dish_type, dish_price, quantity_)
        order_amount = dish_price * quantity_
        orders.append(order_amount)
        return order_amount
    
    elif global_variable_to_export == 8:
        dish_id, dish_type, dish_price = 8, 'Chicken Crispy Sandwich', 180
        db.place_order(dish_id, dish_type, dish_price, quantity_)
        order_amount = dish_price * quantity_
        orders.append(order_amount)
        return order_amount
    
    elif global_variable_to_export == 9:
        dish_id, dish_type, dish_price = 9, 'Extreme veg sandwich', 100
        db.place_order(dish_id, dish_type, dish_price, quantity_)
        order_amount = dish_price * quantity_
        orders.append(order_amount)
        return order_amount
    

    elif global_variable_to_export == 10:
        dish_id, dish_type, dish_price = 10, 'Chicken Chatni Roll', 150
        db.place_order(dish_id, dish_type, dish_price, quantity_)
        order_amount = dish_price * quantity_
        orders.append(order_amount)
        return order_amount
    
    elif global_variable_to_export == 11:
        dish_id, dish_type, dish_price = 11, 'Chicken Mayo Roll', 130
        db.place_order(dish_id, dish_type, dish_price, quantity_)
        order_amount = dish_price * quantity_
        orders.append(order_amount)
        return order_amount
    
    elif global_variable_to_export == 12:
        dish_id, dish_type, dish_price = 12, 'Veg Roll With Fries', 100
        db.place_order(dish_id, dish_type, dish_price, quantity_)
        order_amount = dish_price * quantity_
        orders.append(order_amount)
        return order_amount

    
    elif global_variable_to_export == 13:
        dish_id, dish_type, dish_price = 13, 'Chicken Biryani', 160
        db.place_order(dish_id, dish_type, dish_price, quantity_)
        order_amount = dish_price * quantity_
        orders.append(order_amount)
        return order_amount
    
    elif global_variable_to_export == 14:
        dish_id, dish_type, dish_price = 14, 'Mutton Biryani', 200
        db.place_order(dish_id, dish_type, dish_price, quantity_)
        order_amount = dish_price * quantity_
        orders.append(order_amount)
        return order_amount
    
    elif global_variable_to_export == 15:
        dish_id, dish_type, dish_price = 15, 'Veg Biryani', 140
        db.place_order(dish_id, dish_type, dish_price, quantity_)
        order_amount = dish_price * quantity_
        orders.append(order_amount)
        return order_amount
    
    else:
        print("Invalid choice. Please choose a valid option.")

