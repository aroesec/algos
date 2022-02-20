#this program takes in an integer and propagates it's right most bit in binary
def propagate_right_bit(x:int) -> int:
    binary = bin(x | x - 1)
    return binary
print(propagate_right_bit(16))
