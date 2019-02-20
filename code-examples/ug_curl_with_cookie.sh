#!/bin/bash

sid="$1"
server="$2"

for i in {1..1000}; do
  api_path='/rest/object/ufgroups/1'
  api_method='PUT'
  api_payload="{\"ufGroup\":{\"name\":\"a\",\"description\":\"\",\"categories\":[{\"id\":1,\"groupId\":1}]}}"
  curl -k -v -H "sid: $sid" -H "Content-Type: application/json" -H "authorization:ZETA" -X $api_method ${server}${api_path} -d $api_payload
# -k option to skip SSL Verification.
  echo "\n =================== $i ===================="
done
