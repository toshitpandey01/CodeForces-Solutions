nums=list(map(int,input("Enter array elements separated by space: ").split()))
def maxSubArray(nums):
    max_sum=float('-inf')
    n=len(nums)
    for i in range(n):
        current_sum=0
        for j in range(i,n):
            current_sum+=nums[j]
            if current_sum>max_sum:
                max_sum=current_sum
    return max_sum
print(maxSubArray(nums))