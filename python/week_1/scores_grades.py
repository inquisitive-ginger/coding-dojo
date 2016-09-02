def convertPercentToLetter(p):
    if p >= 90 and p < 100:
        return "A"
    elif p >= 80 and p < 90:
        return "B"
    elif p >= 70 and p < 80:
        return "C"
    elif p >= 60 and p < 70:
        return "D"
    else:
        return "Yikes."

def capturePercent():
    percent = raw_input("Score: ")
    print "Your grade is {}".format(convertPercentToLetter(int(percent)))

print "Scores and Grades"

for i in range(1,10):
    capturePercent()

print "End of program. Bye!"
