import copy
import numpy as np
# Project Euler Problem 31

target = 10
#coins = [1, 2, 5, 3]
coins = np.array([6.6, 3.4, 5.7, 1.002])
# [120, 340, 570, 101]
# preprocess


coins_n = np.array(coins)
base = 1

while np.sum(coins_n) != 0:
    base *= 10
    base_coin = base*coins
    coins_n = base_coin.astype(np.int64) - base_coin


new_target = target*base
if int(new_target) - new_target != 0:
    print("No ways xd")

coins = (base*coins).astype(np.int64)
ways = [1] + [0]*new_target

for coin in coins:
    for i in range(coin, new_target+1):
        ways[i] += ways[i-coin]  # la

print("Ways to make change =", ways[new_target])  # xd
