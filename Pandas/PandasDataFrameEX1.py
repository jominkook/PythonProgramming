import pandas as pd
import numpy as np

# 데이터프레임 로드
titanic_df = pd.read_csv(r'C:\Users\whaks\Desktop\PythonProgram\titanic.csv')

# 데이터프레임의 처음 3개 행 출력
print(titanic_df.head(3))

# 데이터프레임의 마지막 3개 행 출력
print(titanic_df.tail(3))

# 'Pclass' 열의 값 개수 세기
value_cnt = titanic_df['User_ID'].value_counts()

# 값 개수 출력
print(type(value_cnt))
print(value_cnt)

