#input student count and id of both english and french student subscriptions
englishStudentCount = int(input())

englishStudent = set(map(int, input().split()))

frenchStudentCount = int(input())

frenchStudent = set(map(int, input().split()))


sizeofCommon =len(englishStudent.difference(frenchStudent))
print(sizeofCommon)
