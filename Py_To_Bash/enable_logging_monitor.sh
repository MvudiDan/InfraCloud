#!/bin/bash

IP_ADDRESS="192.168.56.102"
USERNAME="cisco"
PASSWORD="cisco123!"

# 1. Zet logging monitor aan
sshpass -p $PASSWORD ssh -o StrictHostKeyChecking=no $USERNAME@$IP_ADDRESS << EOF
conf t
logging monitor
end
show logging
EOF
