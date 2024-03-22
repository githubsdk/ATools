import os

bones:dict= {'bip02_ponytail12':    'Bip02 Ponytail12',
             'bip02_ponytail11':    'Bip02 Ponytail11',
             'bip02_ponytail1':     'Bip02 Ponytail1',
             'bip02_head':          'Bip02 Head',
             'bip02_l_hand':        'Bip02 L Hand',
             'bip02_l_forearm':     'Bip02 L ForeArm',
             'bip02_l_upperarm':    'Bip02 L UpperArm',
             'bip02_l_clavicle':    'Bip02 L Clavicle',
             'bip02_r_hand':        'Bip02 R Hand',
             'bip02_r_forearm':     'Bip02 R ForeArm',
             'bip02_r_upperarm':    'Bip02 R UpperArm',
             'bip02_r_clavicle':    'Bip02 R Clavicle',
             'bip02_neck':          'Bip02 Neck',
             'bone07':              'Bone07',
             'bone06':              'Bone06',
             'bone05':              'Bone05',
             'bone03':              'Bone03',
             'bone02':              'Bone02',
             'bone01':              'Bone01',
             'bip02_spine2':        'Bip02 Spine2',
             'bip02_spine1':        'Bip02 Spine1',
             'bip02_l_foot':        'Bip02 L Foot',
             'bip02_l_calf':        'Bip02 L Calf',
             'bip02_l_thigh':       'Bip02 L Thigh',
             'bip02_r_foot':        'Bip02 R Foot',
             'bip02_r_calf':        'Bip02 R Calf',
             'bip02_r_thigh':       'Bip02 R Thigh',
             'bip02_spine':         'Bip02 Spine',
             'bip02_pelvis':        'Bip02 Pelvis',
             'bip02':               'Bip02',
             # mvr
             'bip01_ponytail12':    'Bip01 Ponytail12',
             'bip01_ponytail11':    'Bip01 Ponytail11',
             'bip01_ponytail1':     'Bip01 Ponytail1',
             'bip01_head':          'Bip01 Head',
             'bip01_l_hand':        'Bip01 L Hand',
             'bip01_l_forearm':     'Bip01 L ForeArm',
             'bip01_l_upperarm':    'Bip01 L UpperArm',
             'bip01_l_clavicle':    'Bip01 L Clavicle',
             'bip01_r_hand':        'Bip01 R Hand',
             'bip01_r_forearm':     'Bip01 R ForeArm',
             'bip01_r_upperarm':    'Bip01 R UpperArm',
             'bip01_r_clavicle':    'Bip01 R Clavicle',
             'bip01_neck':          'Bip01 Neck',
             'bip01_spine2':        'Bip01 Spine2',
             'bip01_spine1':        'Bip01 Spine1',
             'bip01_l_foot':        'Bip01 L Foot',
             'bip01_l_calf':        'Bip01 L Calf',
             'bip01_l_thigh':       'Bip01 L Thigh',
             'bip01_r_foot':        'Bip01 R Foot',
             'bip01_r_calf':        'Bip01 R Calf',
             'bip01_r_thigh':       'Bip01 R Thigh',
             'bip01_spine':         'Bip01 Spine',
             'bip01_pelvis':        'Bip01 Pelvis',
             'bip01':               'Bip01'
             }

def read_files_with_suffix(directory, suffix):
    files = []
    for root, dirs, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith(suffix):
                files.append(os.path.join(root, filename))
    return files

directory = 'D:/Github/feifei/FlyffVS2019/Tools/ATools v1_2/Model/AutoSave/CtrlItem/FBX/Obj'  # 请替换为实际目录路径
# directory = 'D:/HHGames/flyff-client/MMO/Assets/AssetsPackage/Art/Character/Parts_mCloBaseball01'
suffix = '.fbx'  # 请替换为实际文件后缀名
result = read_files_with_suffix(directory, suffix)

for file_path in result:
    file_dir,file_name = os.path.split(file_path)
    # 统一首字母大写
    rename_file_name = str.replace(file_name, 'part_', 'Part_')
    os.rename(file_path, str.replace(file_path, file_name, rename_file_name))
    file_name, ext = os.path.splitext(file_name)
    print(file_name)
    
    content:str
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read();
    for key, value in bones.items():
        content = content.replace(key, value)
    # 替换贴图格式和路径
    meta_file = file_path + '.meta'
    if('.DDS' in content and os.path.exists(meta_file)):
        os.remove(file_path + '.meta')
    content = content.replace('.dds', '.png').replace('.DDS', '.png')
    content = content.replace('"..\\"', '"..\\Texture\\"').replace('..\\Texture\\Texture\\', '..\\Texture\\')
    # 替换材质命名，换成不带前后缀的文件名，方便查找；另外有些模型做的不规范，没有GMObject0这个名字
    part_name = str.replace(file_name, 'Part_', '')
    content = content.replace('Material0GMObj0', part_name)
    content = content.replace('GMObject0', part_name)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
        
