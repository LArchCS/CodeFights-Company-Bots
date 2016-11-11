# -*- coding: utf-8 -*-
#  https://codefights.com/fight/HvAmyEvETRb7rs5zy

def parkingSpot(carDimensions, parkingLot, luckySpot):
    # for cases the shorter side of parking spot (entrance) is along the X axis
    def passCaseX(x1, x2, y1, y2, n):
        count = spotShort
        for x in range(x1, x2):
            for y in range(y1, y2, n):
                if parkingLot[x][y] == 1:
                    if x - x1 < carShort - 1 and x2 - x < carShort - 1: # if the obstacle lies in the middle of the entrance.. 
                        return False
                    count -= 1
                    break
        return count >= carShort  # if the obstacles do not totally block the entrance for the car

    def passCaseY(x1, x2, y1, y2, n):
        # for cases the parking spot entrance is along the Y axis
        count = spotShort
        for y in range(y1, y2):
            for x in range(x1, x2, n):
                if parkingLot[x][y] == 1:
                    if y - y1 < carShort-1 and y2 - y < carShort-1:
                        return False
                    count -= 1
                    break
        return count >= carShort
            
    carShort = min(carDimensions)
    spotShort = min(luckySpot[2] - luckySpot[0] + 1, luckySpot[3] - luckySpot[1] + 1)
    
    if (luckySpot[2]-luckySpot[0]) <= (luckySpot[3] - luckySpot[1]):
        # use <= just in cases of parking spots in squares (have 2 entrances)
        # if == , if this test fail, go to the next test, since there are 2 entrances
        print "short at X\t",
        if (passCaseX(luckySpot[0], luckySpot[2] + 1, 0, luckySpot[3] + 1, 1) or
            passCaseX(luckySpot[0], luckySpot[2] + 1, len(parkingLot[0]) - 1, luckySpot[1] - 1, -1)):
            return True
    
    if (luckySpot[2] - luckySpot[0]) >= (luckySpot[3] - luckySpot[1]):
        print "short at Y\t",
        return (passCaseY(0, luckySpot[2] + 1,luckySpot[1], luckySpot[3] + 1, 1) or
            passCaseY(len(parkingLot) - 1, luckySpot[0] - 1, luckySpot[1], luckySpot[3] + 1, -1))
            
    return False  # if only went into the first test, but failed

 

# TEST

carDimensions = [2, 1]
parkingLot = [[1,1,1,1], [1,0,0,0], [1,0,1,0]]
luckySpot = [1, 2, 1, 3]
print parkingSpot(carDimensions, parkingLot, luckySpot)  # True

carDimensions = [7, 2]
parkingLot = [[0,0,0,0,0,0,0,0], [1,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0]]
luckySpot = [1, 1, 2, 7]
print parkingSpot(carDimensions, parkingLot, luckySpot)  # True

carDimensions = [3,2]
parkingLot = [[1, 0, 1, 0, 1, 0], [0, 0, 0, 0, 1, 0],[0, 0, 0, 0, 0, 1],[1, 0, 1, 1, 1, 1]]
luckySpot = [1, 1, 2, 3]
print parkingSpot(carDimensions, parkingLot, luckySpot)  # True

carDimensions = [4, 1]
parkingLot = [[1, 0, 1, 0, 1, 0], [1, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 1, 1]]
luckySpot = [0, 3, 3, 3]
print parkingSpot(carDimensions, parkingLot, luckySpot)  # True

carDimensions = [7, 2]
parkingLot = [[0,1,0], [0,0,0], [0,0,0], [0,0,0], [0,0,0], [0,0,0], [0,0,0], [0,0,0]]
luckySpot = [1, 0, 7, 1]
print parkingSpot(carDimensions, parkingLot, luckySpot)  # True

carDimensions = [2, 1]
parkingLot = [[1,0,1], [1,0,1], [1,1,1]]
luckySpot = [0, 1, 1, 1]
print parkingSpot(carDimensions, parkingLot, luckySpot)  # True
print 

carDimensions = [4, 2]
parkingLot = [[0,0,0,1], [0,0,0,0], [0,0,1,1]]
luckySpot = [0, 0, 1, 3]
print parkingSpot(carDimensions, parkingLot, luckySpot)  # False

carDimensions = [3,2]
parkingLot = [[1, 0, 1, 0, 1, 0], [1, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 1, 1]]
luckySpot = [1, 1, 2, 3]
print parkingSpot(carDimensions, parkingLot, luckySpot)  # False

carDimensions = [2, 1]
parkingLot = [[1,0,1], [1,0,1], [1,1,1]]
luckySpot = [1, 1, 2, 1]
print parkingSpot(carDimensions, parkingLot, luckySpot)  # False
