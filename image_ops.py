
# coding: utf-8

# In[8]:


import cv2


# In[9]:


# describing version
print(cv2.__version__)


# In[10]:


#search for camera handling function
x=[i for i in dir(cv2) if 'Video' in i]
print(x)


# In[15]:


#starting videocapture
cap=cv2.VideoCapture(0)  # data live,stored,streaming
# or
#cap=cv2.VideoCapture('D:\DCIM\IMG_2541.JPG')
print(dir(cap))  #exploring camera operations


# In[16]:


#checking camera startpoint
while cap.isOpened():
    status,img=cap.read()
    #changing image to gray scale
    grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # now showing image
    cv2.imshow('live',img)
    #cv2.imshow('gray',graying)
    # 10ms window close keyboard action capture, ord==ascii values --q
    if cv2.waitKey(15) & 0xff==ord('q'):
        break


# In[17]:


cv2.destroyAllWindows()
cap.release()

