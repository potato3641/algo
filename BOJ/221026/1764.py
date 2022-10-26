N,M=map(int,input().split())
deudo=set([input() for _ in range(N)])
bodo=set([input() for _ in range(M)])
db=sorted(list(deudo&bodo))
print(len(db))
for i in db:
    print(i)
