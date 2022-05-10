array = [5,1,22,25,6,-1,8,10]
sequence = [1,6,-1,10]

#edge case
# array = [1, 1, 1, 1, 1]
# sequence =[1, 1, 1]

#this is scratch do not use.
def isValidSubsequenceSolution1(array, sequence):
    indx = 0
    subsequence = []
    for x in array:
        if len(subsequence) >= len(sequence):
            break
        if array[indx] in sequence:
            subsequence.append(x) 
            indx+=1
        else:
            indx+=1
    
    if subsequence == sequence:
        print(subsequence)
        return True
    return False   


# print(isValidSubsequenceSolution1(array, sequence))


#O(n) time | O(1) space
def isValidSubsequenceSolution2(array, sequence):
    arrIdx = 0
    seqIdx = 0
    while arrIdx < len(array) and seqIdx < len(sequence):
        if array[arrIdx] == sequence[seqIdx]:
            seqIdx+= 1
        arrIdx+=1
    return seqIdx == len(sequence)

print(isValidSubsequenceSolution2(array,sequence))