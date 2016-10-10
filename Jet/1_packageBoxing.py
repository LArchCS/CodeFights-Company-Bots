# https://codefights.com/fight/iget5ru64xYknMSx4

def packageBoxing(pkg, boxes):
    box = -1
    volume = float("inf")
    for i in range(len(boxes)):
        product = 1
        for j in range(len(pkg)):
            dimension = sorted(boxes[i])[j]
            product *= dimension
            if sorted(pkg)[j] > dimension:
                break
        else:
            if product < volume:
                volume = product
                box = i
    return box




# TEST
pkg = [4, 2, 5]
boxes = [[4, 3, 5], [5, 2, 5]]
print packageBoxing(pkg, boxes) # 1

pkg = [4, 4, 2]
boxes = [[2, 4, 4], [4, 4, 3]]
print packageBoxing(pkg, boxes) # 0

pkg = [4, 5, 3]
boxes = [[3, 10, 2], [2, 6, 7], [1, 1, 1]]
print packageBoxing(pkg, boxes) # -1









