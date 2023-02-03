'''
1、编写导纳矩阵
%输入case，输出导纳矩阵
2、功率节点方程
%输入case，输出节点方程
3、牛顿lpx法
%输入case，输出求解
'''
import networkx as nx
from Graph import get_Graoh
from case4gs_data import case4gs
from case2383wp_data import case2383wp


if __name__ == '__main__':
    case1 = case4gs
    case2 = case2383wp
    a1 = get_Graoh(case1)
    a2 = get_Graoh(case2)
    b = nx.convert_node_labels_to_integers(a2,1,'increasing degree')
    print('do a good job')




