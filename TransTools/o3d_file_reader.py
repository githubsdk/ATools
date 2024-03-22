from ff_class_define import *
import ff_file_msc
import ani_file_reader


def read_o3d_file(filename) -> Object3D:
    o3d_file: Object3D = Object3D()
    with open(filename, 'rb') as f:
        name_length = ff_file_msc.read_number(f, 1)
        # c_name = ff_file_msc.read_number(f, name_length)
        c_list: list = list()
        for i in range(name_length):
            c = ff_file_msc.read_number(f, 1)

            try:
                b = ff_file_msc.xor_bytes(
                    int.to_bytes(c, signed=True), b'\xcd')
                c_list.append(b.decode())
            except Exception as e:
                print(filename, e)
                return None
            # print(b)

        version = ff_file_msc.read_number(f)

        o3d_file.id = ff_file_msc.read_number(f)
        o3d_file.forces[0] = ff_file_msc.read_vector(f)
        o3d_file.forces[1] = ff_file_msc.read_vector(f)
        if version >= 22:
            o3d_file.forces[2] = ff_file_msc.read_vector(f)
            o3d_file.forces[3] = ff_file_msc.read_vector(f)
        o3d_file.src_iu = ff_file_msc.read_float(f)
        o3d_file.src_iv = ff_file_msc.read_float(f)
        ff_file_msc.read_number(f, 16)
        o3d_file.bounds = ff_file_msc.read_bounds(f)
        o3d_file.per_slerp = ff_file_msc.read_float(f)
        o3d_file.frame_count = ff_file_msc.read_number(f)
        o3d_file.event_count = ff_file_msc.read_number(f)
        if o3d_file.event_count > 0:
            o3d_file.events = ff_file_msc.read_event(f, o3d_file.event_count)
        tmp_value = ff_file_msc.read_number(f)
        if tmp_value != 0:
            o3d_file.coll_obj = ff_file_msc.read_gm_object(f)

        o3d_file.lod = bool(ff_file_msc.read_number(f))

        o3d_file.bone_count = ff_file_msc.read_number(f)
        if o3d_file.bone_count > 0:
            o3d_file.base_bones = [ff_file_msc.read_matrix(
                f) for _ in range(o3d_file.bone_count)]
            o3d_file.base_inv_bones = [ff_file_msc.read_matrix(
                f) for _ in range(o3d_file.bone_count)]
            if o3d_file.frame_count:
                o3d_file.motions = Animation()
                # anim: Animation = Animation()
                o3d_file.motions.bone_count = o3d_file.bone_count
                o3d_file.motions.frame_count = o3d_file.frame_count
                o3d_file.motions = ff_file_msc.read_anim_tm(
                    f, o3d_file.motions)

            # 不用保存
            o3d_file.send_vs = bool(ff_file_msc.read_number(f))

        pool_size = ff_file_msc.read_number(f)
        group_count = 1
        if o3d_file.lod:
            group_count = 3  # MAX_GROUP

        o3d_file.lod_groups = [ff_file_msc.read_lod_groups(
            f, o3d_file.frame_count) for _ in range(group_count)]

        if version >= 21:
            attr_value = ff_file_msc.read_number(f)
            if attr_value == o3d_file.frame_count:
                if o3d_file.frame_count > 0:
                    o3d_file.attributes = ff_file_msc.read_attribute(
                        f, o3d_file.frame_count, True)
            elif o3d_file.frame_count > 0:
                # 没有读取逻辑，跳过
                pass
        elif o3d_file.frame_count > 0:
            # 没有读取逻辑，跳过
            pass
        # print(''.join(c_list))
        # read_name = ff_file_msc.read_str(f, name_length)
        pass
    return o3d_file


# read_o3d_file('D:/Github/feifei/FlyffVS2019/Tools/ATools v1_2/Model/mvr_Abraxas.o3d')

def gen_o3d_files_attribute_json():
    faield = list()
    attributes_dict: dict = dict()
    o3d_files = ff_file_msc.find_all_files(
        'D:/Github/feifei/FlyffVS2019/Tools/ATools v1_2/Model', '.o3d')
    for file in o3d_files:
        o3d_file: Object3D = read_o3d_file(file)
        if o3d_file and o3d_file.attributes and len(o3d_file.attributes) > 0:
            file_name_split = ff_file_msc.normalize_file_name(file, '.o3d')
            if len(file_name_split) > 3:
                faield.append(file)
            else:
                fbx_file_name = '_'.join(file_name_split[:2])
                ff_file_msc.add_animation_attribute(
                    attributes_dict, fbx_file_name, '', o3d_file.attributes)

        elif not o3d_file:
            faield.append(file)
    print(faield)
    return attributes_dict


attributes = gen_o3d_files_attribute_json()
#
# with open('./attributes_o3d.json', 'w', encoding='utf-8') as f:
#     f.write(json.dumps(attributes, cls=AnimEncoder, indent=4))

# ------------------------------------------------
att_anims = ani_file_reader.gen_attribute_json()
with open('./attributes_in_one.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps({**attributes, **att_anims}, cls=AnimEncoder, indent=4))
