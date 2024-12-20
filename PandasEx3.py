import numpy as np
import pandas as pd

col_name2 = ['col1', 'col2', 'col3']
list2 = [[1, 2, 3], [11, 12, 13]]
arr2 = np.array(list2)
print('arr2.shape:', arr2.shape)
df_list2 = pd.DataFrame(list2, columns=col_name2)
print('2차원 리스트로 만든 DataFrame:\n', df_list2)
df_arr2 = pd.DataFrame(arr2, columns=col_name2)
print('2차원 ndarray로 만든 DataFrame:\n', df_arr2)