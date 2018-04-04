"""
Merge two sorted lists and return it as a new list. 
The new list should be made by splicing together the nodes of the first two lists.
Source: https://leetcode.com/problems/merge-two-sorted-lists/#/description
"""


def merge_two_list_helper(list1, list2):
  	# Start with empty
    merged = []
    # Combine the arrays
    merged_range = len(list1)+len(list2)
    
    
    for i in range(merged_range):
      
        if not list1:
            merged.extend(list2)
            return merged
            
        elif not list2:
            merged.extend(list1)
            return merged
        
        
        # Use pop to remove and return the number
        if list1[0] < list2[0]:
            merged.append(list1.pop(0))
        else:
            merged.append(list2.pop(0))


#DO NOT CHANGE THIS FUNCTION
def merge_two_list(list1,list2):
    return merge_two_list_helper(list1, list2)


#test cases
def main():
    list1 = [1,3,5]
    list2 = [2,4,6]
    print ("merging [1,3,5] and [2,4,6]......")
    print ("expected result is [1,2,3,4,5,6]")
    print ("your output is {}".format(merge_two_list(list1, list2)))

if __name__ == "__main__":
    main()

