N, M = list(map(lambda x: int(x), input().split(' ')))

neighbers = [[] for x in range(0, N+1)]
for i in range(0, M):
    city1, city2 = list(map(lambda x: int(x), input().split(' ')))
    neighbers[city1].append(city2)
    neighbers[city2].append(city1)

n_destroyed = int(input())
destroyed = list(map(lambda x: int(x), input().split(' ')))

bombed = []
for city in destroyed:
    neighbers_of_this_city = neighbers[city]
    neighbers_all_destroyed = False not in [x in destroyed for x in neighbers_of_this_city]

    if neighbers_all_destroyed:
        bombed.append(city)

should_have_been_destroyed = []
for city in bombed:
    should_have_been_destroyed.extend(neighbers[city] + [city])

if False in [x in should_have_been_destroyed for x in destroyed]:
    bombed.clear()

if len(bombed) == 0:
    print(-1)
else:
    print(len(bombed))
    bombed.sort()
    for city in bombed:
        print(city, end=' ')
