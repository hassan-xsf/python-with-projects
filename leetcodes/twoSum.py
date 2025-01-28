
def twoSum(nums, target):
    sumsMap = {}
    for i , n in enumerate(nums):
        diff = target - n
        if diff in sumsMap:
            return [sumsMap[diff] , i]
        sumsMap[n] = i
    return []

# Test cases
def test_twoSum():
    # Test case 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print(twoSum(nums1, target1))  # Expected: [0, 1]
    
    # Test case 2
    nums2 = [3, 2, 4]
    target2 = 6
    print(twoSum(nums2, target2))  # Expected: [1, 2]

if __name__ == "__main__":
    test_twoSum()