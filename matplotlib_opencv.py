import cv2 
import matplotlib.pyplot as plt
import numpy as np
img = cv2.imread("messi5.jpg", 0)
lap = cv2.Laplacian(img, cv2.CV_64F, )
lap = np.uint8(np.absolute(lap))


titles = ['image','lap']
images = [img,lap]
for i in range(2):
    plt.subplot(2,1,i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
    
plt.show()