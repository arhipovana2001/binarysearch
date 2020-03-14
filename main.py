import time
import random

find_list = []
n = int(input('Enter the quanity:'))

for i in range(n):
    find_list.append(random.randint(-100, 100))
find_list.sort()

print('Random list:', find_list)
desired_value = int(input('Enter the number:'))
start = 0
stop = len(find_list) - 1
print()


def recursion(a, x, left, right):
    if left > right - 1:
        return 'Not Found'
    else:
        mid = (left + right) // 2
        #print(mid)
        if x < a[mid]:
            #print('меняем стоп')
            return recursion(a, x, left, mid)
        elif x > a[mid]:
            #print('меняем старт')
            return recursion(a, x, mid, right)

        if mid >= 0 and a[mid] == x:
            print('Index = ', end='')
            return mid


def rec():
    start_time = time.time()
    print(recursion(find_list, desired_value, start, stop))
    print('Time:', time.time() - start_time)


def iterative(a, x, left, right):
    while left < right - 1:
        mid = (left + right) // 2
        if a[mid] > x:
            right = mid
        else:
            left = mid
        if left >= 0 and a[left] == x:
            print('Index =', end=' ')
            return left
    else:
        return 'Not Found'


def itera():
    start_time = time.time()
    print(iterative(find_list, desired_value, start, stop))
    print('Time:', time.time() - start_time)


def main():
    print('Recursive method:')
    rec()
    print()
    print('Iterative method:')
    itera()


main()
