test_cases = int(input())
for i in range(test_cases):
    s = set()
    n = int(input())
    ls = list(map(int, input().split()))
    prev_number = ls[0]
    s.add(ls[0])
    for j in range(1,n):
        if ls[j]== prev_number:
            s.add(ls[j]+1)
            prev_number+=1
        else:
            s.add(ls[j])
            if prev_number<ls[j]:
                prev_number = ls[j]
    print(len(s))
        
