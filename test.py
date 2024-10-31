# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 12:23:38 2024

@author: Dell
"""

def calculate_zakat(saving):
    zakat= saving*0.025
    return zakat

s=float(input('Enter annual saving'))
z= calculate_zakat(s)

print('your zakat is', z)

