import csv

def is_ordered(list):

    flag = False
    i = 0
    while i != len(list) - 1:
        if(list[i] <= list[i + 1]):
            flag = True
        else:
            return False

        i += 1

    return flag

def is_ordered_recursive(list, i):

    if i == 1 or len(list) <= 1:
        return False

    if(list[i] < list[i - 1]):
        return True

    return is_ordered_recursive(list, i-1)

test_list = [7,-4,8,12,0]
print(is_ordered(test_list))
print(is_ordered([1,1,1,1,1]))
print(is_ordered([1,2,3]))
list_one = [7,-4, 8, 12, 0]
print(is_ordered(list_one))

print("----------------------------------------------------------")

print(is_ordered_recursive(list_one, len(list_one) - 1))
print(is_ordered_recursive(test_list, len(test_list) - 1))
test_list_two = [1,2,3]
print(is_ordered_recursive(test_list_two, len(test_list_two) - 1))

print("----------------------------------------------------------")

def is_ordered_new(list):

    flag = False
    i = 0
    for i in range(len(list) - 1):
        if (list[i] <= (list[i + 1])):
            flag = True
        else:
            flag = False

        i += 1

    return flag



print(is_ordered_new([1,1,1,1,1]))
print(is_ordered_new([1,2,3]))
print(is_ordered_new([7,-4, 8, 12, 0]))
list_one = [7,-4, 8, 12, 0]

print("----------------------------------------------------------")

print("what is your age?")

print("what Province do you live in?")

with open('filename', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        print(line)

