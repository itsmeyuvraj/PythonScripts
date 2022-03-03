import cv2
import os
import traceback

path = "D:\\FinalForgery\\Copymove\\bwsrc\\"
#Path of input image folder   
output_path = "D:\\FinalForgery\\Copymove\\Convertimagesintoxeroxaftermanipulatingdetailsonimage\\"
#PAth of output foldr(where you want to save images)

dirs = os.listdir(path)
for i in range(len(dirs)):
    print("processing ",dirs[i])
    try:         
        img_grey = cv2.imread(os.path.join(path,dirs[i]), cv2.IMREAD_GRAYSCALE)
        thresh = 128
        img_binary = cv2.threshold(img_grey, thresh, 255, cv2.THRESH_BINARY)[1]
        cv2.imwrite(os.path.join(output_path+dirs[i].split('.')[0]+'.png'),img_binary)
    except:
        traceback.print_exc()
        continue
