from KnapsackItem import *

class DynamicKnapsackTable(object):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.table = [[ [] for _ in range(x + 1)] for _ in range(y + 1)] # initilize empty list 
        
        # for i in range(y + 1): # set that first row and column to 0 
        #     (self.table)[i][0] = []
        # for i in range(x + 1):
        #     (self.table)[0][i] = []
    
    def getItems(self, x: int, y: int) -> list:
        """ Returns the the actual of items in a table
        """
        return((self.table)[y][x])

    def getValue(self, x: int, y: int) -> int:
        """ Returns the sum of value in a particular part of the table
        """
        value = 0
        
        for item in self.getItems(x, y):
            value += item.value

        return(value)
    
    def getWeight(self, x: int, y: int) -> int:
        """ Return the weight sum of weight in a particular part of the table
        """
        weight = 0
        for item in (self.table)[y][x]:
            weight += item.weight
        return(weight)

    def updateTable(self, item: KnapsackItem, x: int, y: int) -> None:
        """ Add a value in the table
        """
        ((self.table)[y][x]).extend(item)

    def returnAnswer(self) -> list:
        answer = []
        for item in ((self.table)[self.y][self.x]):
            answer.append(item.originalForm())
        return(answer)

    def returnMax(self, x1, y1, x2, y2, extraItem) -> list:
        """ Made just to solve the stupid part 2
        """
        first = self.getItems(x1, y1)
        second = self.getItems(x2, y2)
        second.append(extraItem)
        return(max(first, second, key = sumValue))

def sumValue(lst: list) -> int:
        sum = 0
        for item in lst:
            sum += item.value
        return(sum)
