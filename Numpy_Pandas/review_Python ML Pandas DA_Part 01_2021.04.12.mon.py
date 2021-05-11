# coding: utf-8

# 파이썬 머신러닝 판다스 데이터분석
# 
# 
# # Part 1. 판다스 입문
# ## 1. 판다스란?
# - 2008년 금융 데이터 분석용으로 개발되었다. 
# - 오프 소스 커뮤니티를 통해 발전하고 있으며,통계와 데이터 과학, 머신러닝 분야에서 가장 중요한 소프트웨어로 성장하였다. 
# - 파이썬을 기반으로 하며, 데이터를 수집하고 정리하는데 최적화된 도구다.
# - 판다스를 배우면 데이터 과학의 80~90% 업무를 처리할 수 있다.
# 
# 
# ## 2. 판다스 자료 구조
# - 데이터 형식: 구조화된 Series시리즈(1차원 배열)와 DataFrame데이터프레임(2차원 배열)
# - 라이브러리: 여러 종류의 Class(시리즈, 데이터프레임)와 다양한 내장 함수(Series(), DataFrame(), read_csv(), read_excel() 등)으로 구성되어있다.
# - 서로 다른 종류의 데이터를 한 곳에 담는 그릇(컨테이너)이 된다. 
# - 서로 다른 여러 가지 유형의 데이터를 공통의 포맷으로 정리한다.
# - 행과 열로 이루어진 2차원 구조의 데이터프레임은 데이터 분석 실무에서 자주 사용된다.
# 
# ### (1) 시리즈
# - 데이터가 순차적으로 나열된 1차원 배열
# - index와 value가 일대일 대응으로 {k:v} 형태이며, 파이션 딕셔너리와 비슷한 구조다.
# 
# #### - 시리즈 만들기
# - 딕셔너리->시리즈: 시리즈 = pd.Series(딕셔너리)
# 
# ##### 1.1_dict_to_series.py

# In[1]:


# -*- coding: utf-8 -*-

# pandas 불러오기 
import pandas as pd # as pd로 약칭 사용하기

# k:v 구조를 갖는 딕셔너리를 만들고, 변수 dict_data에 저장
dict_data = {'a': 1, 'b': 2, 'c': 3}

# Series() 함수로 딕셔너리(dict_data)를 시리즈로 변환. 변수 sr에 저장 
sr = pd.Series(dict_data)

# 변수 sr의 자료형 출력
print(type(sr))
print('\n') # 한 줄 띄우기

# 변수 sr에 저장되어 있는 시리즈 객체를 출력
print(sr) # 인덱스는 왼쪽, 값은 오른쪾


# #### - 인덱스 구조
# - 인덱스는 자기와 짝을 이루는 데이터의 값의 순서와 주소를 저장한다.
#     - 딕셔너리와 다른 점은, 딕셔너리는 키값으로 접근하는 것에 반해, 시리즈는 인덱스로 접근한다.
# - 인덱스로 데이터 값의 탐색, 정렬, 선택, 결합 등 조작을 할 수 있다.
# - 인덱스의 두 가지 종류
#     - 1) 정수형 위치 인덱스 (0,1,2,...)
#     - 2) 인덱스 이름 또는 인덱스 라벨 (따옴표 필요)
# - 인덱스 배열: 시리즈.index
# - 데이터 값 배열: 시리즈.values
# 
# 
# ##### 1.2_series_index.py

# In[2]:


# 리스트를 시리즈로 변환하여 변수 sr에 저장
# 리스트를 시리즈로 변환할 때는 딕셔너리의 키처럼 인덱스로 변환될 값이 없다. 
# 인덱스를 별도로 정의하지 않으면, 디폴트로 정수형 위치 인덱스가 자동으로 지정된다.
list_data = ['2019-01-02', 3.14, 'ABC', 100, True]
sr = pd.Series(list_data)
print(sr)


# In[3]:


# 인덱스 배열은 변수 idx에 저장. 데이터 값 배열은 변수 val에 저장
idx = sr.index
val = sr.values
print(idx)
print('\n')
print(val)


# #### - 원소 선택
# - 인덱스를 이용하여 시리즈의 원소를 선택한다. 하나 또는 다수를 한꺼번에 선택이 가능하다.
# - 대괄호[] 안에 인덱스를 입력한다.
# 
# 
# ##### 1.3_series_element.py

# In[4]:


# 투플은 한번 묶었으면 변경이 불가능한 특징이 있다.
# 투플을 시리즈로 변환

# 투플은 딕셔너리 키에 해당하는 값이 없기 때문에 정수형 위치 인덱스가 자동 지정된다.
# index 옵션에 인덱스 이름을 지정할 수 있다.
tup_data = ('영인', '2010-05-01', '여', True)
sr = pd.Series(tup_data, index=['이름', '생년월일', '성별', '학생여부'])
print(sr)


# In[5]:


# 원소를 1개 선택
print(sr[0])       # 정수형 위치 인덱스
print('\n') 
print(sr['이름'])  #인덱스 이름 또는 인덱스 라벨


# In[6]:


# 여러 개의 원소를 선택 (인덱스 리스트)
print(sr[[1, 2]]) 
print('\n')           
print(sr[['생년월일', '성별']])


# In[7]:


# 여러 개의 원소를 선택 (인덱스 범위 지정: 슬라이싱)
print(sr[1 : 2])  
print('\n')              
print(sr['생년월일':'성별'])


# ### (2) 데이터프레임
# - 데이터프레임은 행과 열로 만들어지는 2차원 배열이며, R의 데이터프레임에서 유래했다.
# - 데이터프레임의 열은 각각 시리즈 객체이다.
#     - 시리즈를 열벡터라고 하면, 데이터프레임은 여러 개의 열벡터들이 같은 행 인덱스를 기준으로 줄지어 결합된 2차원 백터 또는 행렬이다.
# - 행 인덱스와 열 이름 또는 열 라벨로 구분한다.
#     - 행: __개별 관측대상__ 에 대한 다양한 속성 데이터들의 모음인 __레코드__ (관측값)
#     - 열: 공통의 __속성__ 을 갖는 일련의 데이터. (속성, 범주, 변수)
#     
# 
# #### - 데이터프레임 만들기
# - 원소의 개수가 동일한 1차원의 배열 여러 개(시리즈, 즉 열)을 모아 놓은 집합이다.
# - 딕셔너리->데이터프레임: df = pd.DataFrame(딕셔너리)
# 
# 
# ##### 1.4_dict_to_dataframe.py

# In[8]:


# 열 이름을 key로 하고, 리스트를 value로 갖는 딕셔너리 정의 (2차원 배열)
dict_data = {'c0':[1,2,3], 'c1':[4,5,6], 'c2':[7,8,9], 'c3':[10,11,12], 'c4':[13,14,15]}

# DataFrame() 함수로 딕셔너리를 데이터프레임으로 변환하고 변수 df에 저장
df = pd.DataFrame(dict_data)

# df의 자료형 출력
print(type(df)) 
print('\n')
# 변수 df에 저장되어 있는 데이터프레임 객체를 출력
print(df)


# #### - 행 인덱스 / 열 이름 설정
# - 1) 행 인덱스 / 열 이름 설정: 
#     - df = pd.DataFrame(2차원 배열의 리스트(투플), index=행 인덱스 배열, columns=열 이름 배열)
#     - index, columns 옵션
# 
# 
# ##### 1.5_change_df_idx_col.py

# In[9]:


# 행 인덱스/열 이름 지정하여, 데이터프레임 만들기
df = pd.DataFrame([[15, '남', '덕영중'], [17, '여', '수리중']], 
                   index=['준서', '예은'], # 2행
                   columns=['나이', '성별', '학교']) # 3열

# 행 인덱스, 열 이름 확인하기
print(df)            #데이터프레임
print('\n')
print(df.index)      #행 인덱스
print('\n')
print(df.columns)    #열 이름


# - 2) 새로운 배열 할당하여 행 인덱스와 열 이름 변경:
#     - 행 인덱스 변경: df.index = 새로운 행 인덱스 배열
#     - 열 이름 변경: df.columns = 새로운 열 이름 배열

# In[10]:


# 행 인덱스, 열 이름 변경하기
df.index=['학생1', '학생2']
df.columns=['연령', '남녀', '소속']

print(df)            #데이터프레임
print('\n')
print(df.index)      #행 인덱스
print('\n')
print(df.columns)    #열 이름


# - 3) rename()으로 행 인덱스 또는 열 이름의 일부를 선택하여 변경:
#     - 행 인덱스 변경: df.rename(index = {기존 인덱스:새 인덱스})
#     - 열 이름 변경: df.rename(columns = {기존 이름: 새 이름})
#     
#     
#     - 단, 원본 객체를 직접 수정하는 게 아니라 새 객체를 반환하는 것이므로
#     - 원본 객체 변경하려면 inplace=True 옵션 사용한다. (원본 덮어씌우기, 업그레이드하거나 이 옵션을 씀)
#     
#     
# ##### 1.6_change_df_idx_col2.py

# In[11]:


# 행 인덱스/열 이름 지정하여, 데이터프레임 만들기
df = pd.DataFrame([[15, '남', '덕영중'], [17, '여', '수리중']], 
                   index=['준서', '예은'],
                   columns=['나이', '성별', '학교'])

# 데이터프레임 df 출력
print(df)


# In[12]:


# 열 이름 중, '나이'를 '연령'으로, '성별'을 '남녀'로, '학교'를 '소속'으로 바꾸기
df.rename(columns={'나이':'연령', '성별':'남녀', '학교':'소속'}, inplace=True)

# df의 행 인덱스 중에서, '준서'를 '학생1'로, '예은'을 '학생2'로 바꾸기
df.rename(index={'준서':'학생1', '예은':'학생2' }, inplace=True)

# df 출력(변경 후)
print(df)


# #### - 행 / 열 삭제
# - drop()을 사용하는데, 
#     - 행을 삭제할 때: 옵션 axis = 0 또는 입력x(default가 행 기준)
#     - 열을 삭제할 때: 옵션 axis = 1
#     - 여러 개 삭제할 때: 리스트 형태로 입력
#     - 원본 객체를 직접 변경할 때: inplace=True 옵션 추가(False면 새로운 객체 생성, 원 객체는 유지)
#     
#     
#     - 행 삭제: df.drop(행 인덱스 또는 배열, axis=0)
#     - 열 삭제: df.drop(열 이름 또는 배열, axis=1)
#     
#     
# ##### 1.7_remove_row.py

# In[14]:


# 오류(SettingWithCopyError 발생)
pd.set_option('mode.chained_assignment', 'raise') # SettingWithCopyError

# 경고(SettingWithCopyWarning 발생, 기본 값입니다)
pd.set_option('mode.chained_assignment', 'warn') # SettingWithCopyWarning

# 무시
pd.set_option('mode.chained_assignment',  None) # <==== 경고를 끈다


# In[15]:


# DataFrame() 함수로 데이터프레임 변환. 변수 df에 저장 
exam_data = {'수학' : [ 90, 80, 70], '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100], '체육' : [ 100, 90, 90]}

df = pd.DataFrame(exam_data, index=['서준', '우현', '인아'])
print(df)
print('\n')

# 데이터프레임 df를 복제[:]하여 변수 df2에 저장. df2의 1개 행(row)을 삭제
df2 = df[:]
df2.drop('우현', inplace=True)
print(df2)
print('\n')

# 데이터프레임 df를 복제하여 변수 df3에 저장. df3의 2개 행(row)을 삭제
df3 = df[:]
df3.drop(['우현', '인아'], axis=0, inplace=True)
print(df3)


# ##### 1.8_remove_column.py

# In[16]:


# DataFrame() 함수로 데이터프레임 변환. 변수 df에 저장 
exam_data = {'수학' : [ 90, 80, 70], '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100], '체육' : [ 100, 90, 90]}

df = pd.DataFrame(exam_data, index=['서준', '우현', '인아'])
print(df)
print('\n')

# 데이터프레임 df를 복제하여 변수 df4에 저장. df4의 1개 열(column)을 삭제
df4 = df[:]
df4.drop('수학', axis=1, inplace=True)
print(df4)
print('\n')

# 데이터프레임 df를 복제하여 변수 df5에 저장. df5의 2개 열(column)을 삭제
df5 = df[:]
df5.drop(['영어', '음악'], axis=1, inplace=True)
print(df5)


# --- seYi
