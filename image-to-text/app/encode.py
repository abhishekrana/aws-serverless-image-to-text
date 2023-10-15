import base64
import json

input_file: str = "image-to-text/data/example.png"
output_file: str = "image-to-text/data/example.json"

with open(input_file, "rb") as fp:
    encoded_string: str = base64.b64encode(fp.read()).decode("utf-8")

with open(output_file, "w") as fp:
    fp.write(json.dumps({"content": encoded_string}))
