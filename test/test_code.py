
def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    i = 0
    for j,k in enumerate(nums):
        if(val != k):
            nums[i] = nums[j]
            i += 1
    print(nums)
    return len(nums)


def main():
    num_list = [0,1,2,2,3,0,4,2]
    val = 2
    removeElement(num_list,val)

if __name__ == '__main__':
    main()