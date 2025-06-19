nums = [12,34,23,5,23,53,23,5,23,23]
lnth = len(nums)
for i in range(lnth):
    min = i
    for j in range(i+1,lnth):
        if nums[j] < nums[min]:
            nums[min],nums[j] = nums[j],nums[min]

print(nums)




#🧠 Time Complexity:
# Best case: O(n²)

# Average case: O(n²)

# Worst case: O(n²)

# Space complexity: O(1) (in-place)

