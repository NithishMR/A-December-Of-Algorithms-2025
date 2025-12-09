def find_islands(nums: list[list[int]]) -> int:
    def make_zeros(i: int, j: int) -> None:
        if i < 0 or i >= len(nums) or j < 0 or j >= len(nums[0]):
            return
        if nums[i][j] == 0:
            return
        nums[i][j] = 0
        make_zeros(i + 1, j)
        make_zeros(i - 1, j)
        make_zeros(i, j + 1)
        make_zeros(i, j - 1)

    island_count:int = 0

    for i in range(len(nums)):
        for j in range(len(nums[i])):
            if nums[i][j] == 1:
                island_count += 1
                make_zeros(i, j)

    return island_count


# result = find_islands([
#     [1,1,0,0,0],
#     [1,1,0,0,1],
#     [0,0,0,1,1],
#     [0,0,0,0,0]
# ])
R = int(input())
C = int(input())
nums:list[list[int]] = []
for i in range(C):
    sub_arr = list(map(int, input().split()))
    nums.append(sub_arr)
print(nums)
result:int = find_islands(nums)
print(result)
