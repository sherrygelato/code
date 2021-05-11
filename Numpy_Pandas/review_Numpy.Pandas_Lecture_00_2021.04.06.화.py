#!/usr/bin/env python
# coding: utf-8

# numpy.pdf
# 
# 
# # [Numpy] 01. Numpy(넘파이) 란?
# 
# 
# ## 1. Numpy(넘파이) 란?
# - 고성능의 수치 계산을 하기 위해 만들어진 Python(파이썬)의 핵심 라이브러리다.
# - 다차원 배열을 효과적으로 다루기 위해 ndarray를 사용한다.
# - 벡터화 연산을 지원하기 때문에 반복문을 사용하지 않고도 배열의 모든 원소에 대해 반복 연산이 가능하다.
# - 브로드캐스팅을 지원하기 때문에 배열 간 연산을 하는데 배열의 크기가 서로 다르더라도 크기가 작은 배열을 자동으로 반복 확장하여 크기가 큰 배열에 맞추어 연산이 가능하다.
# 
#  
# ## 2. ndarray 란?
# - N-Dimesional Array
# - 차원(ndim), 자료형(dtype), 모양(shape), 크기(size) 등 멤버 변수를 포함한다.
# 
# 
# - ndarray의 차원은 1차원(1D), 2차원(2D), ... n차원(nD) 등
# - 일반적으로 1차원~ 4차원까지 많이 사용한다.
# - ndarray.ndim 변수로 차원을 확인한다.
# - 예) 1차원의 배열(행), 2행 3열, 2채널의 4행 2열, 3묶음(?)의 2채널의 4행 2열

# In[1]:


import numpy as np # numpy 모듈 불러오기


# In[2]:


nd1 = np.array([1,2,3,4]) # ndarray 생성
nd1


# In[3]:


nd1.ndim    # ndim: 차원


# In[4]:


type(nd1) # 타입 확인


# In[5]:


nd2 = np.array([[1,2,3],[4,5,6]]) # 리스트 안의 리스트 (리스트 내포)
nd2 # 출력 시 행과 열 구조라고 보여줌


# In[6]:


nd2.ndim # number of dimension


# In[7]:


type(nd1)


# In[8]:


type(nd2)


# In[9]:


nd3 = np.array([[[1, 2, 3, 4],
               [5, 6, 7, 8],
               [9, 10, 11, 12]],
              [[11, 12, 13, 14],
               [15, 16, 17, 18],
               [19, 20, 21, 22]]])
# 실제 인덱스 [채널, 행, 열]


# In[10]:


print(nd3)


# In[11]:


nd4 = np.array([[[[1,2], [3,4]],
                 [[5,6],[7,8]]],
                [[[9,10],[11,12]],
                 [[13,14],[15,16]]],
                [[[17,18],[19,20]],
                 [[21,22],[23,24]]]])
nd4
# 인덱스 [묶음, 채널, 행, 열]


# In[12]:


nd4.ndim


# #### 자료형
# - 넘파이의 배열, ndarray는 원소가 모두 같은 자료형이어야 한다. 
# - 열을 만들 때 자료형을 명시적으로 적용하려면 dtype 옵션을 사용한다. 
# - dtype 지정을 하지 않으면, 주어진 데이터를 저장할 수 있는 자료형을 스스로 유추한다.
# - Boolean(dtype=bool), int, float, datatime, timedelta(날짜 차이), str, object
# 
# 
# - ndarray 자료형 확인: print(nd1.dtype)
# - ndarray 자료형 형변환 : nd1 = nd1.astype(np.int32)
# - ndarray 자료형 할당

# In[13]:


nd5 = np.array([1.0, 2.1, 3.0, 4.2]) # float64로 default 할당
print(nd5.dtype) # 자료형 확인


# In[14]:


nd6 = np.array([[1, 2, 3], [4, 5, 6]]) # int32로 default 할당
print(nd6.dtype)


# In[15]:


nd7 = np.array([[1, 2, 3], [4, 5, 6]], dtype = np.float32)
print(nd7.dtype)


# In[16]:


nd8 = np.array([[1, 2, 3], [4, 5, 6]], dtype = 'float64')
print(nd8.dtype)


# In[17]:


# 자료형 형변환
nd5 = nd5.astype(np.int32)
print(nd5.dtype)


# ## 3. ndarrya의 모양: shape
# - 머신러닝/딥러닝에서 *입력 데이터의 shape를 맞추고 확인하는 과정*은 매우 중요하다. 
# - ndarray.shape 변수를 이용하여 shape를 확인하고 결과는 튜플(,)로 나온다.
# - 예) 1차원: (4,), 2차원: (2, 3), 3차원: (2, 4, 3), 4차원: (3, 2, 2, 2)

# In[18]:


nd1.shape # (4,1)의 생략임


# In[19]:


nd2.shape


# ## 4. ndarray의 크기: size
# - ndarray.size 변수로 전체 크기(모든 원수의 갯수)를 알 수 있다.
# - size: 모든 원소의 갯수이며 shape의 모든 값을 곱한 값
# - 예) (4,)의 size: 4, (2, 3)의 size: 6, (2, 4, 3)의 size: 24, (3, 2, 2, 2)의 size: 24

# In[20]:


nd2.size


# In[21]:


nd1.size


# ## 5. ndarray의 reshape
# - 입력데이터의 shape이 불일치한 경우, 이를 맞추기 위해 reshape 해준다.
# - 동일 차원 내 변환 및 이종 차원간 변환이 가능한데, 즉 ndarray의 size가 동일해야 reshape이 가능하다는 소리다.

# ## 6. ndarray의 기타 함수
# - np.zeros(shape) : shape의 모양대로 0으로 채운 ndarray 생성
# - np.ones(shape) : shape의 모양대로 1으로 채운 ndarray 생성
# - np.arange(start, stop, step) : 파이썬 range 함수와 동일

# In[22]:


np.zeros((4,3)) # output: 실수 표현하기에 .이 있는 것


# In[23]:


a = np.ones((3,4))
a


# In[24]:


a.size


# In[25]:


np.arange(12)


# In[26]:


np.arange(1, 10, 2)


# In[27]:


np.arange(0, 10, 2)


# In[28]:


np.arange(12).reshape(4,3)


# In[29]:


np.arange(12).reshape(4,-1) # 끝자리를 알아서 정리해줌


# In[30]:


np.arange(12).reshape(1,-1)


# In[32]:


np.arange(1200).reshape(3, -1)


# ## 7. ndarray의 벡터화 연산
# - 같은 위치의 값끼리 반복 연산(+, -, x, /) 가능하다.
# 
# 
# ## 8. ndarray의 브로드캐스팅
# - 연산이 가능한 형태로 reshape한 후 반복된 값으로 자동으로 할당하여 연산한다.

# In[33]:


# 브로드캐스팅 연산
x = np.arange(5)
x


# In[34]:


x + 1


# In[35]:


# 위와 비교할 것
x = np.arange(5)
y = np.ones_like(x)
y


# In[36]:


x + y


# 참고: [데이터 사이언스 스쿨 파이썬 편](https://datascienceschool.net/01%20python/00.00%20%EC%86%8C%EA%B0%9C%EC%9D%98%20%EA%B8%80.html)

# --- seYi
