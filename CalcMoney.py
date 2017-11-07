#coding: utf-8

import sys
import math

def yearRate2DayRate(yearRate, day_of_year = 360):
    #base = xx
    #base * (1 + yearRate) = base * (1 + dayRate)^n
    dayRate = math.pow(1 + yearRate, 1.0 / day_of_year) - 1
    return dayRate

def calcTotalByDays(base, yearRate, days):
    dayRate = yearRate2DayRate(yearRate)
    total = base * math.pow(1 + dayRate, days)
    return total

def yearRate2MonthRate(yearRate):
    #base = xx
    #base * (1 + yearRate) = base * (1 + monthRate)^12
    monthRate = math.pow(1 + yearRate, 1.0 / 12) - 1
    return monthRate

def calcTotalByMonths(base, yearRate, months):
    monthRate = yearRate2MonthRate(yearRate)
    total = base * math.pow(1 + monthRate, months)
    return total

def calcTotalByFreqInput(inputBase, freqDays = 30, yearRate = 0.04, days = 360):
    daysLeft = days
    totalBase = 0
    total = 0
    while (daysLeft > 0):
        totalBase += inputBase
        total += calcTotalByDays(inputBase, yearRate, daysLeft)
        daysLeft -= freqDays
    return totalBase,total,total-totalBase

def calcTotalByFreqInput_Month(inputBase, freqMonth = 1, yearRate = 0.04, months = 12):
    monthsLeft = months
    totalBase = 0
    total = 0
    while (monthsLeft > 0):
        totalBase += inputBase
        total += calcTotalByMonths(inputBase, yearRate, monthsLeft)
        monthsLeft -= freqMonth
    return totalBase, total, total-totalBase

def calcTotalByFreqInput_Years(inputBase, freq = 1.0 / 12, yearRate = 0.04, years = 1):
    yearsLeft = years 
    totalBase = 0
    total = 0
    while (yearsLeft > 0):
        totalBase += inputBase
        total += inputBase * math.pow(1 + yearRate, yearsLeft)
        yearsLeft -= freq
    return totalBase, total, total-totalBase

if __name__ == '__main__':
    print(yearRate2DayRate(0.04))
    print(calcTotalByFreqInput(5000, yearRate = 0.04, days = 360))
    print(calcTotalByFreqInput(5000, yearRate = 0.04, days = 3600))

    print(yearRate2MonthRate(0.04))
    print(calcTotalByFreqInput_Month(5000, yearRate = 0.04, months = 12))
    print(calcTotalByFreqInput_Month(5000, yearRate = 0.04, months = 120))

    print(calcTotalByFreqInput_Years(5000, yearRate = 0.04, years = 1))
    print(calcTotalByFreqInput_Years(5000, yearRate = 0.04, years = 10))

