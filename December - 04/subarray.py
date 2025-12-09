N:int = int(input())
K:int = int(input())
nums = list(map(int, input().split()))
def find_subarray(nums: list[int], target:int) -> list[int]:
    for i in range(len(nums)):
        sum:int = 0
        j:int = i
        while( sum <= target and j < len(nums)):
            if( sum == target):
                return [i,j - 1]
            sum = sum + nums[j]
            j = j + 1
    return [-1,-1]

print(find_subarray(nums,K))
        