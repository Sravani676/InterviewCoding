'''
Find unqiue numbers in a given array
'''
#first solution is to use inbuilt functions set() and list(), set() eliminates the duplicate numbers, list() converts the set into list
def uniqueNumbers(nums:List[int])->List[int]:
    return list(set(nums))

#second solution is to loop through the list and add to the unique numbers list if it doesn't exist in the list
def uniqueNumbers(nums:List[int])->List[int]:
    uniq_nums = []
    for num in nums:
        if num not in uniq_nums:
            uniq_nums.append(num)
    return uniq_nums
