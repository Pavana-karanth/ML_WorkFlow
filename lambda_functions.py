#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## Lambda function 1
import json
import boto3
import base64

s3 = boto3.client('s3')

def lambda_handler(event, context):
    """A function to serialize target data from S3"""

    # Get the s3 address from the Step Function event input
    key = event['s3_key'] ## done
    bucket = event['s3_bucket'] ## done

    # Download the data from s3 to /tmp/image.png
    s3.download_file(bucket, key, "/tmp/image.png") ## done

    # We read the data from a file
    with open("/tmp/image.png", "rb") as f:
        image_data = base64.b64encode(f.read())

    # Pass the data back to the Step Function
    print("Event:", event.keys())
    return {
        'statusCode': 200,
        'body': {
            "image_data": image_data,
            "s3_bucket": bucket,
            "s3_key": key,
            "inferences": []
        }
    }


# In[ ]:


## Lambda function 2
import json
import sagemaker
import base64
from sagemaker.serializers import IdentitySerializer
from sagemaker.predictor import Predictor #wasnt imported

# Fill this in with the name of your deployed model
ENDPOINT = "image-classification-2025-10-05-05-02-27-632" ## done

def lambda_handler(event, context):

    # Decode the image data
    event = event["body"] # Flattening event because it is not directly in body. 
    image_data_b64 = event["image_data"]
    image = base64.b64decode(image_data_b64)

    # Instantiate a Predictor
    predictor = Predictor(endpoint_name=ENDPOINT) ## done

    # For this model the IdentitySerializer needs to be "image/png"
    predictor.serializer = IdentitySerializer("image/png")
    
    # Make a prediction:
    inferences = predictor.predict(image) ## done
    
    # We return the data back to the Step Function    
    event["inferences"] = inferences.decode('utf-8')
    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }


# In[ ]:


## lambda function 3
import json


THRESHOLD = .93


def lambda_handler(event, context):
    
    # Grab the inferences from the event
    inferences = json.loads(event["inferences"]) ## done
    
    # Check if any values in our inferences are above THRESHOLD
    meets_threshold = any(confidence >= THRESHOLD for confidence in inferences) ## done
    
    # If our threshold is met, pass our data back out of the
    # Step Function, else, end the Step Function with an error
    if meets_threshold:
        pass
    else:
        raise("THRESHOLD_CONFIDENCE_NOT_MET")

    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }

