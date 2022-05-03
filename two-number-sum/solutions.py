#Below are a few ways to solve the Two Number Sum Problem

#Test Data
array = [3,5, -4, 8, 11, 1, -1, 6]
targetSum = 10


#O(n) time | O(n) space
def twoNumberSum(array:list[int],targetSum: int) -> list:
    for num in range(len(array)):
        x = targetSum - array[num]
        if x in array and x != array[num]:
           return [x, array[num]]
    else:
        return []

#O(n) time | O(n) space
def twoNumberSumHashTable(array:list[int],targetSum: int) -> list:
    nums = {}
    for num in array:
        potential_target = targetSum - num
        if potential_target in nums:
            return [potential_target, num]
        else: 
            nums[num] = True
    return []

#O(nlog(n)) time | O(1) space
# def twoNumberSumPointer(array:list[int],targetSum: int) -> list:


print(twoNumberSum(array,targetSum))
print(twoNumberSumHashTable(array,targetSum))