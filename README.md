# aws-serverless-image-to-text

Deploy image to text service using AWS Lambda function and SAM

## Deploy on AWS

```bash
cd image-to-text
sam build
aws cloudformation delete-stack --stack-name image-to-text
sleep 10
sam deploy
```

## Deploy locally

```bash
cd image-to-text
sam build
sam local start-api --debug
```

### Example

1. Input image `./image-to-text/data/example.png`

   ![example](./image-to-text/data/example.png)

2. Convert input image to base64 encoding

    ```bash
    python3 image-to-text/app/encode.py
    ```
    This will generate `image-to-text/data/example.json`

3. Deploy locally and test

    ```bash
    curl -X POST http://127.0.0.1:3000/image-to-text \
        -H "Content-Type: application/json" \
        --data "@image-to-text/data/example.json"
    ```

    Output
    ```bash
    {"message": "This is a lot of 12 point text to test the\nocr code and see if it works on all types\nof file format.\n\nThe quick brown dog jumped over the\nlazy fox. The quick brown dog jumped\nover the lazy fox. The quick brown dog\njumped over the lazy fox. The quick\nbrown dog jumped over the lazy fox.\n\f"}
    ```


# Resources

* https://tesseract-ocr.github.io/
