import networkx as nx
import matplotlib.pyplot as plt

# สร้างกราฟว่าง
G = nx.Graph()

# เพิ่ม node ลงในกราฟ
G.add_node('1')
G.add_node('2')
G.add_node('3')
G.add_node('4')
G.add_node('5')
G.add_node('6')
G.add_node('7')
G.add_node('8')
G.add_node('9')
G.add_node('10')
G.add_node('11')
G.add_node('12')
G.add_node('13')
G.add_node('14')
G.add_node('15')
G.add_node('16')
G.add_node('17')
G.add_node('18')
G.add_node('19')
G.add_node('20')
G.add_node('21')

# เพิ่ม edge ลงในกราฟ
G.add_edge('1', '2')#, weight=4
G.add_edge('1', '3')
G.add_edge('2', '3')

# แสดงกราฟ
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True)
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
plt.show()