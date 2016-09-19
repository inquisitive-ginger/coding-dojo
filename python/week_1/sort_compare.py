import time, random

def bubbleSort(list):
    def bubblePass(list):
        for i in range(0, len(list) - 1):
            firstVal = list[i]
            nextVal = list[i + 1]

            if nextVal < firstVal:
                list[i] = nextVal
                list[i + 1] = firstVal

    while(not(all(list[i] < list[i + 1] for i in range(len(list) - 1)))):
        bubblePass(list)

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

def insertionSort(list):


sorts = {
    "Bubble": bubbleSort,
    "Selection": selectionSort
}

list = random.sample(range(10000), 10000)
for sort in sorts:
    start = time.time()
    sorts[sort](list[:])
    print "{} execution time: {} ms".format(sort, 1000 * (time.time() - start))
