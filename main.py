list = [1,2,3,4,5,6,7,8,9,10,10]
inf = 0
ins = 1
find = 1
while find <= len(list)-1:
    first = list[inf] 
    second = list[ins]
    if first == second:
        print('There is a duplicate number')
        break
    else:
        inf = inf + 1
        ins = ins + 1
        find = find + 1
