

import json
import logging
import boto3
import uuid
import botocore
import os

def lambda_handler(event, context):
    
    import cv2
    import numpy as np

    AWS_ACCESS_KEY_ID = 'Your AWS_ACCESS_KEY_ID'
    AWS_SECRET_KEY = 'Your AWS_SECRET_KEY'
    AWS_S3_BUCKET_NAME = 'Your AWS_S3_BUCKET_NAME for Saving Result'

    for record in event['Records']:
        bucket = record['s3']['bucket']['name'] # bucket name
        key = record['s3']['object']['key'] # file name
        # download_path = '/tmp/{}{}'.format(uuid.uuid4(), key)


    s3_client = boto3.client(
        "s3",
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_KEY,
        region_name="ap-northeast-2"
    )

    url = s3_client.generate_presigned_url(
        ClientMethod='get_object',
        Params={
            'Bucket': bucket,
            'Key': key,

        },
        ExpiresIn=2 * 24 * 60 * 60  
    )

    

    vcap = cv2.VideoCapture(url)

    fps = 30
    frame_index = 0
    # frames = []
    result_file_path = []
    while(True):
        # Capture frame-by-frame
        ret, frame = vcap.read()
        #print cap.isOpened(), ret
        if frame is not None:
            frame = cv2.resize(frame, (416, 416))
            # frames.append(frame)
            frame_index += fps
            vcap.set(cv2.CAP_PROP_POS_FRAMES, frame_index)

            result_path = "/tmp/" + key.split(".")[0]+str(frame_index)+".jpg"
            result_file_path.append(result_path)

            cv2.imwrite(result_path, frame)
            
            if cv2.waitKey(22) & 0xFF == ord('q'):
                break
                # print(frame_index, len(frames))
        else:
            print("Frame is None")
            break
        
    vcap.release()

    for upload_path in result_file_path:
        s3_client.upload_file(upload_path, AWS_S3_BUCKET_NAME, upload_path.split('/')[-1])




    
    return {
        "statusCode": 200,
        # "body": json.dumps({
        #     "message": "image saved to s3://"
        # }),
    }