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
    max = mylist[0]
    for i in mylist:
        if max < i:
            max = i
    return mylist.index(i)

# answer 5
def find_if_number_divisible_10(numbers_list):
    for i in numbers_list:
        if i % 10 == 0:
            return i
    return -1
#print (modolo10([5,55,20]))
#answer6
def count_6_in_the_list(mylist):
    counter = 0
    for i in mylist:
        if i == 6:
            counter += 1
    return counter
#print (sixtime([2,3,4,5,6,6,6,6,6]))
#answer 7
def count_Length_of_string_if_its_4 (list_of_strings):
    counter = 0
    for i in list_of_strings:
        if len(i) == 4:
            counter += 1
    return counter

#print (count_string4(["ffss","fff","kfrs","dd"]))
#answer 8
def lists(list_of_strings):
    for i in list_of_strings:
    if isinstance(i,list_of_strings):
        return true
    return false