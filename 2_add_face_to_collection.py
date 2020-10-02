import boto3
import base64
import json

rekognition_client = boto3.client('rekognition')

image_name = ['alan.jpg','bipin.jpg','downey.jpg','jhonny.jpg','minion.jpg','putin.jpg']

for img in image_name:
    file = open( img ,'rb').read()

    response = rekognition_client.index_faces(
        CollectionId='FaceDetection',
        Image={
        'Bytes': file,
        },
        ExternalImageId='FaceDetection'
    )

#print(json.dumps(response, indent=4, sort_keys=True))

    print(img + ' ' +'added to Collection FaceDetection')
















