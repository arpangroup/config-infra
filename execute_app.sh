#!/bin/bash
set -e  # Exit immediately on error

# Variables
HOME=/home/ec2-user
APP_PATH=$HOME/myapp

# Logging commands for debugging
echo "Starting the Spring Boot app..."

# Run the Spring Boot application
nohup java -Dlogging.file.name=$HOME/api.log -jar $APP_PATH/target/*.jar &

echo "SpringBoot started"
