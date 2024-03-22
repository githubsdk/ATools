import os

import yaml

# 遍历目录下指定后缀名的文件，获得文件绝对路径，
def move_file_to_own_dir(directory, suffix):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(suffix):
                base_name = os.path.basename(root)
                file_name = os.path.splitext(file)[0]
                # 文件不在与文件同名文件夹中
                if base_name != file_name:
                    new_path = os.path.join(root, file_name)
                    if os.path.exists(new_path):
                        print('文件夹已存在')
                    else:
                        print('创建文件夹：' + new_path)
                        os.mkdir(new_path)
                    # 移动文件到新文件夹
                    os.rename(os.path.join(root, file), os.path.join(new_path, file))
                    meta_file = os.path.join(root, '{0}.meta'.format(file))
                    if os.path.exists(meta_file):
                        os.rename(meta_file, os.path.join(new_path, '{0}.meta'.format(file)))
                    print(1)

# 检查该文件所在的目录名，是否和文件名相同；如果不同，创建与文件同名的文件夹，并把文件移动进去                    


directory = 'D:/HHGames/flyff-client/MMO/Assets/AssetsPackage/Art/FFExport/Ctrl'
move_file_to_own_dir(directory,   '.fbx')

# 读取unity 的meta文件，加入节点
def meta_add_label(directory, suffix):
    base_name = os.path.basename(directory)
    label_name = 'MD{0}'.format(base_name)
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(suffix):
               with open(os.path.join(root, file), 'r+') as f:
                   crf = f.read()
                   yaml_data = yaml.load(stream=crf, Loader=yaml.FullLoader)
                   
                   if 'labels' in yaml_data:
                       labels = yaml_data['labels']
                       if label_name not in labels:
                           labels.append(label_name)
                           yaml_data['labels'] = labels
                   else:
                      yaml_data['labels'] = [label_name]

                   if 'ModelImporter' in yaml_data and 'animations' in yaml_data['ModelImporter']:
                       print(yaml_data['ModelImporter'])
                       

                   f.seek(0)
                   f.write(yaml.dump(yaml_data, default_flow_style=False))

# meta_add_label(directory, '.fbx.meta')