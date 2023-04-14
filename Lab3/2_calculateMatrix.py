import os
import numpy as np
import pandas as pd
from PIL import Image
from skimage.feature import graycomatrix, graycoprops

textures_dir_name = 'textures'  # sample folder name
pixel_distances = [1, 3, 5]     # distances between pixels used for grey-level co-occurrence matrix
# angels used for grey-level co-occurrence matrix
angles = [0, np.pi / 4, np.pi / 2, (3 / 4) * np.pi]  # [0, 45, 90, 135 st]
data = pd.DataFrame()   # create data frame for results

for texture_folder in os.listdir(textures_dir_name):                        # list folders in textures folder
    texture_sample_path = os.path.join(textures_dir_name, texture_folder)   # create path to folder with sample
    for texture_sample in os.listdir(texture_sample_path):                  # list each sample in folder
        sample_path = os.path.join(texture_sample_path, texture_sample)
        sample = Image.open(sample_path)
        sample_gray = sample.convert('L')                                    # convert image sample to B-W image
        sample_gray_reduced = sample_gray.point(lambda x: int(x / 4))        # reduce the brightness depth to 5 bits
        sample_gray_array = np.array(sample_gray_reduced)                      # create array from B-W image

        # calculate the gray-level co-occurrence matrix
        glcm = graycomatrix(sample_gray_array, distances=pixel_distances, angles=angles, levels=64, symmetric=True)

        # create dictionary with calculated dissimilarity, correlation, contrast, energy, homogeneity, ASM
        new_row = {'category': texture_folder,
                   'dissimilarity': graycoprops(glcm, 'dissimilarity'),
                   'correlation': graycoprops(glcm, 'correlation'),
                   'contrast': graycoprops(glcm, 'contrast'),
                   'energy': graycoprops(glcm, 'energy'),
                   'homogeneity': graycoprops(glcm, 'homogeneity'),
                   'ASM': graycoprops(glcm, 'ASM')
                   }
        new_row_df = pd.DataFrame.from_dict(new_row, orient='index')  # create data frame from dictionary
        data = pd.concat([data, new_row_df])       # add new results data frame to other

data.to_csv('data.csv')     # save results to .csv file
print('done')