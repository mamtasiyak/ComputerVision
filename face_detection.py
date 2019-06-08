
# coding: utf-8

# In[2]:


import cv2


# In[3]:


facehaar=cv2.CascadeClassifier('face.xml')


# In[4]:


arya_image=cv2.imread('Arya.jpg',0)
#arya=arya_image[1000:3024,2000:4032]
print(arya_image.shape)


# In[13]:


#face detector apply in arya_img --scalling range
face_only=facehaar.detectMultiScale(arya_image,1.15,5)
print(face_only)
for x,y,w,h in face_only:
    cv2.rectangle(arya_image,(x,y),(x+w,y+h),(0,0,255),2)
    
#its normal display
cv2.imshow('all',arya_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[5]:


#starting camera
cap=cv2.VideoCapture(0)

while cap.isOpened():
    status,frame=cap.read()
    face_only=facehaar.detectMultiScale(frame,1.15,5)
    print(face_only)
    for x,y,w,h in face_only:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
    cv2.imshow('facedetect',frame)
    if cv2.waitKey(10) & 0xff == ord('q'):
        break
    
cv2.destroyAllWindows()
cap.release()


# In[6]:


frame.shape

