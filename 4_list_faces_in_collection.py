import boto3
import json

rekognition_client = boto3.client('rekognition')

response = rekognition_client.list_faces(
    CollectionId='FaceDetection'
)


print('The total number of faces in FaceDetection collection are' +' '+ str(len(response['Faces'])))

