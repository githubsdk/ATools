from io import BufferedReader
import os
import struct
import chardet
from ff_class_define import *


def read_tm_animation(f: BufferedReader, read_size: int = 1):
    obj_list: list[TMAnimation]
    for i in range(read_size):
        animation: TMAnimation = TMAnimation()
        animation.rot = read_quaternion(f)
        animation.pos = read_vector(f)
        if read_size == 1:
            return animation
        elif i == 0:
            obj_list = list()
        obj_list.append(animation)
    return obj_list


def read_quaternion(f: BufferedReader):
    quat: Quaternion = Quaternion()
    quat.x = read_float(f)
    quat.y = read_float(f)
    quat.z = read_float(f)
    quat.w = read_float(f)
    return quat


def read_float(f: BufferedReader, order='little'):
    data = f.read(4)
    return float.from_bytes(data, byteorder=order, signed=True)


def read_bone(f: BufferedReader, read_count: int = 1, force_list: bool = False):
    obj_list: list[Bone] = None
    for i in range(read_count):
        bone: Bone = Bone()
        name_length = read_number(f)
        bone.name = read_str(f, name_length)
        bone.inverse_transform = read_matrix(f)
        bone.local_transform = read_matrix(f)
        bone.parent_id = read_number(f)
        if read_count == 1 and not force_list:
            return bone
        elif i == 0:
            obj_list = list()
        obj_list.append(bone)
    return obj_list


def read_anim_tm(f: BufferedReader, anim: Animation):
    anim.bones = read_bone(f, anim.bone_count, True)
    ani_count = read_number(f)
    anim.animations = [TMAnimation()]*ani_count
    anim.bone_frames = [BoneFrame()] * anim.bone_count
    anim_index = 0
    for bone_index in range(anim.bone_count):
        frame_index = read_number(f)
        if frame_index == 1:
            frames: list[TMAnimation] = [
                TMAnimation] * anim.frame_count
            anim.bone_frames[bone_index].frames = frames
            for i in range(anim.frame_count):
                frames[i] = read_tm_animation(f)
                anim.animations[anim_index + i] = frames[i]
            anim_index = anim_index + anim.frame_count
        else:
            anim.bone_frames[bone_index].frames = None
            anim.bone_frames[bone_index].transform = read_matrix(f)
    return anim


def read_vector(f: BufferedReader, read_count: int = 1, is_vector2: bool = False):
    obj_list: list = None
    for i in range(read_count):
        vec = None
        if is_vector2:
            vec = Vector2()
        else:
            vec = Vector3()

        vec.x = read_float(f)
        vec.y = read_float(f)
        if not is_vector2:
            vec.z = read_float(f)
        if read_count == 1:
            return vec
        elif i == 0:
            obj_list = list()
        obj_list.append(vec)
    return obj_list


def read_attribute(f: BufferedReader, read_count: int = 1, force_list: bool = False):
    attributes: list[AnimAttribute] = None
    for i in range(read_count):
        frame_att: AnimAttribute = AnimAttribute()
        frame_att.att_type = read_number(f)
        frame_att.att_sound = read_number(f)
        frame_att.att_frame = int(read_float(f))
        if read_count == 1 and not force_list:
            return frame_att
        elif i == 0:
            attributes = list()
        if frame_att.att_type != 0:
            attributes.append(frame_att)
    return attributes


def read_matrix(f: BufferedReader, matrix_size=16):
    mat = Matrix(matrix_size)
    for i in range(matrix_size):
        mat.matrix[i] = read_float(f)
    return mat


def read_number(f: BufferedReader, nun_size: int = 4, read_count: int = 1, force_list=False, order='little'):
    obj_list: list[BufferedReader] = None
    for i in range(read_count):
        data = f.read(nun_size)
        obj: int = int.from_bytes(data, byteorder=order, signed=True)
        if read_count == 1:
            return obj
        if read_count == 1 and not force_list:
            return obj
        elif i == 0:
            obj_list = []
        obj_list.append(obj)
    return obj_list


def read_float(f: BufferedReader):
    data = f.read(4)
    return struct.unpack('f', data)[0]


def read_str(f: BufferedReader, str_size: int):
    data = f.read(str_size)
    result = chardet.detect(data)
    return data.decode(result['encoding']).strip(b'\x00'.decode())


def read_bounds(f: BufferedReader):
    bounds: Bounds = Bounds()
    bounds.min = read_vector(f)
    bounds.max = read_vector(f)
    return bounds


def read_skin_vertex(f: BufferedReader, read_count: int = 1):
    obj_list: list[SkinVertex] = None
    for i in range(read_count):
        obj: SkinVertex = SkinVertex()
        obj.p = read_vector(f)
        obj.w1 = read_float(f)
        obj.w2 = read_float(f)
        obj.id1 = read_number(f, 2)
        obj.id2 = read_number(f, 2)
        obj.n = read_vector(f)
        obj.t = read_vector(f, is_vector2=True)

        if read_count == 1:
            return obj
        elif i == 0:
            obj_list = []
        obj_list.append(obj)
    return obj_list


def read_normal_vertex(f: BufferedReader, read_count: int = 1):
    obj_list: list[NormalVertex] = None
    for i in range(read_count):
        obj = NormalVertex()
        obj.p = read_vector(f)
        obj.n = read_vector(f)
        obj.t = read_vector(f, is_vector2=True)
        if read_count == 1:
            return obj
        elif i == 0:
            obj_list = []
        obj_list.append(obj)
    return obj_list


def read_color(f: BufferedReader, read_count: int = 1):
    obj_list: list[Color] = None
    for i in range(read_count):
        obj = Color()
        obj.r = read_float(f)
        obj.g = read_float(f)
        obj.b = read_float(f)
        obj.a = read_float(f)
        if read_count == 1:
            return obj
        elif i == 0:
            obj_list = []
        obj_list.append(obj)
    return obj_list


def read_d3d9_material(f: BufferedReader, read_count: int = 1):
    obj_list: list[D3DMaterial9] = None
    for i in range(read_count):
        obj = D3DMaterial9()
        obj.diffuse = read_color(f)
        obj.ambient = read_color(f)
        obj.specular = read_color(f)
        obj.emission = read_color(f)
        obj.power = read_float(f)

        if read_count == 1:
            return obj
        elif i == 0:
            obj_list = []
        obj_list.append(obj)
    return obj_list


def read_material(f: BufferedReader, read_count: int = 1):
    obj_list: list[Material] = None
    for i in range(read_count):
        obj = Material()
        obj.material = read_d3d9_material(f)
        name_length = read_number(f)
        obj.texture_name = read_str(f, name_length)
        if read_count == 1:
            return obj
        elif i == 0:
            obj_list = []
        obj_list.append(obj)
    return obj_list


def read_material_block(f: BufferedReader, read_count: int = 1):
    obj_list: list[MaterialBlock] = None
    for i in range(read_count):
        obj: MaterialBlock = MaterialBlock()
        obj.start_vertex = read_number(f)
        obj.primitive_count = read_number(f)
        obj.material_id = read_number(f)
        obj.effect = read_number(f)
        obj.amount = read_number(f)
        obj.used_bone_count = read_number(f)
        obj.used_bones = read_number(f, 4, 28)
        if read_count == 1:
            return obj
        elif i == 0:
            obj_list = []
        obj_list.append(obj)
    return obj_list


def read_gm_object(f: BufferedReader, read_count: int = 1, obj_to_read: GMObject = None):
    obj_list: list[GMObject] = None
    for i in range(read_count):
        gm_object: GMObject
        if obj_to_read:
            gm_object = obj_to_read
        else:
            gm_object = GMObject()

        gm_object.bounds = read_bounds(f)
        gm_object.opacity = bool(read_number(f))
        gm_object.bump = bool(read_number(f))
        gm_object.rigid = bool(read_number(f))

        read_number(f, 28)

        gm_object.vertex_list_count = read_number(f)
        gm_object.vertex_count = read_number(f)
        gm_object.face_list_count = read_number(f)
        gm_object.index_count = read_number(f)

        gm_object.vertex_list = read_vector(f, gm_object.vertex_list_count)

        if gm_object.type == 1:  # GMT_SKIN
            gm_object.vertices = read_skin_vertex(f, gm_object.vertex_count)
        else:
            gm_object.vertices = read_normal_vertex(f, gm_object.vertex_count)

        gm_object.indices = read_number(f, 2, gm_object.index_count)
        gm_object.llb = read_number(f, 2, gm_object.vertex_count)
        tmp_value = read_number(f)
        if tmp_value != 0:
            gm_object.physique_vertices = read_number(
                f, 4, gm_object.vertex_list_count)

        gm_object.material = bool(read_number(f))
        if gm_object.material:
            gm_object.material_count = read_number(f) or 1
            gm_object.materials = read_material(f, gm_object.material_count)
        gm_object.material_block_count = read_number(f)
        gm_object.material_blocks = read_material_block(
            f, gm_object.material_block_count)
        if read_count == 1:
            return gm_object
        elif i == 0:
            obj_list = list()
        obj_list.append(gm_object)
    return obj_list


def read_lod_group(f: BufferedReader, read_count=1):
    obj_list: list[GMObject] = None
    for i in range(read_count):
        group = LODGroup()
        group.object_count = read_number(f)
        group.objects = read_gm_object(f, read_count=group.object_count)
        if read_count == 1:
            return group
        elif i == 0:
            obj_list = []
        obj_list.append(group)
    return obj_list


def read_lod_groups(f: BufferedReader, frame_count: int):
    group: LODGroup = LODGroup()
    group.object_count = read_number(f)
    group.objects = list()
    for i in range(group.object_count):
        gm_obj: GMObject = GMObject()
        gm_obj.type = read_number(f) & 0xffff
        if gm_obj.type & 0x80000000:
            gm_obj.light = True
        gm_obj.used_bone_count = read_number(f)
        gm_obj.used_bones = read_number(
            f, read_count=gm_obj.used_bone_count, force_list=True)
        gm_obj.id = read_number(f)
        gm_obj.parent_id = read_number(f)
        if gm_obj.parent_id != -1:
            gm_obj.parent_type = read_number(f)
        gm_obj.transform = read_matrix(f)
        gm_obj = read_gm_object(f, obj_to_read=gm_obj)
        if gm_obj.type == 0 and frame_count > 0:
            tmp_frame = read_number(f)
            if tmp_frame != 0:
                gm_obj.frames = read_tm_animation(f, frame_count)
        # group.objects = read_object(f, group.object_count)


def read_event(f: BufferedReader, read_count: int = 1):
    return read_vector(f, read_count)


def normalize_file_name(file_name: str, extension='.ani'):
    file_basename = os.path.basename(file_name)
    file_name_split = str.lower(file_basename)
    file_name_split = file_name_split.replace(extension, '').split('_')
    return file_name_split


def add_animation_attribute(file_attribute_dict: dict, fbx_name: str, anim_name: str, attributes: list[AnimAttribute]):
    # fbx_attributes: dict = None
    # if fbx_name in file_attribute_dict:
    #     fbx_attributes = file_attribute_dict[fbx_name]
    # else:
    #     fbx_attributes = dict()
    # file_attribute_dict[fbx_name] = fbx_attributes
    file_attribute_dict.update({fbx_name: attributes})


def find_all_files(dir, extension: str = '.ani'):
    file_list = []
    for root, dirs, files in os.walk(dir):
        for file in files:
            if file.endswith(extension):
                file_list.append(os.path.join(root, file))
    return file_list


def xor_bytes(bytes1, bytes2):
    return bytes(x ^ y for x, y in zip(bytes1, bytes2))
