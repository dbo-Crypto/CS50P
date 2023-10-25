amount = 50

while amount > 0:
    print(f"Amount Due: {amount}")
    coin = input("Insert Coin: ")
    match coin:
        case "25" | "10" | "5":
            amount = amount - int(coin)
if amount <= 0:
    print(f"Change Owed: {abs(amount)}" )