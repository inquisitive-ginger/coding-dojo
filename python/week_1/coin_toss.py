import random

def tossCoin():
    return "heads" if round(random.random()) == 1 else "tails"

results = {"heads": 0, "tails": 0}
for toss in range(0, 2000):
    res = tossCoin()
    print res
    results[res] += 1

    print "Attempt #{}. Tossing a coin...It's {}...Results So Far - {} heads | {} tails".format(toss, res, results["heads"], results["tails"])
