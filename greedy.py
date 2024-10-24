def find_coins_greedy(amount):
    coins = [50, 10,2,1]
    result = {}

    for coin in coins:
        if amount >= coin:
            count = amount // coin

            if count >0:
                result[coin] = count

            amount -=coin * count

    return result

change = find_coins_greedy(215)
print(change)

def find_min_coins(amount):
    coins = [50, 10,2,1]
    
    min_coins = [float('inf')] * (amount + 1)
    min_coins[0] = 0

    coin_used = [-1] * (amount + 1)

    for coin in coins:
        for current_amount in range(coin, amount +1):
            if min_coins[current_amount - coin] +1 < min_coins[current_amount]:
                min_coins[current_amount] = min_coins[current_amount - coin] +1 
                coin_used[current_amount] = coin

    if min_coins[amount] == float('inf'):
        return None
    
    result = {}
    current_amount = amount
    while current_amount > 0:
        coin = coin_used[current_amount]

        if coin in result:
            result[coin]+=1
        else:
            result[coin] = 1
        
        current_amount -= coin

    return result

print(find_min_coins(215))