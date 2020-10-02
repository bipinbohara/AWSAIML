import boto3

rekognition_client = boto3.client('rekognition')

try:
    response = rekognition_client.delete_collection(
    CollectionId='FaceDetection'
    )

    
    status_code = response['StatusCode'] 

    if status_code == 200:
        print("Collection deleted successfully")

except:
    print('Collection not found')    
