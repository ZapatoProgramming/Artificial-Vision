import cv2

logotwo_img = cv2.imread("datos/GettingStartedWithImages/logotwo_84x84.png", 1) 

window = cv2.namedWindow("logotwo", cv2.WINDOW_NORMAL)

## this while loop is to keep the window open until the user press the 'q' key
alive = True
while alive:
    cv2.imshow("logotwo", logotwo_img)
    key = cv2.waitKey(1000)
    if key == ord('q'):
        alive = False

cv2.destroyAllWindows()