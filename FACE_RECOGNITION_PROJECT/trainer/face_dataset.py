import cv2 
import os 




cam = cv2.VideoCapture(0)
cam.set(3,640) #width
cam.set(4,480) #height

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

face_id = input("\n Enter user id and press enter")

print("\n Initializing face capture.Look rhe camera and wait ...")

count = 0
while(True):
    ret,img = cam.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray,1.3,5)
    
    for(x,y,w,h) in faces:
       cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
       count +=1
    
       cv2.imwrite("dataset/User."+str(face_id)+'.'+str(count)+".jpg",gray[y:y+h,x:x+w])    
       cv2.imshow("image",img)
    
    k = cv2.waitKey(10)& 0xff
    if k== 10:
        break

    elif count>= 31:
        break

print("\n Exixting program and clean stuff")
cam.release()
cv2.destroyAllWindows()    