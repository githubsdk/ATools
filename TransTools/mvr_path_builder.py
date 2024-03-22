# 创建mvr的目录层级

# 读取目录下所有文件，根据每个文件名，去除前缀和后缀，创建目录，并把这个文件放入目录
import os
import shutil

def create_model_path(path):
    # 读取目录下所有文件
    files = os.listdir(path)
    for full_name in files:
        # 去除前缀和后缀
        dir_name = full_name.split('.')[0]
        src_file = os.path.join(path, full_name)
        # 排除目录
        if not os.path.isfile(src_file):
            continue
        # 判断目录是否存在
        dir = os.path.join(path, dir_name)
        if not os.path.exists(dir):
            os.mkdir(dir)
            
        mat_dir = os.path.join(dir, 'Material')
        if not os.path.exists(mat_dir):
            os.mkdir(mat_dir)
        # 移动文件
        dest = os.path.join(path, dir_name, full_name)
        shutil.move(src_file, dest) 
        shutil.move(src_file + '.meta',  dest + '.meta')
        # break

# 读取目录下所有文件，使用@分割文件名，去除前缀和后缀，创建文件夹，并把文件移动到创建的文件夹里
def create_motion_path(path):
    # 读取目录下所有文件
    files = os.listdir(path)
    for full_name in files:
        # 去除前缀和后缀
        dir_name = full_name.split('.')[0].split('@')[0]
        src_file = os.path.join(path, full_name)
        # 排除目录
        if not os.path.isfile(src_file):
            continue
        # 判断目录是否存在
        dir = os.path.join(path, dir_name)
        if not os.path.exists(dir):
            os.mkdir(dir)
        # 移动文件
        dest = os.path.join(path, dir_name, full_name)
        shutil.move(src_file, dest) 

def move_part_material(path):
    # 读取目录下所有文件
    files = os.listdir(path)
    for full_name in files:
        if not str.endswith(full_name, '.mat'):
            continue
        # 去除前缀和后缀
        dir_name = 'Part_' + full_name.split('.')[0]
        src_file = os.path.join(path, full_name)
        # # 排除目录
        # if not os.path.isfile(src_file):
        #     continue
        # 判断目录是否存在
        # dir = os.path.join(path, dir_name)
        # if not os.path.exists(dir):
        #     os.mkdir(dir)
            
        # mat_dir = os.path.join(dir, 'Material')
        # if not os.path.exists(mat_dir):
        #     os.mkdir(mat_dir)
        # 移动文件
        dest = os.path.join(path, dir_name, 'Material', full_name)
        try:
            shutil.move(src_file, dest) 
            shutil.move(src_file + '.meta',  dest + '.meta')
        except:
            print(src_file)
        # break

# move_part_material('D:/HHGames/flyff-client/MMO/Assets/AssetsPackage/Art/FFExport/part_dae2fbx')
# create_model_path('D:/HHGames/flyff-client/MMO/Assets/AssetsPackage/Art/FFExport/part_dae2fbx')
# create_model_path('D:/Github/feifei/FlyffVS2019/Tools/ATools v1_2/Model/AutoSave/Mvr/Model/')
# create_motion_path('D:/Github/feifei/FlyffVS2019/Tools/ATools v1_2/Model/AutoSave/Mvr/Motion/')

def action_check(path):
    '''
    看看一共用了哪些动作
    '''
    action_dict : dict = {}
    files = os.listdir(path)
    for full_name in files:
        if not str.endswith(full_name, '.dae'):
            continue
        action_name = full_name.split('@')[1].split('.')[0]
        action_name = action_name.lower()
        if action_name not in action_dict:
            action_dict[action_name] = 0
        else:
            action_dict[action_name] = action_dict[action_name] + 1

    print(action_dict)

# action_check('D:/Github/feifei/FlyffVS2019/Tools/ATools v1_2/Model/AutoSave/Mvr/MotionDAE/')
