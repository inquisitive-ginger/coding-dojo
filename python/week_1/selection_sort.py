import random

def selectionSort(list):
    for i in range(len(list)):
        cMin = list[i]

        for j in range(i, len(list)):
            if cMin < list[j]:
                continue
            else:
                cMin = list[j]
                cMinIdx = j

        list[cMinIdx] = list[i]
        list[i] = cMin

        # print "Current sublist: {}".format(list[:i])

list = random.sample(range(100), 1000)
print list
sort(list)
print list
