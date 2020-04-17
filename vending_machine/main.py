"""
A vending machine has the following denominations: 1c, 5c, 10c, 25c, 50c, and $1. 
Your task is to write a program that will be used in a vending machine to return change. 
Assume that the vending machine will always want to return the least number of coins or notes. 
Devise a function getChange(M, P) where M is how much money was inserted into the machine and P the price of the item selected, that returns an array of integers representing the number of each denomination to return. 

Example:
getChange(5, 0.99) // should return [1,0,0,0,0,4]"""
import math

examples = (
    ([10, 1], [0,0,0,0,0,9]),
)

def getChange(M, P):
    change = (int(M*100) - int(P*100))
    amounts = [0, 0, 0, 0, 0, 0]
    coins = [100, 50, 25, 10, 5, 1]
    for i in range(0, len(coins)):
        coin = coins[i]
        if change >= coin:
            amounts[i] = int(change/coin)
            change = change % coin
        
        if not change >= 1:
            break
    
    amounts.reverse()
    return amounts


# for params, result in examples:
#     print(params)
print(getChange(10, 1))
print(getChange(10, 5))
print(getChange(10, 5.5))
print(getChange(5, 0.99))
print(getChange(5, 0.98))
print(getChange(5, 0.98))
print(getChange(5, 0.96))
print(getChange(5, 0.97))
print(getChange(5, 0.75))
print(getChange(5, 0.51))
