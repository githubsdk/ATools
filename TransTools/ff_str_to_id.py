# 读取一个xlsx表格，把其中的两列，保存为dict；读另一个xlsx表格，把其中一列的字符串，匹配前一个表格中的关系，替换成数字，并保存xlsx文件
import pandas as pd
df = pd.read_excel(
    'D:/HHGames/flyff-resource/Config/ID_Define.xlsx', sheet_name='Sheet1')
df = df.set_index('name')
df = df['id'].to_dict()
# print(df)
df2 = pd.read_excel(
    'D:/HHGames/flyff-resource/Config/PropMover.xlsx', sheet_name='@PropMover')
# id_dict = df2.set_index('id[!.][funcInt]')
# id_dict = df2['idName[][funcStr]'].to_dict()
# #print(id_dict)
# new_col = dict()
# for key in id_dict.keys():
#     new_col[id_dict[key]] = df[id_dict[key]]

def id_name_to_value(d):
    return df[d['idName[][funcStr]']]

df2.loc[:, 'IdValue'] = df2.apply(id_name_to_value, axis=1)

df2.to_excel('D:/HHGames/flyff-resource/Config/PropMover2.xlsx', index=False)

# 修改xlsx指定列的数据
# df2['id[!.][funcInt]'][key] = df[df2['id[!.][funcInt]'][key]]
# df2.to_excel('D:/HHGames/flyff-resource/Config/ModelMover.xlsx', sheet_name='@ModelMover')
