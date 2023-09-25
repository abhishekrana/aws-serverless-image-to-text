FROM public.ecr.aws/lambda/python:3.10

ENV LD_LIBRARY_PATH=/usr/lib64:$LD_LIBRARY_PATH

RUN yum update -y && yum install yum-utils -y

# Install tesseract
RUN yum-config-manager --add-repo https://download.opensuse.org/repositories/home:/Alexander_Pozdnyakov/CentOS_7/ -y
RUN yum update -y && yum install --nogpgcheck tesseract -y mesa-libGL -y

COPY app.py requirements.txt ./

RUN python3.10 -m pip install -r requirements.txt -t .

COPY app.py ./

CMD ["app.lambda_handler"]

