#input student count and id of both count and subscription
englishStudentCount = int(input())

englishStudent = set(map(int, input().split()))

frenchStudentCount = int(input())

frenchStudent = set(map(int, input().split()))


sizeofatLeastOne =len(englishStudent.union(frenchStudent))
print(sizeofatLeastOne)
