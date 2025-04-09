"""
和文件相关的类定义
"""
from data_define import Record
import json
class FileReader:
    def read_data(self) -> list[Record]:
        pass

class TextFileReader(FileReader):
    def __init__(self,path):
        self.path = path


    def read_data(self) -> list[Record]:
        f = open(self.path, "r" ,encoding="UTF-8")
        record_list: list[Record] = []#record_list = []
        for line in f.readlines():
            line = line.strip()
            data_list = line.split(",")
            record = Record(data_list[0], data_list[1], int(data_list[2]), data_list[3])
            """
            当执行Record(data_list[0], ...)时，实际上发生了三个关键步骤：
            类调用：解释器将Record视为可调用对象（因其实现了__call__方法，默认由__init__触发）
            对象创建：自动调用__new__方法创建空实例（通常无需手动实现）
            初始化执行：自动调用__init__方法进行初始化
            """
            record_list.append(record)
        f.close()
        return record_list

class JsonFileReader(FileReader):
    def __init__(self, path):
        self.path = path

    def read_data(self) -> list[Record]:
        f = open(self.path, "r", encoding="UTF-8")

        record_list: list[Record] = []
        for line in f.readlines():
            data_dict = json.loads(line)
            record = Record(data_dict["date"], data_dict["order_id"], int(data_dict["money"]), data_dict["province"])
            record_list.append(record)

        f.close()
        return record_list


if __name__ == '__main__':
    text_file_reader = TextFileReader("/Users/iwill/Documents/Documents/2011年1月销售数据.txt")
    json_file_reader = JsonFileReader("/Users/iwill/Documents/Documents/2011年2月销售数据JSON.txt")
    list1 = text_file_reader.read_data()
    list2 = json_file_reader.read_data()

    for i in list1:
        print(i)
    for j in list2 :
        print(j)