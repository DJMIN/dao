from dao import D
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)


def handle(data):
    # print(data)
    return data + 1


if __name__ == '__main__':
    # 志(物质) = 道(势, 术+器， 法)(意识)

    # 结果 = 目的(生产者, 消费者)(过程)

    res = D(range, handle)(1, 10)
    print(res)

    res = D(
        range, handle).WD(
        list, handle).WD(
        list, handle).WD(
        list, handle)(1, 10)
    print(res)

    # json_data = [
    #     [-1, 'mysql', 'create_node'],
    #     [0, 'mysql', 'select'],
    #     [1, 'mysql', 'sort'],
    #     [2, 'mysql', 'get_data'],
    #     [3, 'mem', 'sort'],
    #     [4, 'mem', '1to2']]
    #
    # def start(data):
    #     return f'select * from {data}'
    #
    # def handle_1(data: tuple):
    #     return f'{data[0]} order by {data[1]}'
    #
    # def handle_2(data):
    #     import d22d
    #
    # def map_3(data):
    #     return data
    #
    # def reduce_3(self, data):
    #     return sorted(data)
    # #
    # # res = D(start, handle_0) \
    # #     .wd(list, handle) \
    # #     .wd(list, handle) \
    # #     .wd(list, handle) \
    # #     (['userDM', 'user'])
    # #
    # # res = D(excute, handle)\
    # #     .wd(list, handle)\
    # #     .wd(list, handle)\
    # #     .wd(list, handle)\
    # #     (['select * from user where username="c" limit 100'])
    #
    # # print(res)
    #
    # db = {
    #     'user': [
    #         {'a':1,'b':2,'c':3,},
    #         {'a':2,'b':4,'c':3,},
    #         {'a':3,'b':2,'c':3,},
    #     ]
    # }
    #
    # def get_data_by_table_name(ip, host, table_name):
    #     return db.get(table_name)
    #
    # def aes_decode(data):
    #     return data+1
    #
    # def format_data(data):
    #     return {
    #         'a': aes_decode(data["a"]),
    #         'b': data["b"] - 1,
    #         'c': data["c"] * 2,
    #     }
    #
    # res = D(get_data_by_table_name, format_data)(ip, host, 'user')
    # print(res)
