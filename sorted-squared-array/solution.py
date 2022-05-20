from re import I


array = [1,3,5,6,8,9]

#O(n) time | O(n) space
def sortedSquaredArray(array):
    squares = []
    for x in (array):
        square = x * x
        squares.append(square)
    squares.sort()
    return squares

print(sortedSquaredArray(array))


def sortedSquaredArrayLogN(array):
    sortedSquares = [0 for _ in array]
    for idx in range((len(array))):
        value= array[idx]
        sortedSquares[idx] = value * value
    sortedSquares.sort()
    return sortedSquares

print(sortedSquaredArrayLogN(array))


