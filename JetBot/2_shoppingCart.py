def shoppingCart(requests):
    count = 0
    for i in range(len(requests)):
        if requests[i-count] == "checkout":
            del requests[: i + 1 - count]
            count = i+1
            
    res = []
    dic = {}
    itemOrder = []
    for i in requests:
        current = i.split(" : ")
        if current[0] == 'add':
            if current[1] not in dic:
                dic[current[1]] = 1
            else:
                dic[current[1]] += 1
            if current[1] not in itemOrder:
                itemOrder.append(current[1])
        elif current[0] == 'remove':
            del dic[current[1]]
            itemOrder.remove(current[1])
        elif current[0] == 'quantity_upd':
            dic[current[1]] += int(current[2])
    for k in itemOrder:
        if dic[k] > 0:
            res.append(str(k) + ' : ' + str(dic[k]))
    return res




# TEST

requests = ["add : milk",
            "add : pickles",
            "remove : milk",
            "add : milk",
            "quantity_upd : pickles : +4"]
print shoppingCart(requests), '\n'  # ["pickles : 5", "milk : 1"]



requests = ["add : rock",
            "add : paper",
            "add : scissors",
            "checkout",
            "add : golden medal",
            "add : golden medal",
            "quantity_upd : golden medal : -1",]
print shoppingCart(requests), '\n'  # ["golden medal : 1"]











