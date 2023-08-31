from enum import Enum
import os
import json
import logging

logging.basicConfig(
    level=logging.DEBUG, 
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)

logger = logging.getLogger(__name__)

file_handler = logging.FileHandler('supermarket.log')
file_handler.setLevel(logging.DEBUG)  # Set the desired log level for the handler
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

class Actions(Enum):
    ADD_PRODUCT = 1
    PRINT_PRODUCTS = 2
    ADD_TO_CART = 3
    PRINT_CART = 4
    BUY_CART = 5
    EXIT = 0

product_list = []
cart = []

class Product:
    def __init__(self, product_name, product_price, product_inv) -> None:
        self.product_name = product_name
        self.product_price = product_price
        self.product_inv = product_inv

def menu(is_manager, filename):
    load_cart(filename)
    while True:
        for action in Actions:
            if is_manager:
                if action in [Actions.ADD_PRODUCT, Actions.PRINT_PRODUCTS, Actions.EXIT]:
                    print(f'{action.name}-{action.value}')
            else:
                if action in [Actions.PRINT_PRODUCTS, Actions.ADD_TO_CART, Actions.PRINT_CART, Actions.BUY_CART, Actions.EXIT]:
                    print(f'{action.name}-{action.value}')
        user_selection = Actions(int(input("\n Select next action: ")))
        if user_selection == Actions.ADD_PRODUCT and is_manager:
            add_product()
        elif user_selection == Actions.PRINT_PRODUCTS:
            print_products()
        elif user_selection == Actions.ADD_TO_CART and not is_manager:
            add_to_cart()
        elif user_selection == Actions.PRINT_CART and not is_manager:
            print_cart()
        elif user_selection == Actions.BUY_CART and not is_manager:
            buy_cart()
        elif user_selection == Actions.EXIT and is_manager:
            save(filename)
            break
        elif user_selection == Actions.EXIT:
            break

def clean_screen():
    os.system('cls')

def load_cart(filename):
    try:
        with open(filename, 'r') as openfile:
            json_object = json.load(openfile)
            product_list.extend(json_object["product_list"])
            cart.extend(json_object["cart"])
        print("Loaded cart. \n")
    except FileNotFoundError:
        print("No previous cart found. \n")

def add_product():
    clean_screen()
    prod_name = input("product name? ")
    prod_price = float(input("product price? "))
    prod_inv = int(input("product count? "))
    product = {"product": prod_name, "price": prod_price, "inventory": prod_inv}
    product_list.append(product)
    logger.warning("Product added to store: %s", prod_name) 
    print("Product added! \n")

def print_products():
    clean_screen()
    for product in product_list:
        print(product)
        print("\n")

def add_to_cart():
    clean_screen()
    print("Choose a product to add to your cart \n")
    print_products()
    product_name = input("Enter the name of the product to add to cart: ")
    product = next((p for p in product_list if p["product"] == product_name), None)
    if product:
        cart.append(product)
        print("Product added to cart!\n")
        logger.info("Product added to cart: %s", product_name) 
    else:
        print("Product not found in the list.\n")
        logger.error("Product not found in the list %s")

def print_cart():
    clean_screen()
    if not cart:
        print("Your cart is empty.\n")
        logger.error("Cart is empty %s")
    else:
        print("Cart content:\n")
        for item in cart:
            print(item)
            print("\n")
        total_cost = sum(item["price"] for item in cart)
        print("Total price: ",total_cost,"\n")

def buy_cart():
    clean_screen()
    total_cost = sum(item["price"] for item in cart)
    print("Total cart cost:", total_cost)
    print("Your order is on the way!\n")
    cart.clear()
    logger.warning("New order: %s", total_cost) 


def save(filename):
    logger.info("saved data: %s")
    data = {
        "product_list": product_list,
        "cart": cart
    }
    with open(filename, "w") as outfile:
        json.dump(data, outfile)
     

if __name__ == "__main__":
    clean_screen()
    is_manager = input("Are you a manager? (yes/no): ").lower() == "yes"
    filename = "supermarket.json"  
    menu(is_manager, filename)
    save(filename)