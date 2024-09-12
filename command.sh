#!/bin/bash
docker cp logstash:/usr/share/logstash/config ./logstash/config

docker cp logstash:/usr/share/logstash/pipeline ./logstash/pipeline
docker cp filebeat:/usr/share/filebeat/filebeat.reference.yml ./filebeat/config/filebeat.reference.yml

# delete index
curl -X DELETE "http://localhost:9200/filebeat-test-2024.09.10"
