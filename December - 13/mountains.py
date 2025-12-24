N:int = int(input())

arr:list[int] = list(map(int, input().split()))

i: int = 1
doesNotExist:bool = True
while i < N - 1 :
    if (arr[i] > arr[i -1]) and (arr[i] > arr[i + 1]):
        print(i,end=" ")
        doesNotExist = False
    i = i + 1

if doesNotExist:
    print(-1)