#!/bin/bash
# a bash script that sends JSON POST request.
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
