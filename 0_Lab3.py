import boto3
import base64
import json
import os
import sys
from PIL import Image

original_stdout = sys.stdout #Save a reference to the original standard output

rekognition_client = boto3.client('rekognition')

image_file = input("Enter the image filename: ")
print("Check output.txt file")

img = Image.open(image_file)
img.show() # Displays Image in a new window

file = open(image_file,'rb').read()

# To save the text output in a file
with open("output.txt","w+") as file1:
    sys.stdout = file1 # Change the standard output to the file we created

    response = rekognition_client.detect_faces(
        Image={
            'Bytes': file
        },
        Attributes=['ALL']
    )
    #print(response)
    for face in response['FaceDetails']:
        str1 = 'The detected face is between ' + str(face['AgeRange']['Low']) + ' and ' + str(face['AgeRange']['High']) + ' years old \n'
        
        str2 = 'The detected face is of ' + str(face['Gender']['Value'] + '\n')
        
        Smile = str(face['Smile']['Value'])
        Eyeglass = str(face['Eyeglasses']['Value'])
        Sunglass = str(face['Sunglasses']['Value'])
        Beard = str(face['Beard']['Value'])
        Mustache = str(face['Mustache']['Value'])

        if Smile == 'True':
            str3 = 'The detected face is smiling \n'
        else:
            str3 = 'The detected face is not smiling \n'
        
        if Eyeglass == 'True':
            str4 = 'The detected face has Eyeglass on \n'
        else:
            str4 = 'The detected face does not have Eyeglass on \n'
        
        if Sunglass == 'True':
            str5 = 'The detected face is wearing Sunglasses \n'
        else:
            str5 = 'The detected face is not wearing Sunglasses \n'

        if Beard == 'True':
            str6 = 'The detected face has Beard \n'
        else:
            str6 = 'The detected face does not have Beard \n'
            
        if Mustache == 'True':
            str7 = 'The detected face has Mustache \n'
        else:
            str7 = 'The detected face does not have Mustache \n'

        str8 = 'The detected face has following Emotions: ' + '\n' + '\t' + str(face['Emotions'][0]['Type']) + ' with confidence ' + str(face['Emotions'][0]['Confidence']) + '\n'+ '\t' +str(face['Emotions'][1]['Type']) + ' with confidence ' + str(face['Emotions'][1]['Confidence']) + '\n' + '\t' +str(face['Emotions'][2]['Type']) + ' with confidence ' + str(face['Emotions'][2]['Confidence']) + '\n' + '\t' +str(face['Emotions'][3]['Type']) + ' with confidence ' + str(face['Emotions'][3]['Confidence']) + '\n' + '\t' +str(face['Emotions'][4]['Type']) + ' with confidence ' + str(face['Emotions'][4]['Confidence']) + '\n' + '\t' +str(face['Emotions'][5]['Type']) + ' with confidence ' + str(face['Emotions'][5]['Confidence']) + '\n' + '\t' +str(face['Emotions'][6]['Type']) + ' with confidence ' + str(face['Emotions'][6]['Confidence']) + '\n' + '\t' +str(face['Emotions'][7]['Type']) + ' with confidence ' + str(face['Emotions'][7]['Confidence'])

    str_final = str1 + str2 + str3 + str4 + str5 + str6 + str7 + str8
    print(str_final)
    sys.stdout = original_stdout # Reset the standard output to its original value


