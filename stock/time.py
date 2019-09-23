import datetime
import sys
import tushare as ts


data = ts.get_hist_data('600606', '2019-06-15', '2019-06-15')
print(data.empty)
end = datetime.datetime.now()
if len(sys.argv) > 1:
    input_d = sys.argv[1].split('-')
    input_d = list(map(int, input_d))
    begin = datetime.datetime(input_d[0], input_d[1], input_d[2])
else :
    begin = end

delta = datetime.timedelta(days=1)
while begin <= end:
    print(begin.strftime("%Y-%m-%d"))
    begin += delta