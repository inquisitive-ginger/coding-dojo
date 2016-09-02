def oddOrEven(start, stop):
    for val in range(start, stop):
        print "Number is " + str(val) + ". This is an {} number.".format("even" if val % 2 == 0 else "odd")

oddOrEven(1, 2000)
