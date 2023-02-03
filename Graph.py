import networkx as nx
def get_Graoh(case):
    pass
    '''
    这一步创建图节点
    1、每一个节点有两个参数'y_gnd'和's_net'；他们分别表示 支路的对地导纳和节点的净流入功率
    2、后续还有增加节点参数'type'
    3、后续还会增加节点参数'U','theta'
    2、图为无向图
    '''
    G = nx.Graph()
    nodes = case.bus[:, 0]
    nodes = nodes.astype(int)
    G.add_nodes_from(nodes)
    for i_node in nodes:  # 为nodes节点添加初值，否则后面的+=使用不了
        G.nodes[i_node]['y_gnd'] = 0
        G.nodes[i_node]['s_net'] = 0  # 发电机和负载总和
        G.nodes[i_node]['U'] = 1
        G.nodes[i_node]['theta'] = 0

    # set branch
    branchs = case.branch[:, 0:2]
    branchs = branchs.astype(int)
    G.add_edges_from(branchs)

    '''
    set branchs'attrubutes
    这一步完成支路参数的编写
    1、线路支路阻抗
    2、线路旁路导纳归到节点的对地导纳上
    3、变压器支路阻抗
    4、变压器旁路导纳归到节点的对地导纳上
    '''
    z_branchs = case.branch[:, 2] + case.branch[:, 3] * 1j
    y_gnds = case.branch[:, 4]
    z_tansformers = case.branch[:, 8]
    for i_branch, zi_branch, zi_tansformer, yi_gnd in zip(branchs, z_branchs, z_tansformers, y_gnds):
        if zi_tansformer == 0:
            G.edges[i_branch]['y_branch'] = 1. / (zi_branch)
            G.nodes[i_branch[0]]['y_gnd'] += yi_gnd / 2
            G.nodes[i_branch[1]]['y_gnd'] += yi_gnd / 2

        else:
            G.edges[i_branch]['y_branch'] = 1. / (zi_tansformer * zi_branch)
            G.nodes[i_branch[0]]['y_gnd'] += 1. / ((zi_tansformer ** 2 * zi_branch) / (1 - zi_tansformer))
            G.nodes[i_branch[1]]['y_gnd'] += 1. / ((zi_tansformer * zi_branch) / (zi_tansformer - 1))


    '''
    这一步确定节点类型
    '''
    node_type = case.bus[:,1]
    node_of_type = case.bus[:,0] #节点编号
    for nodei_of_type,nodei_type in zip(node_of_type,node_type):
        G.nodes[nodei_of_type]['type'] = nodei_type

    # set gens
    '''
    这一步将发电机功率注入节点‘s_net’
    '''
    PQ_U = case.gen[:,5]
    s_gen = case.gen[:, 1] + case.gen[:, 2]*1j  #发电机功率
    node_gen = case.gen[:, 0]                   #有发电机的节点
    for nodei_gen, si_gen, PQi_U in zip(node_gen, s_gen,PQ_U):
        G.nodes[nodei_gen]['s_net'] += si_gen
        if G.nodes[nodei_gen]['type'] == 2:
            G.nodes[nodei_gen]['U'] == PQi_U

    '''
    这一步将负载注入节点's_net'
    '''
    s_load = case.bus[:,3] + case.bus[:,4]*1j
    node_load = case.bus[:,0]
    for si_load,nodei_load in zip(s_load,node_load):
        G.nodes[nodei_load]['s_net'] += si_load




    return G

    # set loads
