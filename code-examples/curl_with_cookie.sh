#!/bin/bash

sid="$1"
server="$2"

for i in {258..3999}; do
  api_path='/rest/subscription'
  api_method='POST'
  ip4=$(($i % 256))
  q=$(($i / 256))
  ip3=$(($q % 256))
  q=$(($q / 256))
  ip2=$(($q % 256))
  q=$(($q / 256))
  ip1=$(($q % 256))
  api_payload="{\"subscription\":{\"name\":\"$i\",\"adProfileId\":0,\"ipProfileId\":1,\"ufProfileId\":0,\"acProfileId\":0,\"iaProfileId\":0,\"waProfileId\":0,\"malProfileId\":0,\"ipType\":\"Single\",\"ipVersion\":\"IPv4\",\"addr1\":\"$ip1.$ip2.$ip3.$ip4\",\"addr2\":\"\",\"specifiedVlanId\":false}}"
   
  curl -v -H "sid: $sid" -H "Content-Type: application/json" -H "authorization:ZETA" -X $api_method ${server}${api_path} -d $api_payload
done

