# list comprehension
nums = [3, 4, 5, 6, 7, 8]

print("Slicing")

# - including the first index until the end
print(nums[0:])

# - excluding the last index from the start
print(nums[1:2])

# - returning all
print(nums[:])

target = 10

def find_target():
    for a, b in enumerate(nums):
        diff = target - b
        if diff in nums[a + 1:]:
            return [a, nums.index(diff)]

print("Target Found")
print(find_target())