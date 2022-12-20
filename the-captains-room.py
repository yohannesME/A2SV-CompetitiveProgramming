import collections

k = input()
roomList = input().split(' ')
roomList = [int(room) for room in roomList]
guest = collections.Counter(roomList)

for key in guest.keys():
    if guest[key] == 1:
        print(key)
