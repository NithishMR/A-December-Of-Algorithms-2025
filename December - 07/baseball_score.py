ops:list[str] = list(map(str,input().split()))
print(ops)

scores:list[int] = []
for operation in ops:
    if operation == "+":
        result:int = scores[len(scores) - 1] + scores[len(scores) - 2]
        scores.append(result)
    elif operation == "C":
        scores.pop()
    elif operation == "D":
        result:int = scores[len(scores) - 1] 
        result = result * 2
        scores.append(result)
    else:
        scores.append(int(operation))
    print(scores)
final_score:int = 0
for score in scores:
    final_score+=score
print(final_score)