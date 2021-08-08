# ansible-ha-rabbitmq-cluster

### prerequisites
1. To setup ansible password. Run ``` make prerequisites```
1. This project requires virtualbox and vagrant. Tested against Vagrant 2.2.6 and Virtual Box 6.1

### Instructions to setup RabbitMQ cluster via Ansible.

1. Run ```start-vms```
1. Run ```ENV=vagrant make setup-standalone-rabbits```
2. Run ```ENV=vagrant make cluster-rabbits```
3. Run ```ENV=vagrant make build-haproxy```

### Testing
1. Install the requirements in scripts/
1. Run python scripts/producer.py to publish messages to the "test" queue
1. Run python scripts/consumer.py to read messages from the "test" queue
