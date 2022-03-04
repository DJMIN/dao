from dao import D

if __name__ == '__main__':

    def handle(data):
        print(data)
        return data+1

    # 志(物质) = 道(势, 术+器， 法)(意识)

    # 结果 = 目的(生产者, 消费者)(过程)
    res = D(range, handle, list, 1, 10).wd(list, handle, list).WD(list, handle, list)()

    print(res)
