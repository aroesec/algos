# O(nlogn) time
# O(1) space

citation_input = [1,4,1,4,2,1,3,5,6]

def get_h_index(citation_input):
    citation_input.sort(reverse= True)
    for index, value in enumerate(citation_input):
        if value >= index+1:
            h_index = index+1
        else:
            break
    return h_index
print(get_h_index(citation_input))
