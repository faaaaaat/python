import tushare as ts
import datetime
import base

today = datetime.datetime.now().strftime("%Y-%m-%d")

code = '002930'
stockInfo = base.getStockInfo(code)

#print(ts.get_hist_data('sh000001'))


data = ts.get_hist_data(code, today)
#data = ts.get_k_data('sz002930', today)
daily = data.iloc[0]
gap_ma5 = (daily.loc['ma5']/daily.loc['close']-1)*100 if daily.loc['ma5']>=daily.loc['close'] else False
gap_ma10 = (daily.loc['ma10']/daily.loc['close']-1)*100 if daily.loc['ma10']>=daily.loc['close'] else False
gap_ma20 = (daily.loc['ma20']/daily.loc['close']-1)*100 if daily.loc['ma20']>=daily.loc['close'] else False
print([stockInfo['name'], gap_ma5, gap_ma10, gap_ma20])

print(daily)
print(type(daily))
#print(ts.realtime_boxoffice())
#data['new'] = data.apply(lambda x: ((1)?x.loc['ma20'] / x.loc['close'] - 1 : false), 1)
#data['gap_ma5']=data.apply(lambda x: (x.loc['ma5']/x.loc['close']-1)*100 if x.loc['ma5']>=x.loc['close'] else False, 1)
#data['gap_ma10']=data.apply(lambda x: (x.loc['ma10']/x.loc['close']-1)*100 if x.loc['ma10']>=x.loc['close'] else False, 1)
#data['gap_ma20']=data.apply(lambda x: (x.loc['ma20']/x.loc['close']-1)*100 if x.loc['ma20']>=x.loc['close'] else False, 1)
#print(data[['gap_ma5','gap_ma10','gap_ma20']])
