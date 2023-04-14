import networkx as nx
import matplotlib.pyplot as plt

#หัวข้อกราฟ
plt.title('Tent sites in 3 provinces: PrachinBuri, NakhonRatchasima, and NakhonNayok.', size=10)

# สร้างกราฟว่าง
G = nx.Graph()

# เพิ่ม node ลงในกราฟ
G.add_node(1, name='บ้านริมน้ำบางแตน')
G.add_node(2, name='เขาอีโต้')
G.add_node(3, name='น้ำตกตะคร้อ')
G.add_node(4, name='๑๐๐ camping')
G.add_node(5, name='ทับลาน')
G.add_node(6, name='จิบแฟแลเขา Camping')
G.add_node(7, name='ผาเก็บตะวัน')
G.add_node(8, name='จุดสกัดเขาสูง')
G.add_node(9, name='วังน้ำเขียว')
G.add_node(10, name='ไร่ภูเริง')
G.add_node(11, name='อ่างห้วยยาง')
G.add_node(12, name='บ้านมาบกราด')
G.add_node(13, name='เขายายเที่ยง')
G.add_node(14, name='WILD CALLING Farm Park')
G.add_node(15, name='Area 25 Campsite')
G.add_node(16, name='ลำตะคอง')
G.add_node(17, name='วังบอน')
G.add_node(18, name='โก๋แคมป์')
G.add_node(19, name='สวนยายเภา')
G.add_node(20, name='คลองมะเดื่อ')
G.add_node(21, name='สวนคัยวะ')
G.add_node('PrachinBuri')
G.add_node('NakhonRatchasima')
G.add_node('NakhonNayok')

# เพิ่ม edge ลงในกราฟ
G.add_edge(1, 2, weight = 58)#, weight=4
G.add_edge(1, 3, weight = 62)
G.add_edge(1, 18, weight = 54)

G.add_edge(2, 1, weight = 58)
G.add_edge(2, 3, weight = 10)
G.add_edge(2, 4, weight = 30)
G.add_edge(2, 16, weight = 54)# เนื่องจากเป็นเส้นทางขึ้นเขาใช้ความเร็วได้ไม่เต็มที่จึงบวกเพิ่ม 5 กม. 
G.add_edge(2, 17, weight = 20)
G.add_edge(2, 18, weight = 36)

G.add_edge(3, 1, weight = 62)
G.add_edge(3, 2, weight = 10)
G.add_edge(3, 4, weight = 27)
G.add_edge(3, 5, weight = 78)

G.add_edge(4, 2, weight = 30)
G.add_edge(4, 3, weight = 27)
G.add_edge(4, 5, weight = 69)

G.add_edge(5, 3, weight = 78)
G.add_edge(5, 4, weight = 69)
G.add_edge(5, 6, weight = 17)

G.add_edge(6, 7, weight = 26)

G.add_edge(7, 8, weight = 42)
G.add_edge(7, 9, weight = 34)
G.add_edge(7, 12, weight = 153)

G.add_edge(8, 7, weight = 42)
G.add_edge(8, 15, weight = 32)

G.add_edge(9, 7, weight = 34)
G.add_edge(9, 10, weight = 46)
G.add_edge(9, 11, weight = 60)
G.add_edge(9, 12, weight = 120)

G.add_edge(10, 9, weight = 46)
G.add_edge(10, 11, weight = 74)
G.add_edge(10, 13, weight = 64)
G.add_edge(10, 14, weight = 60)

G.add_edge(11, 9, weight = 60)
G.add_edge(11, 10, weight = 74)
G.add_edge(11, 13, weight = 56)

G.add_edge(12, 7, weight = 153)
G.add_edge(12, 9, weight = 120)

G.add_edge(13, 10, weight = 64)
G.add_edge(13, 11, weight = 56)
G.add_edge(13, 14, weight = 58)

G.add_edge(14, 10, weight = 60)
G.add_edge(14, 13, weight = 58)
G.add_edge(14, 15, weight = 23)
G.add_edge(14, 21, weight = 78)

G.add_edge(15, 8, weight = 32)
G.add_edge(15, 14, weight = 23)
G.add_edge(15, 16, weight = 37)

G.add_edge(16, 2, weight = 54)
G.add_edge(16, 15, weight = 37)# เนื่องจากเป็นเส้นทางขึ้นเขาใช้ความเร็วได้ไม่เต็มที่จึงบวกเพิ่ม 5 กม. 

G.add_edge(17, 2, weight = 20)
G.add_edge(17, 18, weight = 25)

G.add_edge(18, 1, weight = 54)
G.add_edge(18, 2, weight = 36)
G.add_edge(18, 17, weight = 25)
G.add_edge(18, 19, weight = 13)
G.add_edge(18, 21, weight = 41)

G.add_edge(19, 18, weight = 13)
G.add_edge(19, 20, weight = 10)
G.add_edge(19, 21, weight = 40)

G.add_edge(20, 19, weight = 10)

G.add_edge(21, 14, weight = 78)
G.add_edge(21, 18, weight = 41)
G.add_edge(21, 19, weight = 40)

# กำหนดสีของโหนด
color_map = {1:'pink',
              2:'pink',
              3:'pink',
              4:'pink',
              5:'pink',
              6:'pink',
              'PrachinBuri':'pink',
              7:'orange',
              8:'orange',
              9:'orange',
              10:'orange',
              11:'orange',
              12:'orange',
              13:'orange',
              14:'orange',
              15:'orange',
              'NakhonRatchasima':'orange',
              16:'green',
              17:'green',
              18:'green',
              19:'green',
              20:'green',
              21:'green',
              'NakhonNayok':'green'}
                     
nx.set_node_attributes(G, color_map, 'color')

# วนลูปเพื่อกำหนดค่าสีให้กับโหนดที่ไม่มีค่าสี
for node in G.nodes():
    if node not in color_map:
        color_map[node] = 'blue'

# แสดงกราฟ
pos = nx.spring_layout(G)

# กำหนดตำแหน่งของโหนด
pos = {1: (-3.18, -3.74),
 2: (-1.7, 0.28),
  3: (-0.03, -1.14),
   4: (-0, 0.86),
    5: (2.586, 0.15),
     6: (2.852, 1.93),
      7: (2.75, 3.4),
       8: (1.05, 3.68),
        9: (1.33, 5.43),
         10: (-0.426, 6.12),
          11: (0.38, 9),
           12: (4.8, 4.50),
            13: (-1.56, 8.4),
             14: (-2.5, 6),
              15: (-0.76, 4.09),
               16: (-1.79, 3.12),
                17: (-2.39, 1.49),
                 18: (-4.5, 0.1),
                  19: (-3.84, 2.46),
                   20: (-4.01, 4.37),
                    21: (-5.42, 7.36),
                    'PrachinBuri':(.5, -2),
                    'NakhonRatchasima':(.50, -3),
                    'NakhonNayok':(0.5, -4)}

nx.draw(G, pos, with_labels=True, node_color=[color_map[node] for node in G.nodes()])
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
#plt.show()



# ระบุจุดเริ่มและสิ้นสุด
startPoint = int(input("Enter start point:"))
endPoint = int(input("Enter end point:"))

# ระบุจุดจากที่หนึ่งไปยังอีกที่ว่าผ่านจุดใดบ้าง
path = nx.shortest_path(G, startPoint, endPoint, weight='weight')
print(path)

path = nx.shortest_path(G, source=startPoint, target=endPoint, weight='weight')

# แสดงกราฟที่ระบุเส้นทางแล้ว
pos = nx.spring_layout(G)

# กำหนดตำแหน่งของโหนด
pos = {1: (-3.18, -3.74),
 2: (-1.7, 0.28),
  3: (-0.03, -1.14),
   4: (-0, 0.86),
    5: (2.586, 0.15),
     6: (2.852, 1.93),
      7: (2.75, 3.4),
       8: (1.05, 3.68),
        9: (1.33, 5.43),
         10: (-0.426, 6.12),
          11: (0.38, 9),
           12: (4.8, 4.50),
            13: (-1.56, 8.4),
             14: (-2.5, 6),
              15: (-0.76, 4.09),
               16: (-1.79, 3.12),
                17: (-2.39, 1.49),
                 18: (-4.5, 0.1),
                  19: (-3.84, 2.46),
                   20: (-4.01, 4.37),
                    21: (-5.42, 7.36),
                    'PrachinBuri':(.5, -2),
                    'NakhonRatchasima':(.50, -3),
                    'NakhonNayok':(0.5, -4)}

# หัวข้อกราฟ
plt.title('Tent sites in 3 provinces: PrachinBuri, NakhonRatchasima, and NakhonNayok.', size=10)

nx.draw(G, pos, with_labels=True, edge_color='gray', node_color=[color_map[node] for node in G.nodes()])  # ให้สีเส้นเป็นสีเทา
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)

# เปลี่ยนสีของเส้นทางที่ผ่านไปทั้งหมดใน path เป็นสีแดง
for i in range(len(path)-1):
    nx.draw_networkx_edges(G, pos, edgelist=[(path[i], path[i+1])], edge_color='red', width=2.0)  

# กำหนด path และชื่อไฟล์ที่ต้องการบันทึก    
filepath = 'img/outputMap/graph.png'

# บันทึกภาพกราฟลงไปยังโฟลเดอร์ที่กำหนด
plt.savefig(filepath, format='jpeg', dpi=1000)

#plt.savefig("graph.jpg", format='jpeg', dpi=600)#######ไม่ได้ใช้
plt.show()