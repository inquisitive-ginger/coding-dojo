def drawX(list):
    for item in list:
        if type(item) == int:
            print "*"*item
        elif type(item) == str:
            print item[0].lower()*len(item)

list = ["Hi", 5, "ZACH", 20, 6]
drawX(list)
