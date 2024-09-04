
def main():
    coke_price = 50
    coins = [25, 10, 5]

    amt_due = int(coke_price)
    print(f"Amount Due: {amt_due}")

    while amt_due > 0 :
        insert_coin = int(input("Insert Coin: "))
        if insert_coin in coins:
            amt_due = amt_due - insert_coin
            if amt_due > 0:
               print(f"Amount Due: {amt_due}")
            else:
                print(f"Change Owed: {abs(amt_due)}")
        else:
            print(f"Amount Due: {abs(amt_due)}")

# abs to return absolute value rather in minus if paid more than expected



main()
