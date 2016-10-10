# https://codefights.com/fight/TTHfLTM5WY6DZbmSJ

def jetDashboard(orders, n):
    def stdDev(X):
        if len(X) == 1:
            return -1
        mean = sum(X)/float(len(X))
        tot = 0.0
        for x in X:
            tot += (x - mean)**2
        return (tot/(len(X)-1))**0.5
    
    record = []
    res = []
    maxNum = None
    for i in range(len(orders)-n, len(orders)):
        record.append(orders[i])
        if orders[i] > maxNum:
            maxNum = orders[i]
        average = sum(record)/float(len(record))
        std = stdDev(record)
        res.append([maxNum, round(average, 5), round(std, 5)])
    print record
    return res
        










# TEST

orders = [4, 2, 5, 9, 2]
n = 5
print jetDashboard(orders, n)
'''
jetDashboard(orders, n) = [[4, 4.0,     -1], 
                           [4, 3.0,     1.41421], 
                           [5, 3.66667, 1.52752], 
                           [9, 5.0,     2.94392],
                           [9, 4.4,     2.88097]]
'''

print

orders = [4, 2, 5, 9, 2]
n = 3
print jetDashboard(orders, n)
'''
jetDashboard(orders, n) = [[4, 4.0,     -1], 
                           [4, 3.0,     1.41421], 
                           [5, 3.66667, 1.52752], 
                           [9, 5.0,     2.94392],
                           [9, 4.4,     2.88097]]
'''