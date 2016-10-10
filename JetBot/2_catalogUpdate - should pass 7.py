# -*- coding: utf-8 -*-
# https://codefights.com/fight/iget5ru64xYknMSx4

# 终于明白哪个case 没考虑到了。。 如果update 里 最后一个物品以 z 开头

def catalogUpdate(catalog, updates):
    while updates:
        current = updates.pop(0)
        for c in range(0, len(catalog)):
            if catalog[c][0] == current[0]:
                catalog[c] += current[1:]
                title = catalog[c].pop(0)
                catalog[c] = [title] + sorted(catalog[c])
                break
            elif catalog[c][0] > current[0]:
                catalog.insert(c, current)
                break
        else:
            catalog.insert(-1, current)
    return catalog


                




# TEST
catalog = [["Books", "Classics", "Fiction"],
           ["Electronics", "Cell Phones", "Computers", "Ultimate item"],
           ["Grocery", "Beverages", "Snacks"],
           ["Snacks", "Chocolate", "Sweets"],
           ["root", "Books", "Electronics", "Grocery"]]
updates = [["Snacks", "Marmalade"],
           ["Fiction", "Harry Potter"],
           ["root", "T-shirts"],
           ["T-shirts", "CodeFights"],
           ["zzz", "ABC", "CD"]]
           
for i in catalogUpdate(catalog, updates):
    print i

'''
catalogUpdate(catalog, updates) = [["Books", "Classics", "Fiction"],
                                   ["Electronics", "Cell Phones", "Computers", "Ultimate item"],
                                   ["Fiction", "Harry Potter"],
                                   ["Grocery", "Beverages", "Snacks"],
                                   ["Snacks", "Chocolate", "Marmalade", "Sweets"],
                                   ["T-shirts", "CodeFights"],
                                   ["root", "Books", "Electronics", "Grocery", "T-shirts"]]
'''
