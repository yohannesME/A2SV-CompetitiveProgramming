if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        students.append([input(), float(input())])
    
    students.sort(key=lambda x:x[1])
    lowest = students[0][1]
    for name, score in students:
        if score > lowest:
            secondLowest = score
            break
      
    output = []
    for name,score in students:
        if score == secondLowest:
            output.append(name)
        if score > secondLowest:
            break
    for name in sorted(output):
        print(name)
