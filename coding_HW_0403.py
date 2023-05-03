"""
문제 1_배열 뒤집기

정수가 들어있는 배열 num_list 가 매개변수로 주어집니다.
num_list 의 원소의 순서를 거꾸로 뒤집은 배열은 return 하도록  solution 함수를 완성하세요.



#1번예시
def solution(num_list): #함수를 실행한다.
    answer = []
    return list(reversed(num_list))

#2번예시
def solution(num_list):
    answer = []
    answer = num_list.copy()
    answer.reverse()
    return answer

#3번 예시
def solution(num_list):
    answer = []
    for n in reversed(num_list):
        answer.append(n)
    return answer

#4번 예시
def solution2(num_list):
    answer = []
    print(len(num_list))
    for i in range(1,len(num_list)+1):
        answer.append(num_list[len(num_list) - i])
    return answer



num_list = [1,2,3,4,5]  #변수를 선언하고 배열을 입력한다.
num_list = solution2(num_list)  #solution 함수를 호출한다.
print(num_list)



문제2) 양꼬치 가격 계산하기 
머쑥이네 양꼬치 가게는 10인분을 먹으면 음료수 하나를 서비스로 줍니다. 
양꼬치는 1인분에 12000원 음료수는 2000원 입니다. 
정수 n 과 정수 k 가 매개변수로 주어졌을때, 양꼬치 n인분과 음료수 K를 먹었다면 
총얼마를 지불하야 하는지 return 하도록 solution 함수를 완성하세요)

입출력 예시 : 
10인분을 시켜 서비스로 음료수를 하나 받아 총 10(양꼬치갯수:n) * 12000원 + 3(음료수갯수:k) *2000
 - 1 (서비스 콜라)*2000 = 124000원입니다. 


def solution(n, k):
    return 12000 * n + 2000 * (k - n // 10)

def solution(n, k):
    answer = n * 12000 + k * 2000 - int(n/10) *2000

def solution(n, k):
    return n * 12000 + (k - n // 10) * 2000

solution(10,3)


"""


for i in range(4,5):
    print(i)