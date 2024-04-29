import numpy as np

number_of_image = 88

num = np.random.permutation(number_of_image)
test_num = num[0 : int(number_of_image/10)]
train_num = num[int(number_of_image/10)+1 : number_of_image-2]
val_num = num[number_of_image-1]

train_path = 'data/ImageSets/Main/train.txt'
test_path = 'data/ImageSets/Main/test.txt'
val_path = 'data/ImageSets/Main/val.txt'

with open(test_path, 'w') as f:
    for i in range(np.size(test_num)):
        f.write(f"{test_num[i]}\n")

with open(train_path, 'w') as f:
    for i in range(np.size(train_num)):
        f.write(f"{train_num[i]}\n")

with open(val_path, 'w') as f:
        f.write(f"{val_num}\n")