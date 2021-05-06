#!/usr/bin/env python
# coding: utf-8

# # # 약수의 합https://programmers.co.kr/learn/courses/30/lessons/12928

# ### 문제 설명
# 정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.

# ### 제한 사항
# n은 0 이상 3000이하인 정수입니다.

# #### 입출력 예 #1
# 12의 약수는 1, 2, 3, 4, 6, 12입니다. 이를 모두 더하면 28입니다.
# 
# 
# #### 입출력 예 #2
# 5의 약수는 1, 5입니다. 이를 모두 더하면 6입니다.

# ### 나의 풀이
# - 1) 1부터 n까지의 수를 만들고
# - 2) 약수를 찾고
# - 3) 약수값 더하고
# - 4) 이 코드를 간단화 했다.

# In[1]:


# 1) ~ 3) 코드 실행 및  확인

def solution(n):
    answer = 0 # 초깃값
    
    for i in range(1, n+1): # 1부터 n까지의 수
        if n % i == 0: # 약수 찾기
            answer += i # 약수 값 더하기
            
    return answer


# In[2]:


solution(12)


# In[3]:


solution(5)


# In[4]:


# 4) 코드 간단화 하기

def solution(n):
    return sum([i for i in range(1, n + 1) if n % i == 0 ])


# In[5]:


solution(12)


# In[6]:


solution(5)


# --- seYi
