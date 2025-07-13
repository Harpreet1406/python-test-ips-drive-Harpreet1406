def smallest_missing_positive_integer(nums):
    nums_set = set(nums)
    n = len(nums)
    
    for i in range(1, n + 2):  # Check up to n+1
        if i not in nums_set:
            return i






    



  

