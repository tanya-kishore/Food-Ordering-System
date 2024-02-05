import sqlite3
conn=sqlite3.connect('data.db')
cursor=conn.cursor()


q='''
CREATE TABLE IF NOT EXISTS user_new(username TEXT PRIMARY KEY,password TEXT,mobile_no INTEGER,address TEXT)
'''
cursor.execute(q)
conn.commit()


o='''
CREATE TABLE IF NOT EXISTS cart(order_id INTEGER PRIMARY KEY AUTOINCREMENT,dish_id INTEGER,dish_type TEXT,dish_price INTEGER,quantity INTEGER)
'''

cursor.execute(o)
conn.commit()


def create_connection():
    conn = sqlite3.connect('data.db')
    return conn

def close_connection(conn):
    conn.close()

def insert_data(username,password,mobile,address):
    q1='''
    INSERT INTO user VALUES(?,?,?,?)
    '''
    cursor.execute(q1,(username,password,mobile,address))
    conn.commit()
    


def check_user(username):
    cursor.execute(''' SELECT * FROM user WHERE username=?''',(username,))
    a = cursor.fetchall()
    if (len(a)==0):
        return None
    else:
        return a
    

def update_password(username,new_password):
    try:
        cursor.execute('''UPDATE user SET password = ? WHERE username = ?''', (new_password, username))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error updating password: {e}")
        conn.rollback()

def menuTable():
    
    a11='''
    CREATE TABLE IF NOT EXISTS Food_menu(dish_id INTEGER PRIMARY KEY,dish TEXT,dish_type TEXT,dish_price INTEGER)
    '''

    cursor.execute(a11)
    conn.commit()


def pizza_menu():
    a1='''
    INSERT INTO Food_menu VALUES(?,?,?,?)
    '''
    data=[(1,'Pizza', 'Chicken Fazita Pizza', 200),(2,'Pizza', 'Chicken Bar BQ Pizza', 280),(3,'Pizza', 'Creamy Max Pizza', 180)] 
    cursor.executemany(a1,data)
    conn.commit()

def burger_menu():
    a2='''
    INSERT INTO Food_menu VALUES(?,?,?,?)
    '''
    data=[(4,'Burger','Zinger Burger',180),(5,'Burger','Chicken Burger',150),(6,'Burger','Mutton Burger',200)]

    cursor.executemany(a2,data)
    conn.commit()

def sandwich_menu():
    a3='''
    INSERT INTO Food_menu VALUES(?,?,?,?)
    '''
    data=[(7,'Sandwich','Club Sandwich',150),(8,'Sandwich','Chicken Crispy Sandwich',180),(9,'Sandwich','Extreme veg sandwich',100)]
    cursor.executemany(a3,data)
    conn.commit()


def roll_menu():
    a4='''
    INSERT INTO Food_menu VALUES(?,?,?,?)
    '''
    data=[(10,'Roll','Chicken Chatni Roll',150),(11,'Roll','Chicken Mayo Roll',130),(12,'Roll','Veg Roll With Fries',100)]
    cursor.executemany(a4,data)
    conn.commit()


def biryani_menu():
    a5='''
    INSERT INTO Food_menu VALUES(?,?,?,?)
    '''
    data=[(13,'Biryani','Chicken Biryani',160),(14,'Biryani','Mutton Biryani',200),(15,'Biryani','Veg Biryani',140)]
    cursor.executemany(a5,data)
    conn.commit()



def place_order(dish_id, dish_type, dish_price,quantity):
    try:
        cursor.execute('''INSERT INTO cart (dish_id, dish_type, dish_price,quantity) VALUES (?,?,?, ?)''', (dish_id, dish_type, dish_price,quantity))
        conn.commit()
        data_one=cursor.fetchall()
        return data_one
    except sqlite3.Error as e:
        print(f"Error placing order: {e}")
        conn.rollback()
        return None

