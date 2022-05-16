# answer 1
def sum_list(mylist):
    sum = 0
    for i in mylist:
        sum = sum + i
    return sum
#answer 2
def mul_list(mylist):
    result = 1
    for i in mylist:
        result = result * i
    return result
#answer 3
def max_number(mylist): #[2, 3, 6]
    max = mylist[0]
    for i in mylist:
        if max < i:
            max = i
    return i
# answer 4
def place_max_number(mylist):
    place_max_number = place_max_number[0]
    for i in mylist:
        if maxnumber < i:
            return index(mylist)
# answer 5
def modolo10(mylist):
    modolo10 = modolo10[0]
    for i in mylist:
        if modolo10 % 10 == 0:
            return i
        else:
            return "-1"
#answer6
def sixtime(mylist):
    counter = 0
    for i in mylist:
        if i == 6:
            counter += 1
    return counter
#print (sixtime([2,3,4,5,6,6,6,6,6]))
#answer 7

