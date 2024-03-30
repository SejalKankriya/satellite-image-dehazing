#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Import Library
import cv2
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt  
from skimage import io

# Load the saved model
model = tf.keras.models.load_model('AOD_Net_reg.h5')

# Load the hazy image
img = cv2.imread('test_dataset/0810.jpg')
size = (512,512)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = cv2.resize(img, size) / 255.0

# Use the model to dehaze the image
dehazed_img = model.predict(np.expand_dims(img, axis=0))[0] 

# Save the dehazed image
dehazed_img = np.clip(dehazed_img * 255.0, 0, 255).astype(np.uint8)
cv2.imwrite('dehazed_image.jpg', cv2.cvtColor(dehazed_img, cv2.COLOR_RGB2BGR))

fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(10, 10))
axs[1].imshow(dehazed_img)
axs[1].set_title('Predicted Dehazy Image')
axs[0].imshow(img)
axs[0].set_title('Hazy Image')
plt.show()