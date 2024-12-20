import pandas as pd
import numpy as np

dict = {'col1':[1, 11], 'col2':[2, 22], 'col3':[3, 33]}
df_dict = pd.DataFrame(dict)
print('딕셔너리로 만든 DataFrame:\n', df_dict)

arr3 = df_dict.values
print('df_dict.values 타입:', type(arr3), 'df_dict.values shape:', arr3.shape)
print(arr3)