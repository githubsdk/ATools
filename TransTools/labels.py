# 读取指定目录里的.meta文件，使用yaml分析并打印label属性
import yaml
import os

fbx_dir = 'D:/HHGames/flyff-client/MMO/Assets/AssetsPackage/Art/FFExport/part_dae2fbx'
fbx_lables = dict()
for root, dirs, files in os.walk(fbx_dir):
    for file in files:
        if file.endswith('.fbx.meta'):
            with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                meta = yaml.load(f, Loader=yaml.FullLoader)
                if 'labels' in meta:
                    label_key = file.replace('.fbx.meta', '')
                    fbx_lables[label_key] = meta['labels']
                    # print(meta['labels'], file)
                else:
                    print('no label --------------->', file)

dir = 'D:/HHGames/flyff-client/MMO/Assets/AssetsPackage/Prefabs/Parts'
# 导入python yaml包，使用yaml读取指定目录里的.meta文件，修改文件的labels属性并保存该.meta文件

for root, dirs, files in os.walk(dir):
    for file in files:
        if file.endswith('.prefab.meta'):
            meta = None

            label_key = file.replace('.prefab.meta', '')
            if label_key in fbx_lables:
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    meta = yaml.load(f, Loader=yaml.FullLoader)
                    # print(meta, file)
                with open(os.path.join(root, file), 'w', encoding='utf-8') as f:
                    meta['labels'] = fbx_lables[label_key]
                    # meta['labels'].append('PartPrefab')
                    yaml.dump(meta, f, default_flow_style=False)
            else:
                print('no label --------------->', file)
# files = os.listdir()
# for file in files:
#     if file.endswith('.meta'):
#         with open(file, 'r', encoding='utf-8') as f:
#             meta = yaml.load(f)
#             print(meta['label'], file)
