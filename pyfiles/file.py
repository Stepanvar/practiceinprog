A = (1,2,3)
B = list(A)
B[0] = 20
print(B)
list1 = [10, 30, 7]
list2 = list1
list3 = list(list1)
list4 = list1.copy()
list2[2] = 40
print(list1, list2, list3, list4)
list1.append(70)
print(list1, list2, list3, list4)
list1 = list1 * 2
print(list1, list2, list3, list4)
B = [x+2 for x in A if x % 2 == 0]
def create_login(name):
    name = list(name)
