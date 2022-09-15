# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 02:17:10 2022

@author: salva

Formula:
    PV = Pmt/rDec*(1 - (1+rDec)**(-n))
"""

import numpy as np

Pmt = float(input('input payment ->'))

rAPR = float(input('input interest rate, APR -> '))
rDEC = rAPR/1200 # 1200 because monthly pmts
nMonths = int(input('number of months to pay off -> '))

PV = Pmt/rDEC*(1 - (1+rDEC)**(-nMonths))

print(f"for APR={rAPR :.2f}, Pmt = {Pmt:.2f}, \
      number of months = {nMonths:d}")
print(f"Amount you can borrow is {PV:.2f}")
      
if PV < 20000:
          print('sorry, you cant afford a nice car')
elif PV < 30000:
              print('you can buy a Honda Accord')
else:
              print('You can buy a Tesla')
      
      