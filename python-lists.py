if __name__ == '__main__':
    N = int(input())
    arr = []
    my_commands = {'insert': lambda index,value: arr.insert(index,value), 'print':lambda : print(arr), 'remove':lambda value: arr.remove(value),'reverse':lambda : arr.reverse(),'pop': lambda : arr.pop(),'append':lambda value: arr.append(value), 'sort': lambda: arr.sort()}
    for _ in range(N):
        command = input().split()
        if len(command) == 1:
            my_commands[command[0]]()
        elif len(command) == 2:
            my_commands[command[0]](int(command[1]))
        elif len(command) == 3:
            my_commands[command[0]](int(command[1]), int(command[2]))
            
        
