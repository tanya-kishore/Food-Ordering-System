import db
import order

def generate_bill():
    # bill_status=order.place_order()
    total_bill = sum(order.orders)
    return total_bill

