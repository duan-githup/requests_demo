# 1、导包
import yaml
import os

class GetYaml:

    @classmethod
    def loads(cls,fileName,key):

        # 2、获取文件流
        with open("."+os.sep+"data"+os.sep+"{}.yaml".format(fileName),"r",encoding="utf-8") as f:
            # 3、读取文件
            data = yaml.load(f,Loader=yaml.FullLoader)

        # 获取父级键
        dict_date = data[key]
        list_data = list()

        # 获取子级的values
        for i in dict_date.values():
            list_data.append(i)

        return list_data


    # def dumps():
    #     # 2、准备写入的数据
    #     data={"S_data":{"test1":"hello"},"Sdata2":{"name":"汉字"}}
    #
    #     with open("./datas.yaml","w",encoding="utf-8") as f:
    #         # 3、写入文件
    #         yaml.dump(data,f,allow_unicode=True)



if __name__ == '__main__':
    l = loads("data", "test_case2")
    print(l)