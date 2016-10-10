# -*- coding: utf-8 -*-
def recurringTask(firstDate, k, daysOfTheWeek, n):
    def leapyr(n):
        if n % 400 == 0:
            return True
        elif n % 100 == 0:
            return False
        elif n % 4 == 0:
            return True
        else:
            return False
    
    def translate(L):
        monthsLocal = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        day = L[0]
        month = L[1]
        year = L[2]
        if leapyr(year):
            monthsLocal[1] = 29
        while day > monthsLocal[month -1]:
            day -= monthsLocal[month -1]
            month += 1
            if month == 13:
                month = 1
                year += 1
                if leapyr(year):
                    monthsLocal[1] = 29
                else:
                    monthsLocal[1] = 28
        res = ['%02d'%(day), '%02d'%(month), '%d'%(year)]
        return "/".join([i for i in res])
    
    def weekDay(year, month, day): 
        # 1. total days after 01/01/1900
        dayOfWeek  = 1    # dayOfWeek for 01/01/1900 = 1, Monday
        years = year - 1900
        totalDays = (years) * 365
        totalDays += years / 4 - years / 100 + (years + 100) / 400 # leap year correction
        
        # 2. total days adding this year's days
        monthsLocal = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if leapyr(year):    # just for this year
            monthsLocal[1] = 29
        totalDays += sum(monthsLocal[0:month - 1]) + day - 1
        
        # 3. calculate the day of the week             
        dayOfWeek = (totalDays % 7 + dayOfWeek) % 7  
        return dayOfWeek
        
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    
    firstDate = firstDate.split('/')
    recurDays = []
    year = int(firstDate[2])
    month = int(firstDate[1])
    day = int(firstDate[0])
    for i in daysOfTheWeek:
        recurDays.append(days.index(i))
    
    if leapyr(year):
        months[1] = 29

    firstDay = weekDay(year, month, day)
    print firstDay
    recurDaysTranslate = []
    
    for i in recurDays:
        dayToAdd = i - firstDay
        if dayToAdd < 0:
            dayToAdd += 7
        recurDaysTranslate.append(dayToAdd)
        
    recurDaysTranslate.sort()
    sequence = []
    for i in range(n/len(recurDaysTranslate) + 1):
        for j in recurDaysTranslate:
            sequence.append(j + i*k*7)
    sequence = sequence[:n]
    
    calendar = []
    for i in range(len(sequence)):
        calendar.append([int(firstDate[0]) + sequence[i], int(firstDate[1]), int(firstDate[2])])
    return [translate(i) for i in calendar]





print recurringTask('01/01/2015', 2, ["Monday", "Thursday"], 4) # ['01/01/2015', '05/01/2015', '15/01/2015', '19/01/2015']

print recurringTask("28/12/2019", 1, ["Saturday"], 11)  #["22/02/2020", 29/02/2020"]   07/03/2020

print recurringTask("01/02/2100", 4, ["Sunday", "Monday"], 4)  # ["01/02/2100", "07/02/2100", "01/03/2100", "07/03/2100"]

print recurringTask("30/05/1995", 4, ["Tuesday"], 1)  # ["30/05/1995"]

print recurringTask("23/02/2000", 2, ["Wednesday", "Friday"], 4)  # ["23/02/2000", "25/02/2000", "08/03/2000", "10/03/2000"]

print recurringTask("31/12/2999", 1, ["Tuesday"], 2)  # ["31/12/2999", "07/01/3000"]

print recurringTask("01/01/1900", 1, ["Monday"], 2)
# 4, 6, 1, 2, 3, 2