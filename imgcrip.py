import cv2

def get4PlatesFromAImage(filename, x, y, width, height):
    """
    スキャン画像から4つのプレートを切り出す
    img = img[y:y+height,x:x+width]

    Parameters
    ----------
    filename : char
        画像の名前
    x : int x[4]
        プレートのX座標
    y : int y[4]
        プレートのy座標
    width : int width[4]
        プレートのwidth座標
    height : int height[4]
        プレートのheight座標
    """
    img = cv2.imread(filename)
    for i in range(4):
        plate = img[y[i]:y[i]+height[i],x[i]:x[i]+width[i]]
        plate= cv2.rotate(plate, cv2.ROTATE_90_COUNTERCLOCKWISE) #反時計回りに９０度回転
        plateName = "t{}.jpg".format(i+1)
        cv2.imwrite(plateName, plate)

if __name__ == '__main__':
    x = [204, 204, 1823, 1824]
    y = [47, 2063, 42, 2063]
    width = [1302, 1302, 3129, 3122]
    height = [1945, 3961, 1940, 3961]

    get4PlatesFromAImage("./scanimg.jpg", x, y, width, height)
