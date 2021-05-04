#!/usr/bin/env python
# coding: utf-8

# # 시저 암호

# ### 문제 설명
# - 어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화 방식을 시저 암호라고 합니다. 예를 들어 "AB"는 1만큼 밀면 "BC"가 되고, 3만큼 밀면 "DE"가 됩니다. "z"는 1만큼 밀면 "a"가 됩니다. 문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 만드는 함수, solution을 완성해 보세요.

# ### 제한 조건
# - 공백은 아무리 밀어도 공백입니다.
# - s는 알파벳 소문자, 대문자, 공백으로만 이루어져 있습니다.
# - s의 길이는 8000이하입니다.
# - n은 1 이상, 25이하인 자연수입니다.

# ### 입출력 예
# |s|n|result|
# |-----|---|---|
# |"AB"|1|"BC"|
# |"z"|1|"a"|
# |"a B z"|4|"e F d"|

# ### 나의 풀이:
# - 세 부분으로 나누자 생각했다. 소문자, 대문자, 공백
# - 구분이 쉽게 소문자 문자열과 대문자 문자열을 나눠 저장하고
# - 세 부분으로 나눠 코드를 입력했다.
# - 문자열 인덱스를 .index() 함수로 찾고 n만큼 더해줘서 인덱스에 저장했다.
# - 소/대문자 문자열에서 인덱스를 26으로 나눈 나머지를 위치로 지정해 답안에 저장했다.

# In[1]:


def solution(s, n):
    answer = ''

    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = lower.upper()

    for alphabet in s:

        if alphabet in lower:
            idx = lower.index(alphabet) + n
            answer += lower[idx % 26]

        elif alphabet in upper:
            idx = upper.index(alphabet) + n
            answer += upper[idx % 26]

        else:
            answer += " "

    return answer


# In[2]:


solution("AB", 1)


# --- seYI
