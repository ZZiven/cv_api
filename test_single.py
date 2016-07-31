# import the necessary packages
from __future__ import print_function
from PIL import Image
import requests
import cv2
 
# define the URL to our face detection API
url = "http://localhost:8000/face_detection/detect/"
 
# use our face detection API to find faces in images via image URL
image = cv2.imread("obama.jpg")
payload = {"url": "http://www.pyimagesearch.com/wp-content/uploads/2015/05/obama.jpg"}
r = requests.post(url, data=payload).json()
print( "obama.jpg: {}".format(r))
 
# loop over the faces and draw them on the image
for (startX, startY, endX, endY) in r["faces"]:
	cv2.rectangle(image, (startX, startY), (endX, endY), (0, 255, 0), 2)

mage_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
ret_img = Image.fromarray(image_rgb)
response = HttpResponse(mimetype="image/jpeg")
ret_img.save(response, "JPEG")
 
return response
 
# show the output image
#cv2.imshow("obama.jpg", image)
#cv2.waitKey(0)
 
