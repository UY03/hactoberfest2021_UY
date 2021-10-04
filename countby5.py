def count_by_5():
    """ Count from 5 to 100 in steps of 5 """
    """ 5 10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85 90 95 100 """
    print ('Counting from 5 through 100 in steps of 5')
    ct = 5
    while ct <= 100:
        print(ct, end = " ")
        ct = ct + 5
count_by_5()