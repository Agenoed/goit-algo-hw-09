import time

def find_coins_greedy(amount):

    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    remaining_amount = amount
    for coin in coins:
        if coin <= remaining_amount:
            result[coin] = remaining_amount // coin
            remaining_amount %= coin
    return result

def find_min_coins(amount):

    coins = [1, 2, 5, 10, 25, 50]
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    result = {}
    while amount > 0:
        for coin in coins:
            if dp[amount - coin] == dp[amount] - 1:
                result[coin] = result.get(coin, 0) + 1
                amount -= coin
                break
    return result

def measure_time(func, amount):

    start_time = time.time()
    func(amount)
    end_time = time.time()
    return end_time - start_time


amount = 113
print(f"Жадібний алгоритм для суми {amount}: {find_coins_greedy(amount)}")
print(f"Динамічне програмування для суми {amount}: {find_min_coins(amount)}")


amounts = [1453, 16793, 243453, 1464876]

for amount in amounts:
    greedy_time = measure_time(find_coins_greedy, amount)
    dynamic_time = measure_time(find_min_coins, amount)
    print(f"\nЖадібний алгоритм для суми {amount}: {find_coins_greedy(amount)}")
    print(f"Динамічне програмування для суми {amount}: {find_min_coins(amount)}")
    print(f"  Час виконання для суми {amount}:")
    print(f"  Жадібний алгоритм: {greedy_time:.6f} секунд")
    print(f"  Динамічне програмування: {dynamic_time:.6f} секунд")
