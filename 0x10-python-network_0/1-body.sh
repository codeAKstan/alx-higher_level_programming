#!/bin/bash
# This script takes a URL as an argument, displays body of the response 
curl -s -o /dev/null -w "%{http_code}\n" "$1" | grep -q 200 && curl -s "$1"
