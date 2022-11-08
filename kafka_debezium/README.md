# Run Debezium Kafka Connect using Docker
![image](https://user-images.githubusercontent.com/67249292/200215708-5e469a32-4c8c-4d67-a7a9-156b953a6b33.png)

# Local Systems
* Docker Dekstop
* pgAdmin/DBeaver
* Postman

# Docker Containers
* Kafka
* Zookeeper
* Kafdrop
* postgres

## Instructions
Run file containers up with `docker-compose -f docker-compose-debezium.yaml up -d`

POST  http://localhost:8083/connectors --> To register the kafka connector with Postman


JSON :

      {
        "name": "inventory-connector",
        "config": {
          "connector.class": "io.debezium.connector.postgresql.PostgresConnector",
          "database.hostname": "postgres",
          "database.port": "5432",
          "database.user": "postgres",
          "database.password": "postgres",
          "database.dbname" : "postgres",
          "database.server.name": "dbserver1",
          "table.include.list": "inventory.customers"

        }
      }
