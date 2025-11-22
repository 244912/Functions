def check_discount(current, previous):
    spadek = previous - current
    procent = (spadek / previous) * 100

    if procent >= 10:
        print("Buy the product!!")
        print(f"Product price reduced by {int(procent)}%")