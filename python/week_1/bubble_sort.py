import random, time

def bubblePass(list):
    for i in range(0, len(list) - 1):
        firstVal = list[i]
        nextVal = list[i + 1]

        if nextVal < firstVal:
            list[i] = nextVal
            list[i + 1] = firstVal

list = random.sample(range(10000), 10000)

start = time.time()
while(not(all(list[i] < list[i + 1] for i in range(len(list) - 1)))):
    bubblePass(list)

print "Execution time: {} ms".format(1000 * (time.time() - start))
# print list
