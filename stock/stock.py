import tushare as ts
import datetime
#import matplotlib.pyplot as plt
import base

# sort_key = 2
# def sort_stock(elem):
    # return elem[sort_key]

ts.set_token('0f463b66c590584ead0b7b4b4f19a286441ec791991164b8f601e57f')
pro = ts.pro_api()
stock_info = pro.stock_basic()
stock_info = stock_info.set_index(['symbol'])
#info = stock_info.loc[stock_info['symbol'] == '002119']
today = datetime.datetime.now().strftime("%Y-%m-%d")
today = "2019-06-03"
stock = []
#code = ('002119', '600352', '300099', '600093', '000159', '600290', '601860', '300265', '002847', '002930', '300519', '603259', '601138', '600929', '600549', '600581', '300505', '300644', '600128', '601899', '600606')
code = ('002119')
info = stock_info.loc['600290']
print(info)
data = ts.pro_bar(ts_code=info.ts_code, start_date='20190503', end_date='20190520', ma=(5,10))
#data.plot(x='trade_date', y=['close'])
#plt.show()
print(data)
gfhg
#print(ts.get_hist_data('sh000001'))
# for i in code:
#     stockInfo = base.getStockInfo(i)
#     data = ts.get_hist_data(i, today)
#     print(type(data))
#     #data = ts.get_k_data('sz002930', today)
#     print(data)
#     ess
#     daily = data.iloc[0]
#     #print(daily)
#     #gap_ma5 = (daily.loc['ma5']/daily.loc['close']-1)*100 if daily.loc['ma5']>=daily.loc['close'] else 'false'
#     #gap_ma10 = (daily.loc['ma10']/daily.loc['close']-1)*100 if daily.loc['ma10']>=daily.loc['close'] else 'False'
#     #gap_ma20 = (daily.loc['ma20']/daily.loc['close']-1)*100 if daily.loc['ma20']>=daily.loc['close'] else 'False'
#     gap_ma5 = round((daily.loc['close']/daily.loc['ma5']-1)*100, 2)
#     gap_ma10 = round((daily.loc['close']/daily.loc['ma10']-1)*100, 2)
#     gap_ma20 = round((daily.loc['close']/daily.loc['ma20']-1)*100, 2)
#     #print((stockInfo['name'], gap_ma5, gap_ma10, gap_ma20))
#     stock.append((stockInfo['name'], gap_ma5, gap_ma10, gap_ma20))

# stock.sort(key=sort_stock)
#print(stock)

# file = today + '_stock.txt'
# f = open(file, 'wt', encoding= 'utf-8')

# for s in stock:
#     for c in s:
#         f.write(str(c))
#         f.write('\t')
#     f.write('\n')

# f.close() 

#print(daily)
#print(type(daily))
#print(ts.realtime_boxoffice())
#data['new'] = data.apply(lambda x: ((1)?x.loc['ma20'] / x.loc['close'] - 1 : false), 1)
#data['gap_ma5']=data.apply(lambda x: (x.loc['ma5']/x.loc['close']-1)*100 if x.loc['ma5']>=x.loc['close'] else False, 1)
#data['gap_ma10']=data.apply(lambda x: (x.loc['ma10']/x.loc['close']-1)*100 if x.loc['ma10']>=x.loc['close'] else False, 1)
#data['gap_ma20']=data.apply(lambda x: (x.loc['ma20']/x.loc['close']-1)*100 if x.loc['ma20']>=x.loc['close'] else False, 1)
#print(data[['gap_ma5','gap_ma10','gap_ma20']])
