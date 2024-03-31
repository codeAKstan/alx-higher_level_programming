#!/bin/bash
# This script sends a request to a URL passed as an argument using curl
curl -s -o /dev/null -w "%{http_code}" "$1"
