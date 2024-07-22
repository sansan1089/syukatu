import cv2
import numpy as np
from ImageIO import ImageIO
from Circle import Circle
from Output import Output

class Difference:
    def compareImages(self,image1_path,image2_path):

        #- - - - - ImageIOクラスを呼び出す - - - - -
        #グレースケールとカラースケールで画像ファイルを読み込む
        io=ImageIO()
        image_before=io.readCOLORImage(image1_path)
        image_result=io.readCOLORImage(image2_path)
        image1=io.readGRAYImage(image1_path)
        image2=io.readGRAYImage(image2_path)
        #- - - - - - - - - - - - - - - - - - - - -

        #それぞれの画像に処理を施す
        image1=self.imageProcessing(image1)
        image2=self.imageProcessing(image2)

        #⬆️の画像たちを差分化
        diff=cv2.absdiff(image1,image2)

        #- - - - - Circleクラスを呼び出す - - - - -
        #画像の間違い部分に丸を描画
        circle=Circle()
        image_result=circle.writeCircle(diff,image_result)
        #- - - - - - - - - - - - - - - - - - - - -

        #- - - - - Outputクラスを呼び出す - - - - -
        #print指示を出す
        output=Output()

        #もし丸を描画した回数が0回(間違いなし)なら"No Difference"と書かれた画像を表示
        #0回以上(間違いあり)なら二つの画像を並べて表示
        if circle.getCount()==0:
            output.wrongPrint(image_before,image_result)
        else:
            output.differencePrint(image_before,image_result)
        #- - - - - - - - - - - - - - - - - - - - -

    def imageProcessing(self,image):

        #ヒストグラム平滑化によりコントラストを上げる
            #終了したら上書き保存
        clahe=cv2.createCLAHE(clipLimit=30.0,tileGridSize=(10,10))
        processed_image=clahe.apply(image)

        #ガウシアンフィルタで平滑化してノイズを軽減する
            #終了したら上書き保存
        processed_image=cv2.GaussianBlur(processed_image,(13,13),0)

        return processed_image

            