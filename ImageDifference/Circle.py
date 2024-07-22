import cv2
import numpy as np
class Circle:
    count=0
    def writeCircle(self,diff,image_r):
        #2値化
        ret,diff=cv2.threshold(diff,30,255,cv2.THRESH_BINARY)

        #ガウシアンフィルタで平滑化
        diff=cv2.GaussianBlur(diff,(11,11),0)

        #輪郭検出 contourは座標、hierarchyは階層情報
        contours,hierarchy=cv2.findContours(diff,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        #for(int c=最初:i<contour(全ての座標に);i++)のような意味
        for c in contours:
            x,y,w,h=cv2.boundingRect(c) #cは上で検出した輪郭の左上の座標
            if w>30 and h> 30:
                cv2.ellipse(image_r,((x+(w//2),y+(h//2)),(w,h),0),(0,0,255),thickness=3) #求めたcをもとにして四角を描画する
                self.count=self.count+1

        return image_r
    
    def getCount(self):
        return self.count