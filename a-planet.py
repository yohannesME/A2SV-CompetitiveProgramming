from collections import Counter

# the test cases that are inputed
testcase = int(input())

#the planets there orbits
planets = []

#answer the number of minimum cost destruction
minimumDestruction = 0

#input the planets
for _ in range(testcase):
    n,c = list(map(int, input().split(' ')))
    planets.append([list(map(int, input().split(' '))),c])


for planet,c in planets:
    planet = Counter(planet)
    for value in planet.values():
        if value > c:
            minimumDestruction += c
        else:
            minimumDestruction += value
    print(minimumDestruction)
    minimumDestruction = 0

