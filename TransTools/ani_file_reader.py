import json
import os

from ff_class_define import *
from ff_file_msc import *

'''
文件作用：搜集目录中ani文件，解析并提取attribute属性，导出到json
注意：att_type 是按位算的，多个属性可能只有1个att_type输出；具体可以搜索atool代码里 MA_SOUND 及相关内容
'''


def read_ani_file(filename):
    file_anim: Animation = Animation()
    # 读取文件
    with open(filename, 'rb') as f:
        # 计算int的大小
        version = read_number(f)
        file_anim.id = read_number(f)
        file_anim.per_slerp = read_float(f)

        f.read(32)
        file_anim.bone_count = read_number(f)
        file_anim.frame_count = read_number(f)
        # print(bone_count, frame_count)

        temp = read_number(f)
        if temp != 0:
            for i in range(file_anim.frame_count):
                file_anim.paths.append(read_vector(f))

        file_anim = read_anim_tm(f, file_anim)

        file_anim.attributes = read_attribute(f, file_anim.frame_count, True)

        event_count = read_number(f)
        if event_count != 0:
            read_event(f, event_count)
            print('event', event_count, '有事件----------------------->', filename)

        # print('finish')
    return file_anim

# anim = read_ani_file(
#     'D:/Github/feifei/FlyffVS2019/Tools/ATools v1_2/Model/mvr_female_SklMerOneSnake.ani')
# print(1)
# files = find_all_files(
#     'D:/Github/feifei/FlyffVS2019/Tools/ATools v1_2/Model')
# for file in files:
#     sigle_anim: Animation = read_ani_file(file)
#     # print(sigle_anim, sigle_anim.attributes)
#     if len(sigle_anim.attributes) > 0:
#         print(file, json.dumps(sigle_anim.attributes, cls=AnimEncoder))


def gen_attribute_json():
    files = find_all_files(
        'D:/Github/feifei/FlyffVS2019/Tools/ATools v1_2/Model')
    attributes_dict: dict = dict()
    for file in files:
        sigle_anim: Animation = read_ani_file(file)
        if len(sigle_anim.attributes) > 0:
            file_name_split = normalize_file_name(file, '.ani')
            if len(file_name_split) > 3:
                anim_name = '_'.join(file_name_split[-2:])
            else:
                anim_name = file_name_split.pop()
            # 有一些文件，前半部分是模型文件名，后半部分是动作名
            fbx_file_name = '_'.join(file_name_split[:2])
            add_animation_attribute(
                attributes_dict, '{0}@{1}'.format(fbx_file_name, anim_name), '', sigle_anim.attributes)

    # print(file, json.dumps(attributes_dict, cls=AnimEncoder, indent=4))
    return attributes_dict


# anim = read_ani_file(
#     'D:/Github/feifei/FlyffVS2019/Tools/ATools v1_2/Model/mvr_vilguard_atk1.ani')

# 生成帧属性用的
attributes = gen_attribute_json()
with open('./attributes_anim.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(attributes, cls=AnimEncoder, indent=4))

# files = find_all_files(
#     'D:/Github/feifei/FlyffVS2019/Tools/ATools v1_2/Model')
# for file in files:
#     file_basename = os.path.basename(file)
#     file_name_split = str.lower(file_basename)
#     file_name_split = file_name_split.replace('.ani', '').split('_')
#     if len(file_name_split) != 3:
#         print(file_name_split, file_name_split[-2:], '_'.join(file_name_split[-2:]))
#         print(file_name_split[-2:], file_name_split[:2], file_name_split[-1:])
