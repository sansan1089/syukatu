import os
import cv2
import numpy as np

class ImageIO:
    #グレースケールで画像を読み込む
    def readGRAYImage(self,fileName):
        try:
            img=cv2.imread(fileName,cv2.IMREAD_GRAYSCALE)
            return img
        except Exception as e:
            print(e)
            return None
    
    #カラースケールで画像を読み込む
    def readCOLORImage(self,fileName):
        try:
            img=cv2.imread(fileName)
            return img
        except Exception as e:
            print(e)
            return None