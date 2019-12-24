from queue import Queue


N, M = map(lambda x: int(x), input().split(' '))
S, E = map(lambda x: int(x), input().split(' '))
neighbers = [[] for x in range(0, N+1)]
for i in range(0, M):
    p1, p2 = map(lambda x: int(x), input().split(' '))
    neighbers[p1].append(p2)
    neighbers[p2].append(p1)

# Make it a complete graph.
neighbers[1].append(2)
neighbers[N].append(N-1)
neighbers = [x + [i-1, i+1] if i >= 2 and i <= N-1 else x for i, x in enumerate(neighbers)]

q = Queue()
q.put(S)

dist = [-1 for x in range(0, N + 1)]
dist[S] = 0

while not q.empty():
    current = q.get()
    for neighber in neighbers[current]:
        if dist[neighber] == -1:
            dist[neighber] = dist[current] + 1
            q.put(neighber)

print(dist[E])
