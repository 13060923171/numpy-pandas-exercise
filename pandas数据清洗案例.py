import pandas as pd

data = pd.read_excel
# 如果有重复值，则保留第一个
data.drop_duplicates(keep='first', inplace=True)

# 替换None
data = data.applymap(lambda x: '暂无数据' if x == 'None' else x)

# 切分地区、房屋户型、所在楼层、抵押信息后删除原列，将拆分出的新列合并至原data
data = pd.concat([data, data['地区'].str.extract(pat='(?P<区>.*?)\s(?P<镇>.*?)\s(?P<环>.*)'),
                  data['房屋户型'].str.extract(
                      pat='(?P<室>\d+)室(?P<厅>\d+)厅(?P<厨>\d+)厨(?P<卫>\d+)卫'),
                  data['所在楼层'].str.extract(
                      pat='(?P<所处楼层>.+)\(共(?P<总层数>\d+)层\)'),
                  data['抵押信息'].map(lambda x:x.strip()).str.extract(pat='(?P<有无抵押>.{1})抵押(?P<抵押情况>.*)?')], axis=1)

data.drop(['地区', '所在楼层', '抵押信息'], axis=1, inplace=True)
data['区'] = data['区']+'区'
# 去除建筑面积后面的平米单位，并转为float
data['建筑面积'] = data['建筑面积'].map(lambda x: float(x[:-1]))

# 转换数据类型
data['价格'] = data['价格'].astype(float)

# 转换日期类型
data['挂牌时间'] = pd.to_datetime(data['挂牌时间'])

# 如果存在非时间类型的字符串则替换为NaT
data['上次交易'] = pd.to_datetime(data['上次交易'], errors="coerce")

# 存在括号几期、某区，都暂且删除
data['小区'] = data['小区'].str.replace("[\(\（].*?[\)\）]", "")

# 筛选出价格小于20的数据，我们可以发现这些房源的面积及所属区域都是比较好的，记录的数据可能有所错误
# 返回链家网站搜索这几套房源后发现，这些价格的单位都是"亿"，所以我们需要对所有数据再一次进行清洗
# 统一使用'万'作为总价的单位
data['价格'] = data['价格'].map(lambda x: x*10000 if x < 20 else x)

# 计算每平米单价
data['均价'] = round(data['价格']/data['建筑面积']*10000, 2)