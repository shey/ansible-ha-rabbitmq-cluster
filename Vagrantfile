# -*- mode: ruby -*-
# vi: set ft=ruby :
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = 'ubuntu/focal64'

  config.ssh.insert_key = false
  config.ssh.forward_agent = true

  ssh_pub_key = File.readlines("#{Dir.home}/.ssh/id_rsa.pub").first.strip

  config.vm.provision "shell", inline: <<-SHELL
    echo #{ssh_pub_key} >> /home/vagrant/.ssh/authorized_keys
    echo #{ssh_pub_key} >> /root/.ssh/authorized_keys
    sudo apt -qq install python-is-python3
  SHELL

  # General VirtualBox VM configuration.
  config.vm.provider :virtualbox do |v|
    v.customize ["modifyvm", :id, "--cpus", 4]
    v.customize ["modifyvm", :id, "--memory", 4096]
    v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
    v.customize ["modifyvm", :id, "--natdnsproxy1", "on"]
    v.customize ["modifyvm", :id, "--ioapic", "on"]
  end

  config.vm.synced_folder ".", "/vagrant", disabled: true

  config.vm.define "rabbitproxy" do |rabbitproxy|
    rabbitproxy.vm.hostname = "rabbitproxy"
    rabbitproxy.vm.network :private_network, ip: "192.168.114.101"
  end

  config.vm.define "rabbit1" do |rabbit1|
    rabbit1.vm.hostname = "rabbit1"
    rabbit1.vm.network :private_network, ip: "192.168.114.102"
  end

  config.vm.define "rabbit2" do |rabbit2|
    rabbit2.vm.hostname = "rabbit2"
    rabbit2.vm.network :private_network, ip: "192.168.114.103"
  end

end
