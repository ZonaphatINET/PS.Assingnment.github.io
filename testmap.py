import networkx as nx

# สร้างกราฟ
G = nx.Graph()

# เพิ่ม node พร้อมกำหนด attribute
G.add_node(1, name='Node 1', weight=10)
G.add_node(2, name='Node 2', weight=5)

# เข้าถึง attribute ของ node
print(G.nodes[1]['name'])  # ผลลัพธ์: Node 1
print(G.nodes[2]['weight'])  # ผลลัพธ์: 5