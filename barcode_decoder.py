# -------------------------------------------- 
# DD - AI Powered Enterprise Search
# __author__ : Dnyaneshwar Dewadkar 
#            : 12:11 PM 27/01/21
#            : barcode_decoder.py 
#  
# --------------------------------------------


from pyzbar import pyzbar
import argparse
import cv2


# construct the argument parser and parse the arguments

def barcode(image_path):
    image = cv2.imread(image_path)
    barcodes = pyzbar.decode(image)
    for single_bar_code in barcodes:
        # extract the bounding box location of the barcode and draw the
        # bounding box surrounding the barcode on the image
        (x, y, w, h) = single_bar_code.rect
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
        # the barcode data is a bytes object so if we want to draw it on
        # our output image we need to convert it to a string first
        barcodeData = single_bar_code.data.decode("utf-8")
        barcodeType = single_bar_code.type
        # draw the barcode data and barcode type on the image
        text = "{} ({})".format(barcodeData, barcodeType)
        cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (0, 0, 255), 2)
        # print the barcode type and data to the terminal
        print("[INFO] Found {} barcode: {}".format(barcodeType, barcodeData))
        return barcodeData
    # show the output image
    cv2.imshow("Image", image)
    cv2.waitKey(0)


if __name__ == '__main__':
    image_path = "./images/p1.jpeg"
    barcode(image_path)
