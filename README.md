# AWSAIML LAB3

1. There are 6 python files among which files starting from 1-5 are used to create collection, add images to the collection, comapare faces within the images, list the number of faces added to the collection and delete the collection respectively.
    * To compare the faces use 'test.jpg' (different image of the same person)
    
2. File 0_Lab3.py is used analyze the face within the image, the output is saved in the output.txt and the image that the user inputs is displayed in a new window.

3. An image file 'minion.jpg' is not recognized as a face and hence not included in the collection too because Amazon Rekognition does not categorize it as a face.

![Screenshot1](img/Screenshot1.png)

![Screenshot3](img/Screenshot3.png)

4. The faces were falsely classified as not smiling and even with/without beard or mustache in some cases, the problem might be with photo quality or some bias with the face detection algorithm.
