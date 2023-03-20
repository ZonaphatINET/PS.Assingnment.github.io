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
G.add_edge('1', '2', weigth =4)#, weight=4
G.add_edge('1', '3')
G.add_edge('1', '18')

G.add_edge('2', '1')
G.add_edge('2', '3')
G.add_edge('2', '4')
G.add_edge('2', '16')
G.add_edge('2', '17')
G.add_edge('2', '18')

G.add_edge('3', '1')
G.add_edge('3', '2')
G.add_edge('3', '4')
G.add_edge('3', '5')

G.add_edge('4', '2')
G.add_edge('4', '3')
G.add_edge('4', '5')

G.add_edge('5', '3')
G.add_edge('5', '4')
G.add_edge('5', '6')

G.add_edge('6', '7')

G.add_edge('7', '8')
G.add_edge('7', '9')
G.add_edge('7', '12')

G.add_edge('8', '7')
G.add_edge('8', '15')

G.add_edge('9', '7')
G.add_edge('9', '10')
G.add_edge('9', '11')
G.add_edge('9', '12')

G.add_edge('10', '9')
G.add_edge('10', '11')
G.add_edge('10', '13')
G.add_edge('10', '14')

G.add_edge('11', '9')
G.add_edge('11', '10')
G.add_edge('11', '13')

G.add_edge('12', '7')
G.add_edge('12', '9')

G.add_edge('13', '10')
G.add_edge('13', '11')
G.add_edge('13', '14')

G.add_edge('14', '10')
G.add_edge('14', '13')
G.add_edge('14', '15')
G.add_edge('14', '21')

G.add_edge('15', '8')
G.add_edge('15', '14')
G.add_edge('15', '16')

G.add_edge('16', '2')
G.add_edge('16', '15')

G.add_edge('17', '2')
G.add_edge('17', '18')

G.add_edge('18', '1')
G.add_edge('18', '2')
G.add_edge('18', '17')
G.add_edge('18', '19')
G.add_edge('18', '21')

G.add_edge('19', '18')
G.add_edge('19', '20')
G.add_edge('19', '21')

G.add_edge('20', '19')

G.add_edge('21', '14')
G.add_edge('21', '18')
G.add_edge('21', '19')

# แสดงกราฟ
pos = nx.spring_layout(G)

    # กำหนดตำแหน่งของโหนด
pos = {'1': (0, 0), '2': (-1, 1), '3': (0, 1), '4': (1, 1), '5': (0, 2), '6': (0, 3), '7': (-1, 3), '8': (-2, 4), '9': (-1, 4), '10': (-2, 5), '11': (-1, 5), '12': (-2, 3), '13': (-2, 6), '14': (-1, 6), '15': (-3, 4), '16': (-3, 3), '17': (-2, 0), '18': (-1, 0), '19': (-2, -1), '20': (-3, -1), '21': (-2, 7)}

nx.draw(G, pos, with_labels=True)
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
plt.show()

# ระบุจุดเริ่มและสิ้นสุด
startPoint = str(input("Enter start point:"))
endPoint = str(input("Enter end point:"))

# ระบุจุดจากที่หนึ่งไปยังอีกที่ว่าผ่านจุดใดบ้าง
path = nx.shortest_path(G, startPoint, endPoint)
print(path)

path = nx.shortest_path(G, source=startPoint, target=endPoint)

# แสดงกราฟที่ระบุเส้นทางแล้ว
pos = nx.spring_layout(G)

 # กำหนดตำแหน่งของโหนด
pos = {'1': (0, 0), '2': (-1, 1), '3': (0, 1), '4': (1, 1), '5': (0, 2), '6': (0, 3), '7': (-1, 3), '8': (-2, 4), '9': (-1, 4), '10': (-2, 5), '11': (-1, 5), '12': (-2, 3), '13': (-2, 6), '14': (-1, 6), '15': (-3, 4), '16': (-3, 3), '17': (-2, 0), '18': (-1, 0), '19': (-2, -1), '20': (-3, -1), '21': (-2, 7)}

nx.draw(G, pos, with_labels=True, edge_color='gray')  # ให้สีเส้นเป็นสีเทา
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)

# เปลี่ยนสีของเส้นทางที่ผ่านไปทั้งหมดใน path เป็นสีแดง
for i in range(len(path)-1):
    nx.draw_networkx_edges(G, pos, edgelist=[(path[i], path[i+1])], edge_color='red', width=2.0)
plt.show()
