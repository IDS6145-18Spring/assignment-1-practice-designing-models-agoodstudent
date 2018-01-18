import math
from vegtable import vegtable

class distillery():
    '''This is a distillery'''

    def __init__(self, b, e):
        '''Intializes the vegtable'''
        self.beverages = b
        self.employees = e


    def Volume(self):
        '''The volume of a string bean is like a cylinder'''
        return math.pi * self.radius ** 2 * self.length


    def Grow(self):
        '''This is how a stringbean grows'''
        rate =  self.sun*self.water / 1000
        self.radius += 0.14 * rate
        self.length += 0.2 * rate
        self.weight += 0.5 * rate

        volume = self.Volume()
        self.water -= (volume* self.weight) / 2.03
        self.sun = 0.0
        return None