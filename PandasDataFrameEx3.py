import pandas as pd
import numpy as np

# 데이터프레임 로드
titanic_df = pd.read_csv(r'C:\Users\whaks\Desktop\PythonProgram\titanic.csv')

titanic_df['Age_0'] = 0
#새로 만들어진 Age_0 컬럼에 모두 0을 입력
titanic_df.head(3)
print(titanic_df.head(3))

#'Age'열의 value값들이 10배가 되어 새로운 Age_by_10 컬럼에 입력
titanic_df['Age_by_10'] = titanic_df['User_ID']*10

#1의 방식과 2의 방식을 종합하여 새로운 열을 생성한다
titanic_df['Family_No'] = titanic_df['Likes'] + titanic_df['Shares'] + 1

titanic_df.head(3)
print(titanic_df.head(3))