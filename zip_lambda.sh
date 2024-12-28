#!/bin/bash

ZIP_NAME="lambda_function.zip"
FILES="lambda_function.py"

echo "Creating $ZIP_NAME..."
zip $ZIP_NAME $FILES
echo "$ZIP_NAME created successfully."


#Make the script executable and run it:
#chmod +x zip_lambda.sh
#./zip_lambda.sh