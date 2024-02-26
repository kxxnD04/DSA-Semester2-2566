"""Labs 12.01 - Coin Exchange"""
from json import loads as pubeth
def coin_exchange(amount: int, coins: dict):
    """greedy alg"""
    lis, ans, used = [10, 5, 2, 1], 0, {}
    print("Amount:", amount)
    for price in lis:
        ans += min(amount//price, coins[str(price)])
        used[price] = min(amount//price, coins[str(price)])
        amount -= min(amount//price, coins[str(price)])*price
    if amount <= 0:
        print("Coin exchange result:")
        for coin in used:
            print("  {} baht = {} coins".format(coin, used[coin]))
        print("Number of coins:", ans)
    else:
        print("Coins are not enough.")
coin_exchange(int(input()), pubeth(input()))
