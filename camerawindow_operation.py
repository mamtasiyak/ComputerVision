
# coding: utf-8

# In[1]:


import cv2
import numpy as np


# # Same window multi image copy

# In[2]:


img=cv2.imread('Arya.jpg')

image=cv2.resize(img,(0,0),None,.50,.50)

numpy_horizontal=np.hstack((image,image))
numpy_horizontal_concat=np.concatenate((numpy_horizontal,numpy_horizontal),axis=0)

cv2.imshow('image',numpy_horizontal_concat)

cv2.waitKey(0)
cv2.destroyAllWindows


# In[3]:


image.shape


# # Same window (color, gray)

# In[ ]:


img=cv2.imread('Arya.jpg')

image=cv2.resize(img,(0,0),None,.50,.50)

gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
gray1=np.broadcast_to(gray[:,:,np.newaxis],(360,640,3))
numpy_horizontal=np.hstack((image,gray1))
numpy_horizontal_concat=np.concatenate((numpy_horizontal,numpy_horizontal),axis=0)
cv2.imshow('image',numpy_horizontal_concat)
#cv2.imshow('image',gray)
cv2.waitKey(0)
cv2.destroyAllWindows


# In[ ]:


cap=cv2.VideoCapture(0)
while cap.isOpened():
    status,frame=cap.read()  #start taking frames
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
   # gray_resize=cv2.resize(gray,(0,0),None,.50,.50)
    vdo=np.broadcast_to(gray[:,:,np.newaxis],(480,640,3)) 
    #gray_resize=cv2.resize(vdo,(0,0),None,.50,.50)
    newframe=np.concatenate((vdo,frame),axis=1)
    cv2.imshow('live',newframe)
    
    if cv2.waitKey(10) & 0xff == ord('q'):
        break
        
cv2.destroyAllWindows()
cap.release()


# In[ ]:


gray_resize.shape

