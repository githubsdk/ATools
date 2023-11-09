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
             'bip02':               'Bip02'
             }

def read_files_with_suffix(directory, suffix):
    files = []
    for root, dirs, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith(suffix):
                files.append(os.path.join(root, filename))
    return files

directory = "D:/HHGames/flyff-client/MMO/Assets/AssetsPackage/Art/FFExport/part_dae2fbx"  # 请替换为实际目录路径
# directory = 'D:/HHGames/flyff-client/MMO/Assets/AssetsPackage/Art/Character/Parts_mCloBaseball01'
suffix = ".fbx"  # 请替换为实际文件后缀名
result = read_files_with_suffix(directory, suffix)

for file_path in result:
    content:str
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read();
    for key, value in bones.items():
        content = content.replace(key, value)
    content = content.replace(".dds", ".png")
    content = content.replace("..\\", "..\\Texture\\")
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
        
