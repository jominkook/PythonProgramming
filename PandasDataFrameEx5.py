#데이터 평균 최고값 구하기

import pandas as pd

data = pd.read_csv(r'C:\Users\whaks\Desktop\PythonProgram\weather_data.csv')

#csv파일을 딕셔너리로 변형하기
data_dict = data.to_dict()

#변경한 딕셔너리로 파일의 한 열을 리스트로 변경해서 호출하기
temp_list = data['temp'].to_list()


#평균구하기
print(sum(temp_list)/len(temp_list))
#평균구하기2
print(data['temp'].mean())

#최고값 구하기
print(data['temp'].max())

#주에서 가장 온도가 높았던 날짜 구하기
print(data[data.temp == data.temp.max()])

#월요일 값 가져오기
monday = data[data.day == 'Monday']
monday_temp = int(monday.temp)
print(monday_temp)
monday_f = monday_temp * 9/5 + 32 #섭씨를 화씨로 변환
print("화씨온도:", monday_f,"F")