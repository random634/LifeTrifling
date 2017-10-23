#coding: utf-8

import sys
import math

def yearRate2DayRate(yearRate, day_of_year = 365):
    #base = xx
    #base * (1 + yearRate) = base * (1 + dayRate)^n
    dayRate = math.pow(1 + yearRate, 1.0 / day_of_year) - 1
    return dayRate

def calcTotalByDays(base, yearRate, days):
    dayRate = yearRate2DayRate(yearRate)
    total = base * math.pow(1 + dayRate, days)
    return total

def calcTotalByFreqInput(inputBase, freqDays = 30, yearRate = 0.04, days = 365):
    daysLeft = days
    totalBase = 0
    total = 0
    while (daysLeft > 0):
        totalBase += inputBase
        total += calcTotalByDays(inputBase, yearRate, daysLeft)
        daysLeft -= freqDays
    return totalBase,total,total-totalBase

if __name__ == '__main__':
    print(calcTotalByFreqInput(2000, yearRate = 0.04, days = 365))
    print(calcTotalByFreqInput(2000, yearRate = 0.04, days = 3650))