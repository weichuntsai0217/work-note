#!/bin/bash

sid="$1"
server="$2"

for i in {1..1000}; do
  api_path='/rest/profile/uf/1'
  api_method='PUT'
  api_payload="{\"ufProfile\":{\"defaultAction\":0,\"defaultRdpgId\":0,\"description\":\"\",\"enabled\":true,\"name\":\"u2\",\"rules\":[{\"urlGroupId\":1,\"schdId\":1,\"rdpgId\":0,\"action\":1}]}}"
  curl -k -v -H "sid: $sid" -H "Content-Type: application/json" -H "authorization:ZETA" -X $api_method ${server}${api_path} -d $api_payload
# -k to skip SSL Verification
  echo "\n =================== $i ===================="
done
