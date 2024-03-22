import datetime
import json


MAX_BONES = 28


class AnimAttribute:
    def __init__(self) -> None:
        self.att_type: int = 0
        self.att_sound: int = 0
        self.att_frame: int = 0


class Quaternion:
    def __init__(self) -> None:
        self.x: float = 0
        self.y: float = 0
        self.z: float = 0
        self.w: float = 0


class Vector2:
    def __init__(self) -> None:
        self.x: float = 0
        self.y: float = 0

class Vector3(Vector2):
    def __init__(self) -> None:
        super().__init__()
        self.z: float = 0


class TMAnimation:
    def __init__(self) -> None:
        self.rot: Quaternion = None
        self.pos: Vector3 = None


class Matrix:
    def __init__(self, length):
        self.matrix: list[float] = [0.0] * length


class Bone:
    def __init__(self) -> None:
        self.name: str = None
        self.inverse_transform: Matrix = None
        self.transform: Matrix = None
        self.local_transform: Matrix = None
        self.parent_id: int = None


class BoneFrame:
    def __init__(self) -> None:
        self.frames: list[TMAnimation] = None
        self.transform: Matrix = None


class Animation:
    def __init__(self) -> None:
        self.id: int = 0
        self.per_slerp: int = 0
        self.bone_count: int = 0
        self.frame_count: int = 0
        self.paths: list[Vector3] = list()
        self.bones: list[Bone] = None
        self.animations: list[TMAnimation] = None
        self.attributes: list[AnimAttribute] = None
        self.bone_frames: list[BoneFrame] = None
        self.events: list[Vector3] = [Vector3()]*4
# ----------------------------------------------------------------------------------------------------------------------


class Bounds:
    def __init__(self) -> None:
        self.min: Vector3 = None
        self.max: Vector3 = None


class Color:
    def __init__(self) -> None:
        self.r: float = 0
        self.g: float = 0
        self.b: float = 0
        self.a: float = 0


class D3DMaterial9:
    def __init__(self) -> None:
        self.diffuse: Color = Color()
        self.specular: Color = Color()
        self.emission: Color = Color()
        self.power: float = 0
        self.ambient: Color = Color()


class Material:
    def __init__(self) -> None:
        self.material: D3DMaterial9 = None
        self.texture_name: str = None


class MaterialBlock:
    def __init__(self) -> None:
        self.start_vertex: int = 0
        self.primitive_count: int = 0
        self.material_id: int = 0
        self.effect: int = 0
        self.amount: int = 0
        self.used_bone_count: int = 0
        self.used_bones: list[int]


class GMObject:
    def __init__(self) -> None:
        self.id: int = 0
        self.type: int = 0  # EGMType
        self.used_bone_count: int = 0
        self.used_bones: list[int] = [-1]*MAX_BONES  # MAX_BONES=28
        self.parent_id: int = 0
        self.parent_type: int = 0
        self.transform: Matrix = None
        self.bounds: Bounds = None
        self.opacity: bool = False
        self.bump: bool = False
        self.rigid: bool = False
        self.vertex_count: int = 0
        self.vertex_list_count: int = 0
        self.face_list_count: int = 0
        self.index_count: int = 0
        self.vertex_list: list[Vector3] = None
        self.vertices: list = None
        self.indices: list = None
        self.llb: list = None
        self.physique_vertices: list[int] = None
        self.material: bool = False
        self.material_count: int = 0
        self.materials: list[Material] = None
        self.material_block_count: int = 0
        self.material_blocks: list[MaterialBlock] = None
        self.frames: list[TMAnimation] = None
        self.light: bool = False


class LODGroup:
    def __init__(self):
        self.object_count: int = 0
        self.objects: list[GMObject] = None


class Object3D:
    def __init__(self) -> None:
        self.id: int = 0
        self.forces: list[Vector3] = [Vector3()]*4
        self.src_iu: float = 0
        self.src_iv: float = 0
        self.bounds: Bounds = None
        self.per_slerp: float = 0
        self.frame_count: int = 0
        self.event_count: int = 0
        self.events: list[Vector3] = None
        self.coll_obj: GMObject = None
        self.lod: bool = False
        self.bone_count: int = 0
        self.lod_groups: list[LODGroup] = [LODGroup()]*3
        self.attributes: list[AnimAttribute] = None
        self.base_bones: list[Matrix] = None
        self.base_inv_bones: list[Matrix] = None
        self.motions: Animation = None
        self.send_vs: bool = False


class NormalVertex:
    def __init__(self) -> None:
        self.p: Vector3 = Vector3()
        self.n: Vector3 = Vector3()
        self.t: Vector2 = Vector2()


class SkinVertex(NormalVertex):
    def __init__(self):
        super().__init__()
        self.w1: float = 0
        self.w2: float = 0
        self.id1: int = 0
        self.id2: int = 0


class AnimEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            print("MyEncoder-datetime.datetime")
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        if isinstance(obj, bytes):
            return str(obj, encoding='utf-8')
        if isinstance(obj, int):
            return int(obj)
        elif isinstance(obj, float):
            return float(obj)
        elif isinstance(obj, AnimAttribute):
            return obj.__dict__
        else:
            return super(AnimEncoder, self).default(obj)
