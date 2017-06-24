import skimage, numpy as np, cv2 as cv, matplotlib.pyplot as plt
from skimage import feature

def GLCM(img, distance_vector, angle_vector):
    return skimage.feature.greycomatrix(img, distance_vector, angle_vector, levels=None, symmetric=False, normed=True)

def GLCM_Properties(GLCM, property):
    return skimage.feature.greycoprops(GLCM, prop=property)

img1 = np.array(cv.imread('image1.png',0))
img2 = np.array(cv.imread('image2.png',0))

GLCM_1 = GLCM(img1, [1], [0])
GLCM_2 = GLCM(img2, [1], [0])

Energy_1 = GLCM_Properties(GLCM_1, 'energy')
Energy_2 = GLCM_Properties(GLCM_2, 'energy')

print('Energy of img 1: ', float(Energy_1))
print('Energy of img 2: ', float(Energy_2))

Contrast_1 = GLCM_Properties(GLCM_1, 'contrast')
Contrast_2 = GLCM_Properties(GLCM_2, 'contrast')

print('Contrast of img 1: ', float(Contrast_1))
print('Contrast of img 2: ', float(Contrast_2))

Dissimilarity_1 = GLCM_Properties(GLCM_1, 'dissimilarity')
Dissimilarity_2 = GLCM_Properties(GLCM_2, 'dissimilarity')

print('Dissimilarity of img 1: ', float(Dissimilarity_1))
print('Dissimilarity of img 2: ', float(Dissimilarity_2))

Homogeneity_1 = GLCM_Properties(GLCM_1, 'homogeneity')
Homogeneity_2 = GLCM_Properties(GLCM_2, 'homogeneity')

print('Homogeneity of img 1: ', float(Homogeneity_1))
print('Homogeneity of img 2: ', float(Homogeneity_2))

Correlation_1 = GLCM_Properties(GLCM_1, 'correlation')
Correlation_2 = GLCM_Properties(GLCM_2, 'correlation')

print('Correlation of img 1: ', float(Correlation_1))
print('Correlation of img 2: ', float(Correlation_2))

ASM_1 = GLCM_Properties(GLCM_1, 'ASM')
ASM_2 = GLCM_Properties(GLCM_2, 'ASM')

print('ASM of img 1: ', float(ASM_1))
print('ASM of img 2: ', float(ASM_2))