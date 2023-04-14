import os
from PIL import Image

photos_dir_name = 'photos_for_lab3'  # directory names
textures_dir_name = 'textures'
cut_size = 128                       # size of samples in x and y

for photo_name in os.listdir(photos_dir_name):
    photo_name_without_JPEG = photo_name.split(".")[0]              # cut file extension
    photo_path = os.path.join(photos_dir_name, photo_name)          # create path to photo
    texture_dir_path = os.path.join(textures_dir_name, photo_name_without_JPEG)  # create path to texture directory

    try:                                                            # try to create directory for textures
        os.mkdir(texture_dir_path)
    except FileExistsError:
        print('Error: Texture directory already exists')

    photo = Image.open(photo_path)                  # open photo
    num_of_x_cut = round(photo.size[0] / cut_size)  # calculate the amount of cuts in x and y
    num_of_y_cut = round(photo.size[1] / cut_size)

    for x in range(num_of_x_cut):
        for y in range(num_of_y_cut):
            texture_name = photo_name_without_JPEG + str(x) + '_' + str(y) + '.jpg'     # create name for texture sample
            cropped_image = photo.crop((y * cut_size, x * cut_size, (y + 1) * cut_size, (x + 1) * cut_size))
            path = os.path.join(textures_dir_name, photo_name_without_JPEG, texture_name)  # create path to photo
            cropped_image.save(path)                                                       # save cropped photo
