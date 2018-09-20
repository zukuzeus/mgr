import ast
import os

listOfNames = ast.literal_eval(
    "['frame12.jpg', 'frame117.jpg', 'frame118.jpg', 'frame119.jpg', 'frame120.jpg', 'frame121.jpg', 'frame131.jpg', 'frame132.jpg', 'frame1166.jpg', 'frame1167.jpg', 'frame1168.jpg', 'frame1169.jpg', 'frame1170.jpg', 'frame1172.jpg', 'frame1173.jpg', 'frame1174.jpg', 'frame1175.jpg', 'frame1176.jpg', 'frame1177.jpg', 'frame1178.jpg', 'frame1179.jpg', 'frame1180.jpg', 'frame1181.jpg', 'frame1182.jpg', 'frame1183.jpg', 'frame1184.jpg', 'frame1185.jpg', 'frame1186.jpg', 'frame1187.jpg', 'frame1188.jpg', 'frame1189.jpg', 'frame1190.jpg', 'frame1191.jpg', 'frame1192.jpg', 'frame1193.jpg', 'frame1194.jpg', 'frame1195.jpg', 'frame1196.jpg', 'frame1197.jpg', 'frame1198.jpg', 'frame1199.jpg', 'frame1200.jpg', 'frame1201.jpg', 'frame1202.jpg', 'frame1203.jpg', 'frame1204.jpg', 'frame1205.jpg', 'frame1206.jpg', 'frame1207.jpg', 'frame1209.jpg', 'frame1301.jpg', 'frame1302.jpg', 'frame1303.jpg', 'frame1304.jpg', 'frame1305.jpg', 'frame1306.jpg', 'frame1307.jpg', 'frame1308.jpg', 'frame1309.jpg', 'frame1310.jpg', 'frame1311.jpg', 'frame1312.jpg', 'frame1313.jpg', 'frame1314.jpg', 'frame1315.jpg', 'frame1316.jpg', 'frame1317.jpg', 'frame1318.jpg', 'frame1319.jpg', 'frame1320.jpg']")

counter = 0
for file in listOfNames:
    os.rename(
        os.path.join("C:\mgr\mgr\project\porownanie_sieci\drDębski\groundtruth", str(file).replace(".jpg", ".txt")),
        os.path.join("C:\mgr\mgr\project\porownanie_sieci\drDębski"
                     "\groundtruth", 'frame{}.txt'.format(counter)))
    counter += 1
