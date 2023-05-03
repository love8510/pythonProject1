"""
1번 문제 해답
정수 배열 numbers와 정수 num1, num2가 매개변수로 주어질 때, numbers의 num1번 째 인덱스부터 num2번째 인덱스까지
자른 정수 배열을 return 하도록 solution 함수를 완성해보세요.


def solution5(numbers, num1, num2):
    answer = []
    for i in range(len(numbers)):
        if i == num1:
            for x in range(num1, num2 +1):
                answer.append(numbers[x])
    return answer




def solution10(numbers, num1, num2):
    answer = []
    for i in numbers:
        answer.append(i)

    answer = answer[num1:num2+1]
    return answer

print(solution10([1, 2, 3, 4, 5],1,3))
print(solution5([1, 3, 5],1,2))



2번 문제 해답
두 배열이 얼마나 유사한지 확인해보려고 합니다. 문자열 배열 s1과 s2가
 주어질 때 같은 원소의 개수를 return하도록 solution 함수를 완성해주세요.




def solution(s1, s2):
    return len(set(s1)&set(s2));

solution(["a","b","c"],["com","b","p","c"])

def solution(s1, s2):
    answer = 0
    for i in range(len(s1)) :
        for j in range(len(s2)) :
            if s1[i] == s2[j] :
                answer += 1
    return answer

solution(["a","b","c"],["com","b","p","c"])
"""


def soulution(id_pw,db):

    answer = ""
    for list in db:

        if id_pw == list:
            answer = "login"
    return answer

def soulution2(id_pw,db):

    answer = ""
    for i in range(len(db)):
        if db[i]==id_pw:
            answer = "login"

    return answer




print(soulution(["meosseugi","1234"],[["meosseugi","1234"],["yyoom","12334"]]))
print(soulution2(["meosseugi","1234"],[["meosseugi","1234"],["yyoom","12334"]]))