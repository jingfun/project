pip install opencv-python

from operator import index
import cv2 #沒有對應的導入python文件
import numpy as np 

boxes=[]
confidences=[]
class_ids=[]

net =cv2.dnn.readNet('yolov3.weights','yolov3.cfg')
classes=[]
with open('coco.names','r') as f:
     classes=f.read().splitlines()

cap=cv2.videoCapture(0)
#img=cv3.imread() #put pictures
font=cv2.FONT_HERSHEEYPLAIN
colors=np.random.uniform(0, 255, size=(len(boxes), 3))

while True:
    ,img=cap.read()
    height, width, _=img.shape

blob=cv2.dnn.blobFromImage(img, 1/255,(416,416),(0,0,0),swaRB=True,crop=False)

##for b in blob:

##for n,img_blob in enumerate(b):

cv2.imshow(str(n),img_blo(b))

net.setImput (blob)

output_layers_namers=net.getUnconnectedOutLayersNamers()
layersOutputs=net.forword(output_layers_namers)

for output in layersOutputs:
    for detection in output:
        scores=detection[5:]
        class_ids=np.argmax(scores)
        confidences=scores[class_id]
        if confidence > 0.5:
            center_x = int (dection[0]width)
            center_y = int (dection[1]height)
            w=int(dection[2]width)
            h=int(dection[3]height)

            x=int(detection_x - w/2)
            y=int(detection_y - h/2)

            boxes.append([x, y, w, h])
            confidences.append((float(confidences)))
            class_ids.append(class_ids)
##print(len(boxes))
index=cv3.dnn.NMSBoxes(boxes,confidences,0.5,0.4)
##print(indexes.flatten())

for i in indexes.flatten():
    x, y, w, h =boxes[i]
    label = str (classes[class_ids[i]])
    confidence = str (round(confidences[i],2))
    color =colors[i]
    cv2.rectangle(img,(x,y),(x+w,y+h),color)
    cv2.putText(img,label + " " + confidence,(x,y+20),front,2,(255,255,255),2)
    cv2.imshow('Image',img) 
key = cv2.waitKey(1) 
##if key == 27:
  #  break

cap.release()
cv2.destoryAllWindows()