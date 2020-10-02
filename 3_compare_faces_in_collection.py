import boto3
import base64
import json
from PIL import Image

image_file = input("Enter the image filename: ")
img = Image.open(image_file)
img.show()

file = open(image_file,'rb').read()

rekognition_client = boto3.client('rekognition')

response = rekognition_client.detect_faces(
    Image={
        'Bytes': file
    }
)
#print(response['FaceDetails'][0])


if(len(response['FaceDetails'])>0):
    res = rekognition_client.search_faces_by_image(
        CollectionId='FaceDetection',
        Image={
           'Bytes': file
        }
    )
    faceMatches = res['FaceMatches']
    #print(json.dumps(faceMatches, indent=4, sort_keys=True))
    
    if not faceMatches:
        print("Given face is not in the collection")
    else:
        Similarity = str((faceMatches[0]['Similarity']))
        print("Given face matches the collection with"+' '+ Similarity + ' ' +'Similarity')

else:
    print("The image does not match with any existing faces.")
