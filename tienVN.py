def count_coin_combinations(N, M):
    coins = [5000, 2000, 1000, 500, 200]
    count = 0

    def change_coins(amount, index, change):
        nonlocal count

        if amount == 0 and change <= M:
            count += 1
            return

        if index == len(coins):
            return

        for i in range(amount // coins[index] + 1):
            if change + i > M:
                break
            change_coins(amount - i * coins[index], index + 1, change + i)

    change_coins(N, 0, 0)
    return count

N = int(input())
M = int(input())
print(count_coin_combinations(N, M))
