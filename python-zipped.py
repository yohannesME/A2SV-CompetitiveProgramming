#input the amount of subject and student respectively
N, X = list(map(int, input().split()))

#the grades of all the students
grades = []
for _ in range(X):
    grades.append(list(map(float, input().split())))

#select the each student grade and calculate score
for grade in zip(*grades):
    #display the average
    print(sum(grade)/X)
