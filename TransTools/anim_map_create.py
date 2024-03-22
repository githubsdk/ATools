
import json


def read_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


motion_cfg_path = 'D:/HHGames/flyff-client/FFSource/表格转换/mvr-动作表.json'
motion_cfg = read_json(motion_cfg_path)

mi_define_path = 'D:/HHGames/flyff-client/FFSource/表格转换/defineObj.h_defines.json'
mi_define = read_json(mi_define_path)


# 获得字典的所有key，生成一个列表
male_motion_keys = list(motion_cfg['MI_MALE']['animation'].keys())
female_motion_keys = list(motion_cfg['MI_FEMALE']['animation'].keys())

# 合并两个列表，并去除重复内容；调试用看看男女动作差异
all_motion_keys = list(set(female_motion_keys + male_motion_keys))
print(len(all_motion_keys), len(male_motion_keys), len(female_motion_keys))


def assemble_animation_config(origin_dict, assemble_dict):
    for k, v in origin_dict.items():
        if 'animation' in v:
            assemble_dict[k] = v
        else:
            print('----------', k)
            assemble_animation_config(v, assemble_dict)


# 字典合并
npc_cfg = dict()
assemble_animation_config(motion_cfg.pop('NPC'), npc_cfg)
monster_cfg = dict()
assemble_animation_config(motion_cfg.pop('Monster'), monster_cfg)
# motion_cfg.pop('MI_MALE')
# motion_cfg.pop('MI_FEMALE')

# 合并需要的dict
all_motions = {**npc_cfg, **monster_cfg,  **motion_cfg}


def collect_motion_names(cfg):
    names = list()
    for k, v in cfg.items():
        motions_list = list(v['animation'].keys())
        names = names + motions_list
        if len(motions_list) > 20:
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!', k, len(motions_list))
    names = list(set(names))
    print('collect_motion_names', len(names), names)

collect_motion_names(npc_cfg)
collect_motion_names(monster_cfg)


# 收集所有动作配置，可以导出配置
collect_motions_dict = dict()
# 收集使用的动作名，仅供调试
collect_motion_name_list = list()
for key in all_motions.keys():
    animations_list = all_motions[key]['animation']
    collect_motion_name_list = collect_motion_name_list + \
        list(animations_list.keys())
    collect_motions_dict.update({key: animations_list})

collect_motion_name_list = list(set(collect_motion_name_list))

print(len(collect_motion_name_list), len(collect_motions_dict))

# 保存json
with open('D:/HHGames/flyff-client/FFSource/表格转换/collect_motions.json', 'w', encoding='utf-8') as f:
    json.dump(collect_motions_dict, f, indent=4, ensure_ascii=False)

# collect_motion_name_list 按value的名字排序
collect_motion_name_list.sort()
