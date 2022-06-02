# O(nLogn) time | O(1) space
def nonConstructibleChange(coins):
    amount = 1
    coins.sort()
    for coin in coins:
        if coin > amount:
            return amount
        amount +=coin
    return amount 

assert  nonConstructibleChange([1,2,5]) == 4
assert  nonConstructibleChange([5, 6, 1, 1, 2, 3, 4, 9]) == 32








