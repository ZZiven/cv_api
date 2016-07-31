# cv_api

Overview
I implemented this simple face detection web application under the introduction from http://api.pyimagesearch.com/. It's in Python 3.5.2 and Opencv 3.0.0 in OSX.  

POST: /face_detection/detect/
Detects faces in images either via uploaded file or URL of image. The response will include a JSON dictionary consisting of:

Key	Data Type	Description
success	boolean	Indicates whether or not the request was successful or not.
num_faces	int	Number of faces detected in the image.
faces	list	Starting and ending (x, y)-coordinates for each face in the image.

URL Upload Example
$ curl -X POST 'http://api.pyimagesearch.com/face_detection/detect/' -d 'url=http://www.pyimagesearch.com/wp-content/uploads/2015/05/obama.jpg'
{"num_faces": 1, "success": true, "faces": [[410, 100, 591, 281]]}

File Upload Example
$ curl -X POST -F image=@obama.jpg 'http://api.pyimagesearch.com/face_detection/detect/'
{"num_faces": 1, "success": true, "faces": [[410, 100, 591, 281]]}
