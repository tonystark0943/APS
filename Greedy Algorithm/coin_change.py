def coin_change(amount):
    denominations = [1000, 100, 50, 20, 10, 5, 2, 1]
    amt = amount
    no_of_dems = [0]*len(denominations)

    for i in range(len(denominations)):
        no_of_dems[i] = amount//denominations[i]
        amount %= denominations[i]

    print(amt, " in ", no_of_dems)
        
coin_change(750)