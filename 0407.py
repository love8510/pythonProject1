import numpy as np
"""
def solution(numbers):
    answer = []
    answer = np.array(numbers)*2
    answer = answer.tolist()
    return answer



arr_test = np.array(
    [1, 2, 3, 4, 5]  # 1차 array
)

list_test = arr_test.tolist()

print(arr_test)
print(list_test)

-- Result
[1 2 3 4 5]

[1, 2, 3, 4, 5]





def solution(strings, n):
    new =[]
    answer =[]
    for i in range(len(strings)):
        a = strings[i][n]
        print(a)
        b = a+strings[i]
        new.append(b)
    new.sort()
    for i in range(len(new)):
        print(new)
        c = new[i][1:]
        print(c)
        answer.append(c)
    return answer

def solution2(strings, n):
    new =[]
    answer =[]
    for string in strings:
        answer.append(string[n])

    answer.sort()

    for i in answer:
        for string in strings:
            if string[n]==i:
                print(string)
                answer.append(string)

    return answer



array = ["sun","bed","car"]
solution2(array,1)



def solution(arr1,arr2):
    answer = []
    for a in range(0,len(arr1)):
        for b in range(0,len(arr1[a])):
           arr1[a][b] += arr2[a][b]
    answer.append(arr1)
    return answer


def solution2(arr1,arr2):
    answer = []
    for i in range(0,len(arr1)):
        answer.append(arr1[i]+arr2[i])
        return answer


def solution3(arr1,arr2):
    answer = []
    for i in range(len(arr1)):
        row=[]
        for j in range(arr1[0]):
            row.append(arr1[i][j]+arr2[i][j])
    return row
arr1 = [[1,2],[2,3]]
arr2 = [[3,4],[5,6]]
print(solution(arr1,arr2))
"""

def solution(arr):
    answer = []
    for a in range(0,len(arr)):
        if arr[a] == arr[a+1]:
            continue
        else:
            answer.append(arr[a])
    return answer

def solution2(arr):
    answer = [arr[0]]
    for a in arr:
        if not a == answer[-1]:
            answer.append(a)
    return answer


def solution3(arr):
    answer = []
    for i in arr:
        if answer[-1:] != [i]:
            answer.append(i)
    return answer

def solution4(arr):
    answer = set(arr)
    return answer



def solution4(arr):
    answer = []
    for i in range(0,len(arr)):
        if i !=0 and arr[i]==answer[-1]:
            continue
        else:
            answer.append(arr[i])
    return answer

def solution6(arr): #강한솔
    answer = []
    before_ = 0
    for item in arr:
        if len(answer)==0:
            before_ = item
            answer.append(item)
            continue
        if item == before_:
            continue
        else:
            answer.append(item)
            before_ = item
            continue
    return answer


def solution7(arr):
    num = []
    answer = []
    for i in range(len(arr)):
        if i==0 or arr[i]!=arr[i-1]:
            num.append(i)
    for k in range(len(num)):
        answer.append(arr[num[k]])

    return answer


def solution9(arr):
    answer = []
    for i in range(len(arr)):
        if i ==0:
            answer.append(int(arr[i]))
        elif arr[i] != arr[i-1]:
            answer.append(int[arr[i]])
    return answer

def solution10(arr):
    answer = [ ]
    for num in arr:
        if not answer or answer[-1] !=num:
            answer.append(num)
    return answer

arr = [1,1,3,3,0,1,1]
print(solution10(arr))
