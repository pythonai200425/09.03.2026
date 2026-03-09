

def print_range_recc_asc(_from, _to):
    if _from > _to:
        print()
        return
    print(_from, end=' ')
    _from += 1
    print_range_recc_asc(_from, _to)

def print_range(_from, _to):
    for x in range(_from, _to + (gap := +1 if _to > _from else -1), gap):
        print(x, end=' ')
    print()

print_range(10, 3)
print_range(2, 9)

print_range_recc_asc(3, 10)

def factorial(a):
    # 5! = 1 * 2 * 3 * 4 * 5
    if a == 0 or a == 1:
        return 1
    result = 2
    for i in range(3, a + 1):
        result *= i
    return result

def factorial_recc(a):
    # 1 * 2 * 3 * 4 * 5
    if a == 0 or a == 1:
        return 1

    #        5 * 4 * 3 * 2 * 1
    # 5 * 4!
    #     4 * 3!
    #         3 * 2!
    #             2 * 1!
    #                 1
    result = a * factorial_recc(a - 1)
    return result

############################### 1
def sum_recc(positive):
    pass

# 5 -> 1 + 2 + 3 + 4 + 5

############################### 2
def multiply_recc(a_pos, b_pos):
    # without *
    pass

# 3, 4 -> 12 3 + 3 + 3 + 3 + 0
# 3, 2 -> 6
# 4, 1 -> 4
# 5, 0 -> 0

############################### 3
def reverse_str_recc(s):
    # without reverse, without [::-1]
    pass

# "hello" -> "olleh"

############################### 4
def sum_list_recc(l1):
    # without function sum
    pass
# [6, 4, 10, 15] -> 35

############################### 5
def count_digits_recc(n):
    pass
# 986 -> 3

############################### 6
def is_palindrome(s):
    pass
# "aba" -> True
# "racecar" -> True
# "hello" -> False

############################### 7
def count_occurrences(lst, target):
    pass
# count_occurrences([1,2,3,2,2,5], 2) -> 3
# count_occurrences([7,7,7], 7) -> 3
# count_occurrences([], 5) -> 0
'''
factorial(5)
= 5 * factorial(4)

factorial(4)
= 4 * factorial(3)

factorial(3)
= 3 * factorial(2)

factorial(2)
= 2 * factorial(1)

factorial(1)
= 1
'''

print(factorial(5))
print(factorial_recc(5))
print(factorial_recc(4))
