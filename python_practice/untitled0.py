# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 20:35:12 2018

@author: jin
"""

from FirstClasses import *

x = FirstClass()
y = FirstClass()

x.setdata("King Arthur")
y.setdata(3.14159)

x.display()
y.display()

x.data = 'King Peng'
x.display()

z= SecondClass()
z.setdata(24)
z.display()


