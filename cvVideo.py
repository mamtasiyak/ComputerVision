
# coding: utf-8

# In[6]:


import cv2


# In[7]:


print(cv2.__version__)


# In[8]:


cap=cv2.VideoCapture(0)


# In[9]:


#while cap.isOpened():
i=0
while i<100:
    status,data=cap.read()
    print(len(data))
    status,frame=cap.read()
    #time to draw a line
    #   start point,end point ,color,   width of line
    cv2.line(frame,(0,0),(250,250),(0,0,255),1)
    # draw rectangle
    cv2.rectangle(frame,(300,300),(400,500),(100,255,50),4)
    cv2.rectangle(frame,(300,300),(200,300),(10,40,70),-1)
    #draw circle
    
    #now converting to gray scale
    gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    hsv_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    #checking frame size
    print(frame.shape)
    #now display frame
    cv2.imshow('live',frame)
    cv2.imshow('live1',gray_frame)
    cv2.imshow('live2',hsv_frame)  
    i=i+1
    if cv2.waitKey(10) & 0xff==ord('q'):    #here ord is for converting keys to ascii
        break
#destroying all windows having frames
cv2.destroyAllWindows()
#stoping camera
cap.release()  # now you can use the same camera for another app
    

