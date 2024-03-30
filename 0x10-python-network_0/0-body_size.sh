#!/bin/bash
# This script takes a URL as an argument, sends a request to that URL 
curl -s "$1" | wc -c
