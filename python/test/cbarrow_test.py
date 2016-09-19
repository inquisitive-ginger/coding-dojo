def grader(score):
    print score;
    if score < 59:
        letter_grade = "Bad Bongos!"
    elif (score >= 60 and score < 70):
        letter_grade = "D"
    elif (score >= 70 and score < 80):
        letter_grade = "C"
    elif (score >= 80 and score < 90):
        letter_grade = "B"
    elif (score >= 90 and score <= 100):
        letter_grade = "A"
    else:
        print "Fell through"
    # print "Your Score is {}. Your grade is: {}".format(score, letter_grade)


print "Please enter the scores:"

print "What is your 1st score?"
score = raw_input()
grader(score)
