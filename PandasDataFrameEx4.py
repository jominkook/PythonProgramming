import pandas as pd

data = pd.read_csv(r'C:\Users\whaks\Desktop\PythonProgram\2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20241227.csv')

#회색 다람쥐 마릿수 찾아보기
gray_squirrels = len(data[data['Primary Fur Color'] == 'Gray'])
red_squirrels = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_squirrels = len(data[data['Primary Fur Color'] == 'Black'])

#출력
# print(gray_squirrels)
# print(red_squirrels)
# print(black_squirrels)

#다람쥐의 색깔별로 데이터프레임 만들기
squirrel_color = data['Primary Fur Color'].value_counts()
squirrel_color_df = squirrel_color.reset_index()

#출력
# print(squirrel_color_df)

#다람쥐의 색과 갯수를 딕셔너리로 만들기
data_dict = {
    'Fur_color': ['Gray', 'Cinnamon', 'Black'],
    'Count': [gray_squirrels, red_squirrels, black_squirrels]
}

#csv파일로 저장하여 만들기
df = pd.DataFrame(data_dict)
df.to_csv(r'C:\Users\whaks\Desktop\PythonProgram\squirrel_count.csv', index=False)