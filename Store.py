import os
from time import sleep


# for x in os.listdir("..\"):
#     if x.endswith(".txt"):
#         # Prints only text file present in My Folder
#         print(x)

while True:
    print(
        " enter '1' for show all product \n '2' for add a product \n '3' for edit existing product"
    )
    usr_choise = input("Enter your choice: ")

    if usr_choise == "1":  # Read abailable product details
        all_products = os.listdir("./products")
        for a in range(len(all_products)):
            product_name = all_products[a].replace(".txt", "")
            with open(f"./products/{all_products[a]}", "r") as product_read:
                product_data = (product_read.read()).split(" ")
            print(
                f"\n{product_name} || quantity {product_data[1]} || price {product_data[0]}"
            )

    elif usr_choise == "2":  # Add new product
        new_product_name = input("Enter New Product name: ")
        all_products = os.listdir("./products")
        if all_products.count(f"{new_product_name.capitalize()}.txt") > 0:
            print("\nProduct name already available \n")
            continue
        quantity = int(input("Enter Quantitity of new product: "))
        price = int(input("Enter Price of the product: "))
        with open(f"./products/{new_product_name.capitalize()}.txt", "w") as new_pr:
            new_pr.write(f"{price} {quantity}")
        for a in range(3):
            print("\n")
            sleep(0.5)
        print("Product Added to your Billing Machine\n\n")

    elif usr_choise == "3":  # Edit a  product details
        inpt_name = input("Enter Product Name: ")
        pr_name = inpt_name.capitalize()
        try:
            with open(f"./products/{pr_name}.txt", "r") as product:
                data = product.read().split(" ")
            print(f"{pr_name} price is {data[0]} || quantity {data[1]}")

        except:
            print("\nInvalid input\n")
            continue

        print(f"enter value for {pr_name}")
        price = input("Enter price(x for escape): ")
        quantity = input("Enter quantity(x for escape): ")
        if price == "x":
            price = data[0]
        if quantity == "x":
            quantity = data[1]

        with open(f"./products/{pr_name}.txt", "w") as edited:
            edited.write(f"{price} {quantity}")

        for a in range(3):
            print("\n")
        print("\nEdit sucessfully applied\n")

    else:
        print("\nInvalid input\n")
