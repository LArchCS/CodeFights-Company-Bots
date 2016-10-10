# -*- coding: utf-8 -*-
# https://codefights.com/fight/TTHfLTM5WY6DZbmSJ

def merchantMinimization(items, merchants):
    import itertools
    
    dic = {i:[] for i in items}
    for item in items:
        for i in range(len(merchants)):
            if item in merchants[i] and (i not in dic[item]):
                dic[item].append(i)
    
    size = len(merchants)
    options = []
    for i in range(size):
        foo = list(itertools.combinations(range(size), i))
        options += foo
    
    for option in options[1:]:
        score = {i:0 for i in items}
        for i in option:
            for item in dic:
                if i in dic[item]:
                    score[item] = 1
        if sum(score.values()) == len(items):
            return list(option)
    return [-1]

dic = {'kiwis': [1, 2], 'apples': [0, 1, 3], 'bananas': [2, 3]}



# TEST
items = ["apples", "bananas", "kiwis"]
merchants = [["apples", "pineapples"],
             ["apples", "kiwis"],
             ["kiwis", "papayas", "bananas"],
             ["bananas", "apples"]]

print merchantMinimization(items, merchants) # [0, 2]




