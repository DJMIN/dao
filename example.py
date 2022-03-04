from dao import D
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)


def handle(data):
    print(data)
    return data + 1


if __name__ == '__main__':
    # 志(物质) = 道(势, 术+器， 法)(意识)

    # 结果 = 目的(生产者, 消费者)(过程)

    res = D(range, handle)(1, 10)
    print(res)

    res = D(range, handle).zhi(1, 10).wd(list, handle).wu_dao(list, handle)()

    print(res)
