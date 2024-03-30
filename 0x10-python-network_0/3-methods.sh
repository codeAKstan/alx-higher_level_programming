#!/bin/bash
# This script takes a URL as an argument and displays all HTTP methods the server will accept
curl -s -i -X OPTIONS "$1" | awk '/Allow:/ {print $2}'
