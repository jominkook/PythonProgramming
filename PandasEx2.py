import pandas as pd

# 데이터프레임 생성
data = {'name': ['John', 'Emma', 'Mike'],
        'age': [25, 30, 35],
        'city': ['Seoul', 'New York', 'London']}
df = pd.DataFrame(data)

# 데이터프레임 출력
print(df)

# 열 선택
print(df['name'])

# 행 선택
print(df.loc[0])

# 조건에 따른 행 선택
print(df[df['age'] > 30])