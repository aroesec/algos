import sys
import typing
def count_bits(x: int) -> int:
    num_bits = 0
    while x:
        num_bits += x & 1
        x >>=1
    return num_bits


#print(count_bits(12))



test = sys.float_info
#print(test)


def parity(x: int) -> int:
    result = 0
    while x:
        result ^= x & 1
        x >>= 1
    return result


#print(parity(6))

#this program takes in an integer and propagates it's right most bit in binary
def propagate_right_bit(x:int) -> int:
    print(bin(x))
    print(bin(x-1))
    binary = bin(x | x - 1)
    return binary
print(propagate_right_bit(16))


def test_lambda():
    x = lambda a: list(map(print,a)) and None
    print(x([1,2,3,4,5]))

#test_lambda()


def test_lambda1():
    nums1 = [45, 46, 47, 48, 50]
    nums2 = []

    for i in nums1:
        x = lambda i : i+2
        nums2.append(x(i))
    print(nums2)


test_lambda1()
