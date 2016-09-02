

def printMultiples(start, stop, byValue, parity):
    for val in range(start, stop):
        if val % byValue == 0:
            if parity == "none":
                print val

            if parity == "even" and val % 2 == 0:
                print val

            if parity == "odd" and val % 2 != 0:
                print val

# printMultiples(1, 1000, 1, "odd")
printMultiples(1, 1000000, 5, "none")
# printMultiples(1, 1000000, 5, "even")
