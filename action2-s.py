import numpy as np
import pandas as pd
studenttype = np.dtype({
    'names':['name', 'chinese', 'math','english'],
    'formats':['S32','i', 'i', 'i']})
students = np.array([("ZhangFei",68,65,30),("GuanYu",95,76,98),("LiuBei",98,86,88),("DianWei",90,88,77),("XuChu",80,90,90)],dtype=studenttype)
print("语文平均:%d" %students["chinese"].mean())
print("数学平均:%d" %students["math"].mean())
print("英语平均:%d" %students["english"].mean())
print("语文最大:%d" %students["chinese"].max())
print("数学最大:%d" %students["math"].max())
print("英语最大:%d" %students["english"].max())
print("语文最小:%d" %students["chinese"].min())
print("数学最小:%d" %students["math"].min())
print("英语最小:%d" %students["english"].min())
print("语文标准差:%f" %students["chinese"].std())
print("数学标准差:%f" %students["math"].std())
print("英语标准差:%f" %students["english"].std())
print("语文方差:%f" %students["chinese"].var())
print("数学方差:%f" %students["math"].var())
print("英语方差:%f" %students["english"].var())

a=students["chinese"]+students["math"]+students["english"]
b=students["name"]
df = pd.DataFrame(a,index=b,columns=list("a"))
print( df.sort_values(by="a",ascending=False))

