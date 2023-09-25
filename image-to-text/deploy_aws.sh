#!/bin/bash

set -ex

sam build
aws cloudformation delete-stack --stack-name image-to-text
sleep 10
sam deploy
