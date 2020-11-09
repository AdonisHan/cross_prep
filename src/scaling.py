import pandas as pd
import glob
import os
import seaborn as sns
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'NanumGothic'
from scipy.stats import probplot
import scipy.stats as stats
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import MinMaxScaler
rawData = pd.read_csv(...)

hdata_mn = hdata
mmsscaler = MinMaxScaler()
df1 = pd.DataFrame(hdata_mn.loc[:,'행정동'],columns=['행정동'])
df2 = pd.DataFrame(mmsscaler.fit_transform(hdata_mn.loc[:,'보행등' : '사고건수']))
hdata_mn_scaling = pd.concat([df1,df2],axis = 1)
print(hdata_mn_scaling)

# Z-socre 정규화
from sklearn.preprocessing import StandardScaler
hdata_z = hdata
stdscaler = StandardScaler()
df1 = pd.DataFrame(hdata_z.loc[:,'행정동'],columns=['행정동'])
df2 = pd.DataFrame(stdscaler.fit_transform(hdata_mn.loc[:,'보행등' : '사고건수']))
hdata_z_scaling = pd.concat([df1,df2],axis = 1)

print(hdata_z_scaling)

hdata_z_scaling.to_csv("C:/Users/user/Documents/횡단보도/hdata_z_scaling.csv",header=False,index=False, encoding='cp949')

hdata_dec = hdata
# 소수척도화
max_보행등 = max(hdata_dec.loc[:, '보행등'])
min_보행등 = min(hdata_dec.loc[:, '보행등'])

max_보행자작동신호기 = max(hdata_dec.loc[:, '보행자작동신호기'])
min_보행자작동신호기 = min(hdata_dec.loc[:, '보행자작동신호기'])

max_잔여시간표시기 = max(hdata_dec.loc[:, '잔여시간표시기'])
min_잔여시간표시기 = min(hdata_dec.loc[:, '잔여시간표시기'])

max_보행노인사고다발지역 = max(hdata_dec.loc[:, '보행노인사고다발지역'])
min_보행노인사고다발지역 = min(hdata_dec.loc[:, '보행노인사고다발지역'])

max_노인인구수 = max(hdata_dec.loc[:, '노인인구수'])
min_노인인구수 = min(hdata_dec.loc[:, '노인인구수'])

max_노인보호구역 = max(hdata_dec.loc[:, '노인보호구역'])
min_노인보호구역 = min(hdata_dec.loc[:, '노인보호구역'])

max_사고건수 = max(hdata_dec.loc[:, '사고건수'])
min_사고건수 = min(hdata_dec.loc[:, '사고건수'])

# 소수 척도화 수행
list_of_decs = []
# 행정동	보행등	보행자작동신호기	잔여시간표시기	보행노인사고다발지역	노인인구수	노인보호구역	사고건수

for i in range(0, len(hdata_dec)):
	list_of_decs.append(
[
hdata_dec.loc[i, '행정동'],
hdata_dec.loc[i, '보행등'] / pow(10, len(str(max_보행등))),
hdata_dec.loc[i, '보행자작동신호기'] / pow(10, len(str(max_보행자작동신호기))),
hdata_dec.loc[i, '잔여시간표시기'] / pow(10, len(str(max_잔여시간표시기))),
hdata_dec.loc[i, '보행노인사고다발지역'] / pow(10, len(str(max_보행노인사고다발지역))),
hdata_dec.loc[i, '노인인구수'] / pow(10, len(str(max_노인인구수))),
hdata_dec.loc[i, '노인보호구역'] / pow(10, len(str(max_노인보호구역))),
hdata_dec.loc[i, '사고건수'] / pow(10, len(str(max_사고건수)))
 ]
).loc[i, '사고건수'] / pow(10, len(str(max_사고건수)))
 ])

hdata_dec_scaling = pd.DataFrame(list_of_decs, columns = ['행정동','보행등','보행자작동신호기', '잔여시간표시기','보행노인사고다발지역','노인인구수','노인보호구역','사고건수']
                                )

print(hdata_dec_scaling)

#### 상관분석
col_names = ['행정동','보행등','보행자작동신호기', '잔여시간표시기','보행노인사고다발지역','노인인구수','노인보호구역','사고건수']

# 정규화한 데이터값 
hdata_z_scaling.head()
num_of_var = 8
for i in range(0, num_of_var):
	corr = np.corrcoef(hdata_z_scaling.iloc[:, i],
		hdata_z_scaling.iloc[:, num_of_var-1])
print("(" + col_names[i] + " vs." + col_names[num_of_var-1] +") : %.3f" % (corr[0][1]))

df = hdata.corr()
# 그림 사이즈 지정
fig, ax = plt.subplots( figsize=(7,7) )

# 삼각형 마스크를 만든다(위 쪽 삼각형에 True, 아래 삼각형에 False)
mask = np.zeros_like(df, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True

# 히트맵을 그린다
sns.heatmap(df, 
            cmap = 'RdYlBu_r', 
            annot = True,   # 실제 값을 표시한다
            mask=mask,      # 표시하지 않을 마스크 부분을 지정한다
            linewidths=.5,  # 경계면 실선으로 구분하기
            cbar_kws={"shrink": .5},# 컬러바 크기 절반으로 줄이기
            vmin = -1,vmax = 1   # 컬러바 범위 -1 ~ 1
           )  
plt.show()

sns.heatmap(data = hdata.corr(), annot=True, 
fmt = '.2f', linewidths=.5, cmap='Blues')
