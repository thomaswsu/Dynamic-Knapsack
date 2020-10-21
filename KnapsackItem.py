class KnapsackItem(object):
    """ Used to represent a item in a Knapsack 
    """
    def __init__(self, weight, value):
        """ Each item needs a weight and value to be constructed
        """
        self.weight = weight
        self.value = value
        self.used = False
    
    def getRatio(self) -> float:
        return(self.value / self.weight)

    def originalForm(self) -> list:
        """ Returns original item, from modified form
        """
        return([self.weight, self.value])

    def __add__(self, lst):
        lst.append(self)  
        return(lst)