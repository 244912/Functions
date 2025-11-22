def f(amount):
    ile = 0

    ile = ile + amount // 5
    amount = amount % 5

    ile = ile + amount // 2
    amount = amount % 2

    ile = ile + amount

    return ile