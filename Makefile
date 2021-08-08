prerequisites:
	echo "password" >> password_file

start-vms:
	vagrant up

setup-standalone-rabbits:
	ansible-playbook -i inventory/$(ENV) playbooks/build-standalone-rabbits.yml -vv --diff

cluster-rabbits:
	ansible-playbook -i inventory/$(ENV) playbooks/cluster-rabbits.yml -vv --diff

build-haproxy:
	ansible-playbook -i inventory/$(ENV) playbooks/build-haproxy.yml -vv --diff

edit-vault:
	ansible-vault edit inventory/group_vars/$(ENV)/vault.yml

view-vault:
	ansible-vault view inventory/group_vars/$(ENV)/vault.yml
