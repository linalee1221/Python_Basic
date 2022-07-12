from collections import deque
INF = int(1e9)
M, N, H = map(int, input().split())
graph = []
for _ in range(N*H):
    graph.append(list(map(int, input().split())))
vis = [[INF]*M for _ in range(N*H)]
xpos = [0, 0, 1, -1, 0, 0]
ypos = [1, -1, 0, 0, N, -N]
def bfs():
    q = deque([])
    for i in range(len(ripe)):
        q.append(ripe[i])
    while q:
        xx, yy = q.popleft()
        for i in range(6):
            tmpx = xx + xpos[i]
            tmpy = yy + ypos[i]
            if yy%N == N-1 and tmpy%N == 0:
                continue
            if yy%N == 0 and tmpy%N == N-1:
                continue
            if 0 <= tmpx < M and 0 <= tmpy < N*H and vis[tmpy][tmpx] == INF:
                vis[tmpy][tmpx] = vis[yy][xx] + 1
                q.append((tmpx, tmpy))
    day = 0
    for i in range(N*H):
        for j in range(M):
            if vis[i][j] > day:
                day = vis[i][j]
    if day != INF:
        print(day)
    else:
        print(-1)
ripe = []
for i in range(N*H):
    for j in range(M):
        if graph[i][j] == 1:
            ripe.append((j, i))
            vis[i][j] = 0
        if graph[i][j] == -1:
            vis[i][j] = 0
bfs()