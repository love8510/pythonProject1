"""
# 해시
문제 설명
수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.

마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

제한사항
마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
completion의 길이는 participant의 길이보다 1 작습니다.
참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
참가자 중에는 동명이인이 있을 수 있습니다.

예시 1)
잆력값 : participant-> ["leo", "kiki", "eden"] ->  completion -> 	["eden", "kiki"]
-------------------------------------------------------------------------------------------------------
출력값 : leo

예시 2)

잆력값 : participant-> ["mislav", "stanko", "mislav", "ana"] ->  completion -> 	["stanko", "ana", "mislav"]
-------------------------------------------------------------------------------------------------------
출력값 : mislav


def solution(participant, completion):
    answer = ''
    for()
    return answer

hash_1 = list()
solution(["leo", "kiki", "eden"],["eden", "kiki"])

"""
hash_table = list([0 for i in range(8)])

print(hash_table)

def get_key(data):
    return hash(data)


def hash_function(key):
    return key % 8


def save_data_hash_table(data, value):
    hash_address = hash_function(get_key(data))
    hash_table[hash_address] = value


def get_data_hash_table(data):
    hash_address = hash_function(get_key(data))
    return hash_table[hash_address]


save_data_hash_table('Dave', '01032312332')
save_data_hash_table('David', '01032221111')
print(get_data_hash_table('Dave'))








