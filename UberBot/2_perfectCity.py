def perfectCity(departure, destination):
    d1 = departure
    d2 = destination
    if abs(d1[0] - d2[0]) >= abs(d1[1] - d2[1]):
        r1 = abs(d1[0] - d2[0])
        r2 = min((d1[1] + d2[1]), (abs(int(d2[1]+0.5)-d1[1])+ abs(int(d2[1]+0.5)-d2[1])), (abs(int(d1[1]+0.5)-d1[1])+ abs(int(d1[1]+0.5)-d2[1])))
        print 'A', r1, r2
    else:
        r1 = abs(d1[1] - d2[1])
        r2 = min((d1[0] + d2[0]), (abs(int(d2[0]+0.5)-d1[0])+ abs(int(d2[0]+0.5)-d2[0])), (abs(int(d1[0]+0.5)-d1[0])+ abs(int(d1[0]+0.5)-d2[0])))
        print 'B', r1, r2
    return r1 + r2
    

# TEST
d1= [0.4, 1]
d2 = [0.9, 3]
print d1, d2
print perfectCity(d1, d2), "\n"

d1= [0, 2]
d2 = [2, 0.5]
print d1, d2
print perfectCity(d1, d2), "\n"

d1= [0, 2]
d2 = [2, 2.5]
print d1, d2
print perfectCity(d1, d2), "\n"