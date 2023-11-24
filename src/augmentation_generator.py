import os
import random
import os 
from scipy.ndimage import rotate
from albumentations.augmentations.crops.transforms import CropNonEmptyMaskIfExists, RandomCrop
import albumentations as A

# AUGUMENTATION
IMAGES_TO_GENERATE = 1000

images_path = '../train/images'
mask_path = '../train/masks'

img_aug_path = './AUG_DATA/train'
mask_aug_path = './AUG_DATA/masks'

images= []
masks = []

for im in os.listdir(images_path):
    images.append(os.path.join(images_path,im))
for msk in os.listdir(mask_path):
    masks.append(os.path.join(mask_path,msk))

aug = A.Compose([
    A.VerticalFlip(p=0.5),
    A.RandomRotate90(p=0.5),
    A.HorizontalFlip(p=1),
    A.Transpose(p=1),
    A.GridDistortion(p=1),
    CropNonEmptyMaskIfExists(p=0.3,height=512,width=512),
    A.geometric.rotate.Rotate (limit=90, interpolation=1, border_mode=4, value=None, mask_value=None, always_apply=False, p=0.5),
])

i=1

while i<=IMAGES_TO_GENERATE:
    number= random.randint(0,len(images)-1)
    image = images[number]
    mask = masks[number]
    print(image,mask)
    original_image =io.imread(image)
    original_mask =io.imread(mask)    
    augmented = aug(image=original_image,mask=original_mask)
    transformed_image = augmented['image']
    transformed_mask = augmented['mask']    
    
    new_image_path ='%s/%s.png'%(img_aug_path,i) 
    new_mask_path ='%s/%s.png'%(mask_aug_path,i) 
    print(new_image_path)
    io.imsave(new_image_path,transformed_image)
    io.imsave(new_mask_path,transformed_mask)
    i=i+1