#!/bin/bash
# Get through to secret domain
curl -sLX PUT -d 'user_id=98' -H 'Origin:HolbertonSchool' "$1"
