import random 
import time
from DynamicKnapsackTable import *

def getRatio(item: KnapsackItem) -> float:
    if type(item) == KnapsackItem:
        return(item.getRatio())
    raise TypeError("getRatio was not fed an KnapsackItem")

def greedyKnapsack(lst: list, W: int) -> list:
    items = [] # convert to item class 
    output = []
    
    for item in lst:
        items.append(KnapsackItem(item[0], item[1]))

    items.sort(key = getRatio)
    
    for item in items:
        if W == 0:
            break
        if W >= item.weight and item.used == False:
            output.append(item.originalForm())
            W -= item.weight
            item.used = True

    return(output)

def getWeight(table: DynamicKnapsackTable, x: int, y: int) -> int:
    if type(table) == DynamicKnapsackTable:
        return(table.getWeight(x, y))
    raise TypeError("getWeight was not fed an DynamicKnapsackTable")

def dynamicKnapsack(lst: list, W: int) -> list:
    table = DynamicKnapsackTable(W, len(lst))
    items = []
    
    for item in lst:
        items.append(KnapsackItem(item[0], item[1]))

    for j in range(len(items) + 1):
        for w in range(1, W + 1):
            if j == 0 or w == 0:
                table.updateTable([], w, j)
            elif items[j - 1].weight > w:
                table.updateTable(table.getItems(w, j - 1), w, j )
            else:
                table.updateTable(table.returnMax(w, j - 1, w - items[j - 1].weight, j - 1, items[j - 1]), w, j)
    return(table.returnAnswer())

if __name__ == "__main__":
    print("LPS for [9, 14, 9, 5, 10, 6, 15, 6, 13, 9]:", \
        longestPalindromicSequence([9, 14, 9, 5, 10, 6, 15, 6, 13, 9]))
    print("LPS for [7, 2, 4, 6, 9, 11, 2, 6, 10, 6, 15, 6, 14, 2, 7, 5, 13, 9, 12, 15]:", \
        longestPalindromicSequence([7, 2, 4, 6, 9, 11, 2, 6, 10, 6, 15, 6, 14, 2, 7, 5, 13, 9, 12, 15]))
    randomLst = []
    for _ in range(1000):
        randomLst.append(random.randint(1, 100))
    print("Random LPS:", longestPalindromicSequence(randomLst))

    print("Greedy Knapsack 100:", greedyKnapsack([[96, 91], [96, 92], [96, 92], [97, 94], [98, 95], \
        [100, 94], [100, 96], [102, 97], [103, 97], [104, 99], [106, 101], \
            [107, 101], [106, 102], [107, 102], [109, 104], [109, 106], [110, 107], \
                [111, 108], [113, 107], [114, 110]], 100))
    print("Greedy Knapsack 200:", greedyKnapsack([[96, 91], [96, 92], [96, 92], [97, 94], [98, 95], \
        [100, 94], [100, 96], [102, 97], [103, 97], [104, 99], [106, 101], \
            [107, 101], [106, 102], [107, 102], [109, 104], [109, 106], [110, 107], \
                [111, 108], [113, 107], [114, 110]], 200))
    print("Greedy Knapsack 300:",greedyKnapsack([[96, 91], [96, 92], [96, 92], [97, 94], [98, 95], \
        [100, 94], [100, 96], [102, 97], [103, 97], [104, 99], [106, 101], \
            [107, 101], [106, 102], [107, 102], [109, 104], [109, 106], [110, 107], \
                [111, 108], [113, 107], [114, 110]], 300))
    
    print("Dynamic Knapsack 100:", dynamicKnapsack([[96, 91], [96, 92], [96, 92], [97, 94], [98, 95], \
        [100, 94], [100, 96], [102, 97], [103, 97], [104, 99], [106, 101], \
            [107, 101], [106, 102], [107, 102], [109, 104], [109, 106], [110, 107], \
                [111, 108], [113, 107], [114, 110]], 100))
    print("Dynamic Knapsack 200:", dynamicKnapsack([[96, 91], [96, 92], [96, 92], [97, 94], [98, 95], \
        [100, 94], [100, 96], [102, 97], [103, 97], [104, 99], [106, 101], \
            [107, 101], [106, 102], [107, 102], [109, 104], [109, 106], [110, 107], \
                [111, 108], [113, 107], [114, 110]], 200))
    print("Dynamic Knapsack 300:", dynamicKnapsack([[96, 91], [96, 92], [96, 92], [97, 94], [98, 95], \
        [100, 94], [100, 96], [102, 97], [103, 97], [104, 99], [106, 101], \
            [107, 101], [106, 102], [107, 102], [109, 104], [109, 106], [110, 107], \
                [111, 108], [113, 107], [114, 110]], 300))