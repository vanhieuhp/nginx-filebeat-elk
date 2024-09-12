# ELK Stack Logging Infrastructure

This project involves setting up a logging infrastructure to capture and analyze Nginx logs using Filebeat and the ELK stack, consisting of Elasticsearch, Logstash, and Kibana.

## Table of Contents
- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction
This project sets up a robust logging infrastructure to capture and analyze Nginx logs. The setup uses Filebeat to ship logs to the ELK stack, which includes Elasticsearch for storage and search, Logstash for processing, and Kibana for visualization.

## Prerequisites
- Docker and Docker Compose installed on your system.
- Basic knowledge of Nginx, Elasticsearch, Logstash, and Kibana.

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/elk-logging-infrastructure.git
    cd elk-logging-infrastructure
    ```

2. Start the ELK stack using Docker Compose:
    ```sh
    docker-compose up -d
    ```

3. Verify that the services are running:
    ```sh
    docker-compose ps
    ```

## Configuration
1. Configure Filebeat to read Nginx logs:
    - Edit the `filebeat.yml` configuration file to specify the paths to your Nginx log files.

2. Configure Logstash to process the logs:
    - Edit the `logstash.conf` file to define the input, filter, and output plugins.

3. Configure Kibana to visualize the logs:
    - Access Kibana at `http://localhost:5601` and set up your index patterns.

## Usage
- Start Nginx and generate some logs.
- Filebeat will ship the logs to Logstash.
- Logstash will process the logs and send them to Elasticsearch.
- Use Kibana to visualize and analyze the logs.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License.