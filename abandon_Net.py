from case4gs_data import case4gs
import networkx as nx

'''
创建图节点
1、每一个节点有两个参数'y_gnd'和's_net'；他们分别表示 支路的对地导纳和节点的净流入功率
2、图为无向图
'''
G = nx.Graph()
nodes = case4gs.bus[:, 0]
nodes = nodes.astype(int)
G.add_nodes_from(nodes)
for i_node in nodes:  # 为nodes节点添加初值，否则后面的+=使用不了
    G.nodes[i_node]['y_gnd'] = 0
    G.nodes[i_node]['s_net'] = 0  # 发电机和负载总和

# set branch
branchs = case4gs.branch[:, 0:2]
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
z_branchs = case4gs.branch[:, 2] + case4gs.branch[:, 3] * 1j
y_gnds = case4gs.branch[:, 4]
z_tansformers = case4gs.branch[:, 8]
for i_branch, zi_branch, zi_tansformer, yi_gnd in zip(branchs, z_branchs, z_tansformers, y_gnds):
    if zi_tansformer == 0:
        G.edges[i_branch]['y_branch'] = 1. / (zi_branch)
        G.nodes[i_branch[0]]['y_gnd'] += yi_gnd / 2
        G.nodes[i_branch[1]]['y_gnd'] += yi_gnd / 2

    else:
        G.edges[i_branch]['y_branch'] = 1. / (zi_tansformer * zi_branch)
        G.nodes[i_branch[0]]['y_gnd'] += 1. / ((zi_tansformer ^ 2 * zi_branch) / (1 - zi_tansformer))
        G.nodes[i_branch[1]]['y_gnd'] += 1. / ((zi_tansformer * zi_branch) / (zi_tansformer - 1))

# set gens

s_gen = case4gs.gen[:, 1] + case4gs.gen[:, 2]
node_gen = case4gs.gen[:, 0]
for node, si_gen in zip(node_gen, s_gen):
    G.nodes[node]['s_net'] += si_gen

# set loads
