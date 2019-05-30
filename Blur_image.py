
# coding: utf-8

# In[1]:


import cv2


# In[2]:


minion=cv2.imread('stuartrob.jpg')
cv2.imshow('minions',minion)
cv2.waitKey(0)
cv2.destroyAllWindows()


# #  1. whole image blur

# In[3]:


blur_image=cv2.blur(minion,(15,15))
cv2.imshow('blured',blur_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[4]:


minion.shape


# # 2. Only particular area not blur rest all blur and Particular area blur
# 

# In[7]:


import numpy as np
blur_image=cv2.blur(minion,(15,15))

mask=np.zeros((478,480,3),dtype=np.uint8)
mask=cv2.circle(mask, (100,100) , 100, [255,255,255],-1)

out=np.where(mask==np.array([255,255,255]),minion,blur_image)   #paticular area not blur rest all blur
out1=np.where(mask==np.array([255,255,255]),blur_image,minion)  #particular area blur

cv2.imshow('blured',out)
cv2.imshow('Blured',out1)
cv2.waitKey(0)
cv2.destroyAllWindows()

