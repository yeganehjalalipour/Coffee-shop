# Order.py

# وارد کردن اطلاعات منوی کافه
from Menu import menu


# لیست ذخیره سفارش ها
orders = []


# تابع ثبت سفارش
def add_order():

    product = input("Enter product name: ").lower()

    # بررسی وجود محصول در منو
    if product in menu:

        try:
            quantity = int(input("Enter quantity: "))

            if quantity > 0:

                order = {
                    "product": product,
                    "price": menu[product],
                    "quantity": quantity
                }

                orders.append(order)

                print("Order added successfully!")

            else:
                print("Quantity must be greater than zero!")

        except ValueError:
            print("Please enter a valid number!")

    else:
        print("Product not found in menu!")


# تابع نمایش سفارش ها
def show_orders():

    if len(orders) == 0:

        print("No orders registered!")

    else:

        print("\n========== Customer Orders ==========")

        for order in orders:

            print("Product:", order["product"])
            print("Price:", order["price"])
            print("Quantity:", order["quantity"])

            print("-----------------------------------")
