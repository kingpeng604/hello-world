# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class FirstClass:
    def setdata(self, value):
        self.data = value
        
    def display(self):
        print(self.data)
        
class SecondClass(FirstClass):
    def display(self):
        print('Current value = "%s"' % self.data)

#x = FirstClass()
#y = FirstClass()
#
#x.setdata("King Arthur")
#y.setdata(3.14159)