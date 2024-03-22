define_json_path = 'D:/HHGames/flyff-client/FFSource/表格转换/defineNeuz.h_defines.json'

# 加载json
def load_json(path):
    import json
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

#print(load_json(define_json_path))
    
define_dict = load_json(define_json_path)
# 遍历dict，移除前缀名不是MTI_的key
remove_keys = list()
for key in define_dict.keys():
    if not key.startswith('MTI_'):
        remove_keys.append(key)
        
# 遍历remove_keys，移除对应的key
for key in remove_keys:
    define_dict.pop(key)

# define_dict 按 key 值排序
define_dict = dict(sorted(define_dict.items()))
# define_dict 按 value 值排序
define_dict = dict(sorted(define_dict.items(), key=lambda x:x[1]))

with open('D:/HHGames/flyff-client/FFSource/表格转换/motions_defines.json', 'w', encoding='utf-8') as f:
    import json
    json.dump(define_dict, f, indent=4, ensure_ascii=False)
