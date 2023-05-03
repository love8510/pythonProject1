def solution(phone_book):
    phone_book.sort()
    answer = True
    for i in range(len(phone_book)-1):
         if phone_book[i]==phone_book[i+1][0:len(phone_book[i])]:
            answer = False
            break
    return answer

def solution2(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)):
        if len(phone_book[i])==len(phone_book(i+1)):
            answer = False
    return answer

def solution3(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        print(phone_book[i])
        print(phone_book[i+1][:len(phone_book[i])])
        if phone_book[i]==phone_book[i+1][:len(phone_book[i])]:
            answer = False
            break
        print("###########")
    return answer


def solution4(phone_book):
    answer = phone_book.sort()
    answer = True
    for i in range(len(phone_book)-1):
        if phone_book[i+1].stratswith(phone_book[i]):
            answer = False
    return answer

def solution5(phone_book):
    answer = True
    for i in range(0,len(phone_book)):
        for j in range(0,len(phone_book)):
            if i !=j and phone_book[i] in phone_book[j]:
                answer = False
    return answer
"""
def solution6(phone_book):
    answer = True
    for a in range(0,len(phone_book)):
        for b in range(0,len(phone_book)):
            print(a)
            print(b)
            if a==b:
                continue

            for c in range(phone_book(a)):
            if phone_book[a][c]!= phone_book[b][c]:
            answer = False
            return answer

def solution7(phone_book):
    answer = True
    for item in phone_book:
        for camp in phone_book:
            if camp in phone_book:
                continue
            for i in range(len(item)):
                print(item[i])
                if item[i]==camp[i]:
                    answer = False
                else:
                    answer = True
    return answer

def solution9(phone_book):
    answer = True

    for i in range(len(phone_book)):
        for j in range(i+1,len(phone_book)):
            if phone_book[i].startswith(phone_book[j]) or phone_book[j].startswith(phone_book[i]):
                return False

    return answer


arr = ["97674223", "119","1195524421"]
arr2 = ["123","456","789"]
arr3 = ["12","123","1235","567","88"]
print(solution7(arr))

def solution1(absolutes,signs):
    answer = 0
    for i in range(len(absolutes)):
        if signs[i]:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    return answer

absolutes = [4,7,12]
signs = [True,False,True]

print(solution1(absolutes,signs))

def solution1(numbers):

    answer = 0
    n = len(numbers)

    for i in range(n-2):
        print(i)
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                #print(numbers[i] + numbers[j] + numbers[k])
                if numbers[i] + numbers[j] + numbers[k]==0:
                    answer += 1
    return answer


"""


def solution1(numbers):
    answer = 0
    for i in range(10):
        for k in range(len(numbers)):
            if i == numbers[k]:
                break
            if k == len(numbers)-1:
                answer += i

    return answer

arr = [5,8,4,0,6,7,9]
print(solution1(arr))
