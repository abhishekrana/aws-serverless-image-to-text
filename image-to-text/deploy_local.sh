#!/bin/bash

set -ex

sam build
sam local start-api --debug

