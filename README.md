# neo4j-stream-to-kafka

In this project we will explore Neo4j event stream to Kafka using [neo4j-streams](https://neo4j.com/labs/kafka/4.0/)

----
## Setup

Copy the [neo4j streams plugin](https://github.com/neo4j-contrib/neo4j-streams/releases/download/4.0.6/neo4j-streams-4.0.6.jar) to the `neo4j/plugins` directory
```bash
cp neo4j-streams-4.0.6.jar neo4j/plugins/
```

Start the docker containers for neo4j, kafka and zookeeper using the [docker-compose.yml](./docker-compose.yml) file
```bash
docker-compose up -d
```


-----
## Creating nodes

Now you can open up Neo4j in a browser `http://localhost:7474/browser/` using the credential neo4j/streams
and execute the following cypher command

```cypher
UNWIND range(501,550) as id
CREATE (p:Person {id:id, name: "Name " + id, age: id % 3}) WITH collect(p) as people
UNWIND people as p1
UNWIND range(1,10) as friend
WITH p1, people[(p1.id + friend) % size(people)] as p2
CREATE (p1)-[:KNOWS {years: abs(p2.id - p1.id)}]->(p2)
```

------------------
## Event streams

To see the events steam, you can use the following command
```bash

$ docker exec kafka kafka-console-consumer --bootstrap-server localhost:9092 --topic neo4j --from-beginning

```

### Event streams using python

To view the events using python, you can use the code `consumer.py`
```bash
$ pip install kafka-python

$ python3 consumer.py 

```


-----------------
## References

https://neo4j.com/labs/kafka/4.0/quickstart/
https://github.com/neo4j-contrib/neo4j-streams/releases/tag/4.0.6
https://www.confluent.io/blog/transactions-apache-kafka/

https://timber.io/blog/hello-world-in-kafka-using-python/