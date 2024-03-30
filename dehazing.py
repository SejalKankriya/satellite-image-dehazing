#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import matplotlib.pyplot as plt  
import numpy as np
import tensorflow as tf
import cv2
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

# Load the saved model 
model_path = './AOD_Net_reg.h5'
model = tf.keras.models.load_model(model_path)

# Create the Tkinter UI
root = Tk()
root.title('Dehazing App')
root.geometry('1250x800')

# Define a function to handle the "Choose Image" button click event
def choose_image():
    # Show the file dialog to choose an image file
    file_path = filedialog.askopenfilename()
    
    # Load the image and preprocess it
    img = cv2.imread(file_path)
    size = (512, 512)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, size) / 255.0
    
    # Use the model to dehaze the image
    dehazed_img = model.predict(np.expand_dims(img, axis=0))[0] 
    
    # Postprocess the dehazed image
    dehazed_img = np.clip(dehazed_img * 255.0, 0, 255).astype(np.uint8) 
    
    # Show the original and dehazed images in the UI
    original_image = ImageTk.PhotoImage(Image.open(file_path))
    dehazed_image = ImageTk.PhotoImage(Image.fromarray(dehazed_img))
    
    # Update the labels with the original and dehazed images
    input_image_label.config(image=original_image)
    dehazed_image_label.config(image=dehazed_image)
    
    # Set the labels' image attributes to avoid garbage collection
    input_image_label.image = original_image
    dehazed_image_label.image = dehazed_image
    
    # Update the status label
    status_label.config(text='Dehazing complete!')

# Create the "Choose Image" button and add it to the UI
choose_image_button = Button(root, text='Choose Image', command=choose_image)
choose_image_button.pack()

# Create labels to display the original and dehazed images in the UI
input_image_label_disp = Label(root, text='Input Image', font=('Helvetica', 20))
input_image_label_disp.place(x=200, y=80)

dehazed_image_label_disp = Label(root, text='Dehazed Image', font=('Helvetica', 20))
dehazed_image_label_disp.place(x=900, y=80)

input_image_label = Label(root, padx=280, pady=280)
input_image_label.pack(side='left')
dehazed_image_label = Label(root,  padx=20, pady=20)
dehazed_image_label.pack(side='right')

# Create a status label to display messages to the user
status_label = Label(root, text='', font=('Arial', 20), fg='green')
status_label.place(x=500, y=100)

# Run the Tkinter main loop
root.mainloop()

