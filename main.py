from file_define import *
from data_define import Record
from pyecharts.charts import Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType

text_file_reader = TextFileReader("/Users/iwill/Documents/Documents/2011年1月销售数据.txt")
json_file_reader = JsonFileReader("/Users/iwill/Documents/Documents/2011年2月销售数据JSON.txt")
jan_data: list[Record] = text_file_reader.read_data()
feb_data: list[Record] = json_file_reader.read_data()
all_data: list[Record] = jan_data + feb_data

data_dict = {}
for record in all_data:
    if record.data in data_dict.keys():
        data_dict[record.data] += record.money #此处的record.data是键，右边的money与对应的值相加
    else:
        data_dict[record.data] = record.money

bar = Bar(init_opts=InitOpts(theme=ThemeType.LIGHT))#类对象
bar.add_xaxis(list(data_dict.keys()))
bar.add_yaxis("销售额", list(data_dict.values()), label_opts=LabelOpts(is_show=False))
bar.set_global_opts(
    title_opts=TitleOpts(title="每日销售额")#类对象
)
bar.render("每日销售额柱状图.html")