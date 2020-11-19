'''
    Keras - Open Source Nueral Network Library
    Sequential - Pre Built Class To Add Layers And Train
                Models
    Conv2D - Used To Extract Features From The Given Image
    MaxPooling2D - Resises Image Dimensions Without Reducing
                The Features Of The Image
    Dropout - Reduces The Over Fitting Of Image By Dropping 
                Some Nuerons
    Flatten - Converts The Multi-Dimensional Arrays Into
                Single Vector
    Dense - Neural Network Layer In Which Each Input Nueron
            Is Connected To The Output Nueron
    Adam - Optimiser Used To Compile The Model
    ImageDataGenerator - Increases Available Examples Using 
                The Existing Datasets
'''
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dropout, Flatten, Dense
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import numpy as np
import matplotlib.pyplot as plt
import kaggle
import os
import matplotlib.image as mpimg

# Dataset Locations
main_dir = "New Masks Dataset"
train_dir = os.path.join(main_dir,"Train")
test_dir = os.path.join(main_dir,"Test")
valid_dir = os.path.join(main_dir,"Validation")

train_mask_dir = os.path.join(train_dir,'Mask')
train_nomask_dir = os.path.join(train_dir,'Non Mask')

train_mask_names = os.listdir(train_mask_dir)
train_nomask_names = os.listdir(train_nomask_dir)

#Visulaising Image
nrows = ncols = 4
plt.figure(figsize=(12,12))

mask_pic = [os.path.join(train_mask_dir,i) for i in train_mask_names[:8]]
nomask_pic = [os.path.join(train_nomask_dir,i) for i in train_nomask_names[:8]]
merge_list = mask_pic + nomask_pic

for i in range(len(merge_list)):
    data = merge_list[i].split('\\',2)[-1]
    sp = plt.subplot(nrows,ncols,i+1)
    sp.axis("off")
    image = mpimg.imread(merge_list[i])
    sp.set_title(data,fontsize=12)
    plt.imshow(image,cmap="gray")

# Data Generators
train_datagen = ImageDataGenerator(rescale=1./255,zoom_range=0.2,rotation_range=40,horizontal_flip=True)
test_datagen = ImageDataGenerator(rescale=1./255)
validation_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(train_dir,target_size=(150,150),batch_size=32,class_mode="binary")
test_generator = test_datagen.flow_from_directory(test_dir,target_size=(150,150),batch_size=32,class_mode="binary")
valid_generator = validation_datagen.flow_from_directory(valid_dir,target_size=(150,150),batch_size=32,class_mode="binary")

# Building Model
model = Sequential()

# Convultional Layer 1
model.add(Conv2D(32,(3,3),padding='SAME',activation='relu',input_shape=(150,150,3)))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.5))

# Convultional Layer 2
model.add(Conv2D(64,(3,3),padding='SAME',activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.5))

# Flattening
model.add(Flatten())

# Dense Layer
model.add(Dense(256,activation="relu"))
model.add(Dropout(0.5))

# Output Layer
model.add(Dense(1,activation="sigmoid"))
model.summary()

# Compiling The Model
model.compile(Adam(lr=0.001),loss="binary_crossentropy",metrics=['accuracy'])

# Training The Model
model.fit(train_generator,epochs=30,validation_data=valid_generator)

# Saving The Model
model.save("model.h5")
