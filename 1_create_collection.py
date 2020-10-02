import boto3

rekognition_client = boto3.client('rekognition')

try:
    response = rekognition_client.create_collection(
    CollectionId='FaceDetection'
    )

    print(response['CollectionArn'].split("/")[1] + ' '+ 'collection created.')

except:
    print('Collection already exists')
