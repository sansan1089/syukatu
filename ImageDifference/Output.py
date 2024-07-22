import cv2
import numpy as np
import os

class Output:
    def differencePrint(self, image_b, image_r):
        mergeImg = np.hstack((image_b, image_r))
        cv2.imwrite(os.path.join('uploads', 'result.png'), mergeImg)
        print("Image saved as result.png")  # デバッグ用プリント文

    def wrongPrint(self, image_b, image_r):
        image_w = cv2.putText(image_r, 'No Differences', (50, 50), cv2.FONT_HERSHEY_PLAIN, 4, (0, 0, 255), 5)
        mergeImg = np.hstack((image_b, image_w))
        cv2.imwrite(os.path.join('uploads', 'result.png'), mergeImg)
        print("No Differences image saved as result.png")  # デバッグ用プリント文
