import tushare as ts

#filename = 'stock_base.txt'
#f = open(filename, 'wt', encoding= 'utf-8')
#print(type(f))
stock = ts.get_stock_basics()

def getStockInfo(code):
    return stock.ix[code]

if __name__ == '__main__':
    stock_list = []
    stock = ts.get_stock_basics()
