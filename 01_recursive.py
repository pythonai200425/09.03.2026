

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

print(factorial(5))
print(factorial_recc(5))
print(factorial_recc(4))

############################### 1
def sum_recc(n):
    if n <= 1:
        return 1
    return n + sum_recc(n - 1)

# 5 -> 0 + 1 + 2 + 3 + 4 + 5
print(sum_recc(5))

############################### 2
def multiply_recc(a_pos, b_pos):
    if b_pos == 0 or a_pos == 0:
        return 0
    result = a_pos + multiply_recc(a_pos, b_pos - 1)
    return result

print('3*4 =', multiply_recc(3, 4))
print('3*2 =', multiply_recc(3, 2))
print('3*1 =', multiply_recc(3, 1))
print('3*0 =', multiply_recc(3, 0))
print('1*5 =', multiply_recc(1, 5))
print('0*5 =', multiply_recc(0, 5))

# 3, 4 -> 12 3 + 3 + 3 + 3 + 0
# 3, 2 -> 6
# 4, 1 -> 4
# 5, 0 -> 0

############################### 3
def reverse_str_recc(s):
    # without reverse, without [::-1]

    # stop condition -> len(s) == 0
    # "hello"
    # 'o' + rev('hell')='o lleh'
    # 'l' + rev('hel') ='l leh'
    # 'l' + rev('he')  ='l eh'
    # 'e' + rev('h')   ='e h'
    # 'h' + rev('')    ='h'
    # ''

    # o + "hell" olleh
    # l + "hel" lleh
    # l + "he" leh
    # e + "h"  eh
    # h + ""
    # ""
    if len(s) == 0:
        return ''
    return s[-1] + reverse_str_recc( s[0 : len(s) - 1] )

print(reverse_str_recc('hello'))

# "hello" -> "olleh"

############################### 4
def sum_list_recc(l1):
    # if not l1:
    #     return 0
    if len(l1) == 0:
        return 0

    result = l1[-1] + sum_list_recc(l1[0:-1])
    return result

print(sum_list_recc([6, 4, 10, 15]))
print(sum_list_recc([15]))
print(sum_list_recc([]))

# [6, 4, 10, 15] -> 35

############################### 5
def count_digits_recc(n):
    if n == 0:
        return 0
    result = 1 + count_digits_recc(n // 10)
    return result

# 986 -> 3
print(count_digits_recc(986))

############################### 6
def is_palindrome(s):
    # racecar -> True, equal edges
    # ^     ^
    #  aceca  -> True, equal edges
    #  ^   ^
    #   cec   -> True, equal edges
    #   ^ ^
    #    e    -> True, 1 char

    # abba
    # ^  ^
    #  bb
    #  ^^

    if len(s) <= 1:
        return True
    # 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbbccccccccccccccccccccccccccccccaaaa'
    equal_sides = s[0] == s[-1]
    if not equal_sides:
        return False
    return equal_sides and is_palindrome(s[1: -1])

# "aba" -> True
# "racecar" -> True
# "hello" -> False
print(is_palindrome("aba"))
print(is_palindrome("hello"))
print(is_palindrome("racecar"))

############################### 7
def count_occurrences(lst, target):
    if len(lst) == 0:
        return 0

    plus1 = 0
    if lst[0] == target:
        plus1 = 1

    # short
    # return (1 if lst[0] == target else 0) + count_occurrences(lst[1:], target)

    return plus1 + count_occurrences(lst[1: ], target)




print(count_occurrences([1,2,3,2,2,5], 2)) # -> 3
print(count_occurrences([7,7,7], 7)) #-> 3
print(count_occurrences([], 5)) # -> 0
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


print()
print()