import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("D:/BaiduNetdiskDownload/car_complain.csv")
#拆分problem,并统计
tem_list = df["problem"].str.split(",").tolist()
cate_list = list(set([j  for  i in tem_list for j in i]))
zero_list = pd.DataFrame(np.zeros((df.shape[0],len(cate_list))),columns=cate_list)
for i in range(df.shape[0]):
    zero_list.loc[i,tem_list[i]] = 1
genre_count = zero_list.sum(axis = 0)

print(genre_count)
#设置索引
df1 = zero_list
df1["brand"] = df["brand"]
df1["car_model"] = df["car_model"]
df1["id"] = df["id"]
df2 = df1.groupby("brand")["id"].count()
print(df2)
df3 = df1.groupby("car_model")["id"].count()
print(df3)
df4 = df1.groupby(["brand","car_model"]).agg(['count']).groupby("brand").mean()
print(df4)


