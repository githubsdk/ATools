import os


class Test:
    a = 1
    list_test: list = [1, 2, 3]

    def __init__(self) -> None:
        self.c: int = 3


t1 = Test()
t2 = Test()

print(t1.list_test, t2.list_test)
t1.a = 3
t1.list_test.append(5)
print(t1.a, t2.a, t1.list_test, t2.list_test)
print(t1.c, t2.c)

# 路径中提取文件名


def get_file_name(path):
    return os.path.basename(path)


basename = get_file_name(
    'D:/Github/feifei/FlyffVS2019/Tools/ATools v1_2/Model/mvr_female_SklMerOneSnake.ani')
# 字符串中有多个_，提取最后一个_前的所有内容

basename = basename.split('_')
# file_basename = basename.split('_')[0]
print(basename.pop(), '_'.join(basename))

# 写入文本文件


# def write_text_file(filename, content):
#     with open(filename, 'w', encoding='utf-8') as f:
#         f.write(content)

# def xor_bytes(bytes1, bytes2):
#     return bytes(x ^ y for x, y in zip(bytes1, bytes2))
# b = int.to_bytes(205)
# c = int.to_bytes(-116, signed=True)
# print(int.from_bytes(b), b, c, xor_bytes(b, c).decode())

def fill_list():
    return 3

test_list = [fill_list() for _ in range(6)]
print(test_list)

print('{0}2{1}'.format(3,4), int(3.0))