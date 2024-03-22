import fbx

# 假设fbx_sdk_module是已经导入的FBX SDK模块
fbx_sdk_module = fbx  # 实际上需要通过正确路径导入FBX SDK模块


def load_and_parse_normals(fbx_file_path):
    # 创建一个FBX管理器
    manager = fbx_sdk_module.FbxManager.Create()

    # 初始化IO插件以加载FBX文件
    io_plugin = fbx_sdk_module.FbxIOSettings.Create(
        manager, fbx_sdk_module.IOSROOT)
    manager.SetIOSettings(io_plugin)

    # 创建一个FBX场景
    scene = fbx_sdk_module.FbxScene.Create(manager, "MyScene")

    # 加载FBX文件到场景
    importer = fbx_sdk_module.FbxImporter.Create(manager, "")
    if not importer.Initialize(fbx_file_path, -1, manager.GetIOSettings()):
        raise Exception("Failed to initialize FBX importer.")
    importer.Import(scene)
    importer.Destroy()

    # 遍历场景中的所有节点
    root_node = scene.GetRootNode()
    revers_polygon_vertex(fbx_file_path, root_node)
    # node_count = root_node.GetChildCount()
    # for node_index in range(node_count):
    #     node = root_node.GetChild(node_index)
    #     # 检查节点是否包含网格对象
    #     mesh = node.GetMesh()
    #     mesh_arrtibute = node.GetNodeAttribute()
    # display_polygons(mesh_arrtibute)
    # if mesh is not None:
    #     point_count = mesh.GetControlPointsCount()
    #     # mesh_normal = mesh.GetElementNormal(0)
    #     # da = mesh_normal.GetDirectArray()
    #     # ia = mesh_normal.GetIndexArray()

    #     layer_count = mesh.GetLayerCount()

    #     for layer_index in range(layer_count):
    #         layer = mesh.GetLayer(layer_index)
    #         if layer is not None:
    #             normals = layer.GetNormals()

    #             # print(layer.GetName())

    #             direct_array = normals.GetDirectArray()
    #             direct_count = direct_array.GetCount()
    #             for direct_index in range(direct_count):
    #                 direct = direct_array.GetAt(direct_index)
    #                 flip_direct = fbx.FbxVector4(-direct[0], -direct[1], -direct[2])
    #                 direct_array.SetAt(direct_index, flip_direct)

    # index_array = normals.GetIndexArray()
    # index_count = index_array.GetCount()
    # for index_index in range(0, index_count, 3):
    #     temp_index = index_array.GetAt(index_index)
    #     index_array.SetAt(
    #         index_index, index_array.GetAt(index_index + 2))
    #     index_array.SetAt(index_index + 2, temp_index)

    saveScene('{0}.fbx'.format(fbx_file_path), manager, scene, True)

    # 清理资源
    scene.Destroy()
    manager.Destroy()


def revers_polygon_vertex(file_name, node):
    if not node:
        return
    child_count = node.GetChildCount()
    for child_index in range(child_count):
        child_node = node.GetChild(child_index)
        revers_polygon_vertex(file_name, child_node)
    mesh = node.GetMesh()
    print(node.GetName())
    if not mesh:
        if node.GetName() != 'RootNode':
            raise Exception('{0} {1}no mesh'.format(file_name, node.GetName()))
        return
    uv_list = mesh.GetElementUV().GetIndexArray()
    uv_count = uv_list.GetCount()
    vertice_list = list(range(uv_count))
    for uv_index in range(0, uv_count, 3):
        uv = uv_list.GetAt(uv_index)
        uv_2 = uv_list.GetAt(uv_index+2)
        vertice_list[uv_index] = uv_2
        vertice_list[uv_index + 1] = uv_list.GetAt(uv_index + 1)
        vertice_list[uv_index + 2] = uv#-(uv + 1)

        uv_list.SetAt(uv_index, uv_2)
        uv_list.SetAt(uv_index + 2, uv)

    # r = mesh.RemovePolygon(0)
    # while r >= 0:
    #     r = mesh.RemovePolygon(0)
    mesh.BeginPolygon(-1, -1, False)     
    vertices = mesh.GetPolygonVertices()   
    for i in range(len(vertice_list)):
        vertices[i] = vertice_list[i]
    mesh.EndPolygon()
    vertices21 = mesh.GetPolygonVertices()
    print(node.GetName())


def display_polygons(p_mesh):
    # vertices = p_mesh.GetPolygonVertices()
    # count = len(vertices)
    # for vertices_index in range(0, count, 3):
    #     print(vertices[vertices_index])
    #     v = vertices[vertices_index]
    #     vertices[vertices_index] = vertices[vertices_index + 2]
    #     vertices[vertices_index + 2] = v
    # vertices2 = p_mesh.GetPolygonVertices()
    # print(vertices, vertices2)
    polygon_count = p_mesh.GetPolygonCount()
    for polygon_index in range(polygon_count):
        polygon_size = p_mesh.GetPolygonSize(polygon_index)

        for polygon_size_index in range(0, polygon_size, 3):
            vertex_index = p_mesh.GetPolygonVertex(
                polygon_index, polygon_size_index)
            vertex_index_2 = p_mesh.GetPolygonVertex(
                polygon_index, polygon_size_index + 2)
            pi = p_mesh.GetPolygonVertexIndex(polygon_size_index)
        p_mesh.SetPolygonVertex(
            polygon_index, polygon_size_index, vertex_index_2)
        p_mesh.SetPolygonVertex(
            polygon_index, polygon_size_index + 2, vertex_index)
        print(vertex_index)


def saveScene(pFilename, pFbxManager, pFbxScene, pAsASCII=False):
    ''' Save the scene using the Python FBX API '''
    exporter = fbx.FbxExporter.Create(pFbxManager, '')

    if pAsASCII:
        # DEBUG: Initialize the FbxExporter object to export in ASCII.
        asciiFormatIndex = getASCIIFormatIndex(pFbxManager)
        isInitialized = exporter.Initialize(pFilename, asciiFormatIndex)
    else:
        isInitialized = exporter.Initialize(pFilename)

    if (isInitialized == False):
        raise Exception('Exporter failed to initialize. Error returned: ' +
                        str(exporter.GetStatus().GetErrorString()))

    exporter.Export(pFbxScene)

    exporter.Destroy()


def getASCIIFormatIndex(pManager):
    ''' Obtain the index of the ASCII export format. '''
    # Count the number of formats we can write to.
    numFormats = pManager.GetIOPluginRegistry().GetWriterFormatCount()

    # Set the default format to the native binary format.
    formatIndex = pManager.GetIOPluginRegistry().GetNativeWriterFormat()

    # Get the FBX format index whose corresponding description contains "ascii".
    for i in range(0, numFormats):

        # First check if the writer is an FBX writer.
        if pManager.GetIOPluginRegistry().WriterIsFBX(i):

            # Obtain the description of the FBX writer.
            description = pManager.GetIOPluginRegistry().GetWriterFormatDescription(i)

            # Check if the description contains 'ascii'.
            if 'ascii' in description:
                formatIndex = i
                break

    # Return the file format.
    return formatIndex


# 使用函数解析FBX文件中的法线数据
load_and_parse_normals('Ctrl_MaFlPrMarseItemBox-02.FBX')
