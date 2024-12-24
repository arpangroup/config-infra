#!/bin/bash
set -e  # Exit immediately on error

# Install logrotate
sudo yum install -y logrotate

# Create logrotate configuration
#cat <<EOC > /etc/logrotate.d/custom_logs
#/var/log/my_custom_log {
#    daily
#    rotate 7
#    compress
#    missingok
#    notifempty
#    copytruncate
#}
#EOC

# Create logrotate configuration
cat <<EOC > /etc/logrotate.d/custom_logs
/var/log/my_custom_log {
    daily
    rotate 7
    compress
    missingok
    notifempty
    create
    delaycompress
    postrotate
        /usr/bin/systemctl reload rsyslog.service > /dev/null 2>&1 || true
    endscript
}
EOC

# Restart logrotate service
sudo systemctl restart crond