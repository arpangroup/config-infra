#!/bin/bash
set -e  # Exit immediately on error

# Variables
LOG_FILE="/var/log/setup.log"
HOME=/home/ec2-user
APP_PATH=$HOME/myapp

# Logging commands for debugging
echo "Cloning the repository..."

# Clone the repository
git clone ${var.github_repo_url} /home/ec2-user/hello-ecs-app >> $LOG_FILE 2>&1

# Check if the repository was cloned successfully
if [ ! -d "/home/ec2-user/hello-ecs-app" ]; then
  echo "Failed to clone the repository"
  exit 1
fi
