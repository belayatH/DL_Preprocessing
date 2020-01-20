"""
Author: Belayat
Input: pass the dataset directory and text file of image path
Output: text files of image path: train.txt and val.txt
"""

import numpy as np

# split image into train- validation from all image paths
image_set_dir = './dataset/ImageSets'
trainval_file = image_set_dir+'/img_paths.txt'
train_file = image_set_dir+'/train.txt'
val_file = image_set_dir+'/val.txt'

idx = []
with open(trainval_file) as f:
  for line in f:
    idx.append(line.strip())
f.close()

idx = np.random.permutation(idx)

val_idx = sorted(idx[:len(idx)/2])
train_idx = sorted(idx[len(idx)/2:])

#train_idx = sorted(idx[:len(idx)/2])
#val_idx = sorted(idx[len(idx)/2:])

with open(train_file, 'w') as f:
  for i in train_idx:
    f.write('{}\n'.format(i))
f.close()

with open(val_file, 'w') as f:
  for i in val_idx:
    f.write('{}\n'.format(i))
f.close()

print('Trainining set is exported to ' + train_file)
print('Validation set is exported to ' + val_file)