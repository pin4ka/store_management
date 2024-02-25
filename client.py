import os, shutil, time


def calculation(pr_num, pr_quan):
    with open(f"./temp/{pr_num}.txt", "r") as product_read:
        product_data = product_read.read().split(" ")

    return int(product_data[0]) * pr_quan


def product_count(pr_num, pr_quan):
    with open(f"./temp/{pr_num}.txt", "r") as cache_read:
        cache_data = cache_read.read().split(" ")

    with open(f"./products/{cache_data[2]}.txt", "r") as pr_read:
        product_data = pr_read.read().split(" ")

    product_data[1] = int(product_data[1]) - pr_quan

    with open(f"./products/{cache_data[2]}.txt", "w") as pr_write:
        pr_write.write(f"{int(product_data[0])} {product_data[1]}")
    return f"{cache_data[2]}"


def make_bill(product_name, Quantity, price):
    with open(f"./temp/bill.txt", "a") as bill_write:
        bill_write.write(f"{product_name}   {Quantity}  {price}\n")


def print_bill(total):
    with open(f"./temp/bill.txt", "r") as bill_read:
        the_bill = bill_read.read()
    print("Your bill....")
    print(the_bill, "\nTotal amount         ", total)


while True:
    bill = 0
    print_command = False
    available_pr_lst = []
    try:
        os.mkdir("./temp")
    except:
        shutil.rmtree("./temp")
        os.mkdir("./temp")


    all_products = os.listdir("./products")
    for a in range(len(all_products)):
        with open(f"./products/{all_products[a]}", "r") as count_check:
            count_of_pr = count_check.read().split(" ")
        if int(count_of_pr[1]) > 0:
            available_pr_lst.append(f"{all_products[a].replace(".txt", "")}")
    # SHOW ABAILABLE ITEMS
    print("Available Products")
    for a in range(len(available_pr_lst)):
        # product_name = all_products[a].replace(".txt", "")
        print(f"\t{a+1} {available_pr_lst[a]}|", end="")

        with open(f"./products/{available_pr_lst[a]}.txt", "r") as product_read:
            product_data = product_read.read()

        with open(f"./temp/{a+1}.txt", "w") as temp_data_write:
            temp_data_write.write(product_data + f" {available_pr_lst[a]}")
    print("\n")

    while True:
        try:
            product = input("Enter your product number ('x' for complete): ")
            if product == "x" or product == 'X':
                break
            quaintity = int(input("Enter Quantity: "))
            product_num = int(product)
            product_name = product_count(product_num, quaintity)
            bill = bill + calculation(product_num, quaintity)
            make_bill(product_name, quaintity, calculation(product_num, quaintity))
            print_command = True

        except:
            print("Invalid Input !! \t restart your billing process")
            print_command = False
            break
    
    time.sleep(1)
    print('\n')

    if print_command == True:
        print_bill(bill)
    time.sleep(5)

    shutil.rmtree("./temp")
    for a in range(10):
        time.sleep(0.3)
        print("\n")
    print("\n")
