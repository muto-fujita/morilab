import cv2
import numpy as np

def get4PlatesFromAImage(filename, x, y, width, height):
    """
    スキャン画像から4つのプレートを切り出す
    img = img[y:y+height,x:x+width]

    Parameters
    ----------
    filename : char
        画像の名前
    x : ndarray x[4]
        プレートのX座標
    y : ndarray y[4]
        プレートのy座標
    width : ndarray width[4]
        プレートのwidth座標
    height : ndarray height[4]
        プレートのheight座標
    """
    img = cv2.imread(filename)
    # カラーとグレースケールで場合分け
    if len(img.shape) == 3:
        img_height, img_width, channels = img.shape[:3]
    else:
        img_height, img_width = img.shape[:2]
        channels = 1

    # 切り出し座標を取得
    x = np.array(x * img_width, dtype=np.int32)
    y = np.array(y * img_height, dtype=np.int32)
    width = np.array(width * img_width, dtype=np.int32)
    height = np.array(height * img_height, dtype=np.int32)

    for i in range(4):
        plate = img[y[i]:y[i]+height[i],x[i]:x[i]+width[i]]
        plate= cv2.rotate(plate, cv2.ROTATE_90_COUNTERCLOCKWISE) #反時計回りに９０度回転
        plateName = "t{}.jpg".format(i+1)
        cv2.imwrite(plateName, plate)

if __name__ == '__main__':
    # 座標を割合で指定
    x = np.array([204, 204, 1823, 1824])/3200
    y = np.array([47, 2063, 42, 2063])/4000
    width = np.array([1302, 1302, 3129, 3122])/3200
    height = np.array([1945, 3961, 1940, 3961])/4000

    get4PlatesFromAImage("./scanimg.jpg", x, y, width, height)
