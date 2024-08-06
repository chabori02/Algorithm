for i in range(int(input())):
    a,b = input().split()
    list1 = [[1], [2, 4, 8, 6], [3, 9, 7, 1], [4, 6], [5], [6], [7, 9, 3, 1], [8, 4, 2, 6], [9, 1], [0]]
    com = list1[(int(a) % 10) - 1][int(b) % len(list1[int(a) % 10 - 1])-1]
    if(com == 0):
        print(10)
    else:
        print(com)