import os
import shutil
import random

# Path where your extracted frames are
SOURCE_FOLDER = 'frames'  # folder where all extracted images are
DEST_FOLDER = 'parking_dataset'
SPLIT_RATIO = 0.8  # 80% train, 20% val

# Create directory structure
for split in ['train', 'val']:
    os.makedirs(os.path.join(DEST_FOLDER, 'images', split), exist_ok=True)
    os.makedirs(os.path.join(DEST_FOLDER, 'labels', split), exist_ok=True)

# Get all image filenames
all_images = [f for f in os.listdir(SOURCE_FOLDER) if f.endswith('.jpg') or f.endswith('.png')]
random.shuffle(all_images)

# Split images
split_index = int(len(all_images) * SPLIT_RATIO)
train_images = all_images[:split_index]
val_images = all_images[split_index:]

# Move images
for img in train_images:
    shutil.copy(os.path.join(SOURCE_FOLDER, img), os.path.join(DEST_FOLDER, 'images/train', img))

for img in val_images:
    shutil.copy(os.path.join(SOURCE_FOLDER, img), os.path.join(DEST_FOLDER, 'images/val', img))

print(f"✅ Split complete! {len(train_images)} train and {len(val_images)} val images copied.")


