answer = []
answer.append(1)
i = 1
while(i<=60):
    if(i%2 == 1):
        answer.append(answer[i-1] * 2)
    else:
        answer.append(answer[i-1] + 1)
    i += 1
        
t = int(raw_input())
for x in range(t):
    n = int(raw_input())
    print answer[n]
