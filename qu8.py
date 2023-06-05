# Ques 8
def find_triplets(nums):
    nums.sort()                         # Sort the input list in ascending order
    triplets = []

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue                    # Skip duplicate elements

        left = i + 1
        right = len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                triplets.append([nums[i], nums[left], nums[right]])

                                        # Skip duplicate elements
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1

            elif total < 0:
                left += 1
            else:
                right -= 1

    return triplets

nums = [-25, -10, -7, -3, 2, 4, 8, 10]
triplets = find_triplets(nums)
print(triplets)

#output[[-10,2,8],[-7,-3,10]]