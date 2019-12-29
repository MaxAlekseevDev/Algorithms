#! /usr/bin/env python
# -*- coding: utf-8 -*-
def algorithm(number1, number2):
    m = number1
    n = number2
    start = True
    while(start):
        t = m // n
        r = m - n * t
        if r == 0:
            print("Наибольшим числителем для {} и {} есть {}".format(number1, number2 , n))
            start = False
        else:
            m = n
            n = r

