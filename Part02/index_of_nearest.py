import sys


def index_of_nearest(numbers, number):
    dist = sys.maxsize
    index = -1
    for i in range(len(numbers)):
        if abs(number - numbers[i]) < dist:
            dist = abs(number - numbers[i])
            index = i
    return index


print(index_of_nearest([], 17))
print(index_of_nearest([7, 13, 3, 5, 18], 0))
print(index_of_nearest([9, 5, 3, 2, 11], 4))
print(index_of_nearest([7, 5, 4, 4, 3], 4))
