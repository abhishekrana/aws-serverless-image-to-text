import base64
import numpy as np
import json
import io
import cv2
import pytesseract
from PIL import Image

def lambda_handler(event, context):
    image_bytes = event['body'].encode('utf-8')
    image_dict = json.loads(image_bytes.decode('utf-8'))
    image = Image.open(io.BytesIO(base64.b64decode(image_dict["content"])))
    nimg = np.array(image)
    img_cv = cv2.cvtColor(nimg, cv2.COLOR_BGR2RGB)
    img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)

    result = pytesseract.image_to_string(img_rgb)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": result,
        }),
    }

