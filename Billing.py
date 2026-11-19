# Billing.py

# وارد کردن لیست سفارش ها
from Order import orders


# تابع محاسبه مبلغ کل
def calculate_total():

    total = 0

    for order in orders:

        price = order["price"]
        quantity = order["quantity"]

        total = total + (price * quantity)

    return total


# تابع محاسبه تخفیف
def calculate_discount(total):

    if total > 1000000:

        discount = total * 0.10

    else:

        discount = 0

    return discount


# تابع چاپ فاکتور
def print_invoice():

    if len(orders) == 0:

        print("No orders to print!")

    else:

        print("\n========== Coffee Shop Invoice ==========")

        for order in orders:

            amount = order["price"] * order["quantity"]

            print("Product:", order["product"])
            print("Quantity:", order["quantity"])
            print("Amount:", amount)

            print("----------------------------------------")

        # محاسبه مبلغ کل
        total = calculate_total()

        # محاسبه میزان تخفیف
        discount = calculate_discount(total)

        # محاسبه مبلغ نهایی
        final_price = total - discount

        print("Total Price:", total, "Toman")
        print("Discount:", discount, "Toman")
        print("Final Price:", final_price, "Toman")

        print("========================================")
