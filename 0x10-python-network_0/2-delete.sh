#!/bin/bash
# This script sends a DELETE request to the URL passed as the first argument using curl
curl -s -X DELETE "$1"
