def countingValleys(steps, path):
    count = 0
    depth = 0
    for step in range(steps):
        if path[step] == 'U':
            depth+=1
        elif path[step] == 'D':
            depth-=1
            if depth==-1:
                count+= 1
    return count
