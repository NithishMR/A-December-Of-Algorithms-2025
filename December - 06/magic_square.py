N = int(input("Enter n: "))

def make_magic_square(N: int):
    if N % 2 == 0:
        return "Magic square is only possible for odd values of n."

    M = N * (N * N + 1) // 2

    square = [[0] * N for _ in range(N)]

    i = 0
    j = N // 2

    for num in range(1, N * N + 1):
        next_i = (i - 1) % N
        next_j = (j + 1) % N

        if square[next_i][next_j] != 0:
            i = (i + 1) % N
        else:
            i = next_i
            j = next_j

        square[i][j] = num

   

    return square

result = make_magic_square(N)
for row in result:
    print(*row)
