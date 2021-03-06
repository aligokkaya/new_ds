from datetime import datetime
import requests
import cv2
now = datetime.now()
            # key = convertToBinaryData('./key_logs.txt')
            # system_ip=convertToBinaryData('./system_info.txt')
            # image=convertToBinaryData('./screenshots0.png')
frame=cv2.imread('sigara.png')
# cv2.imshow("frame",frame)
# cv2.waitKey(0)

frame=cv2.resize(frame,(848,480))
data2 = cv2.imencode(".jpg", frame)[1]

headers = {'Accept': 'application/json', }
textfile = {

'screen_image': ('image.jpg', data2.tobytes() , 'image/jpeg', {'Expires': '0'}),
'key_logs': "aaaaaaaaaaaaaa",
'system_info':"bbbbbbbbbbbbbbbbbbbbb",

}

data={
        'module_name': "Telephone Detection",
'notification_no':"06 HYPE 06",
'proffer':"https://www.mevzuat.gov.tr/File/GeneratePdf?mevzuatNo=16924&mevzuatTur=KurumVeKurulusYonetmeligi&mevzuatTertip=5",

"cam_no":"1",
"date":"2022-05-27 05:57:29",
"status":"detection"
}
try:
    response = requests.post('http://127.0.0.1:5000/api/file', files=textfile,headers=headers,data=data)
    if response.status_code==200:
        f=open('./key_logs.txt','w')
        f.write(" ")
        f.close()   
except Exception as e:
    print(e)