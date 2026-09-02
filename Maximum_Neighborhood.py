t=int(input())
for c in range(t):
    n=int(input())
    grid=[]
    value=1
    for j in range(n):
        row=[]
        for k in range(n):
            row.append(value)
            value+=1
        grid.append(row)
    dirs=[(-1,0),(1,0),(0,-1),(0,1)]
    max_cost=0
    for j in range(n):
        for k in range(n):
            cost=grid[j][k]
            for dj,dk in dirs:
                nj=j+dj
                nk=k+dk
                if 0<=nj<n and 0<=nk<n:
                    cost+=grid[nj][nk]
            if cost>max_cost:
                max_cost=cost
    print(max_cost)
