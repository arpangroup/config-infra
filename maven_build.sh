#!/bin/bash
set -e  # Exit immediately on error

# Variables
HOME=/home/ec2-user
APP_PATH=$HOME/myapp

# Logging commands for debugging
echo "Making mvnw executable..."

# Change to the project directory
cd $APP_PATH

# Make mvnw script executable
chmod +x ./mvnw

# Running Maven package
echo "Running Maven package..."
./mvnw package
