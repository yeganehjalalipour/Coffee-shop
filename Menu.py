# Menu.py

# اطلاعات محصولات و قیمت آنها
menu = {
    "coffee": 80000,
    "tea": 50000,
    "cake": 120000,
    "juice": 90000,
    "sandwich": 150000
}


# تابع نمایش منوی کافه
def show_menu():

    print("\n========== Coffee Menu ==========")

    for product, price in menu.items():

        print(product, ":", price, "Toman")

    print("=================================")
