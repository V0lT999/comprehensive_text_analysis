# comprehensive_text_analysis

## Че по установке:

- zookeper: 
  - из директории kafka_2.13-3.3.1 
  - команда bin/zookeeper-server-start.sh config/zookeeper.properties
- kafka-server: 
  - из директории kafka_2.13-3.3.1
  - команда JMX_PORT=8004 bin/kafka-server-start.sh config/server.properties
- cmak:
  - из директории CMAK/target/universal/cmak-3.0.0.7
  - команда bin/cmak -Dconfig.file=conf/application.conf -Dhttp.port=8080
