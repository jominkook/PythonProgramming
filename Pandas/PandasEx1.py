import pandas as pd
import numpy as np

# 시리즈 생성
s = pd.Series([1, 3, 5, np.nan, 6, 8])

# 시리즈 출력
print(s)

# 시리즈 인덱스 출력
print(s.index)

# 시리즈 값 출력
print(s.values)