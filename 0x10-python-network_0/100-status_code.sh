#!/bin/bash
# This script sends a request to a URL passed as an argument using curl
response=$(curl -s -o /dev/null -w "%{http_code}" "$1"); echo "$response"
