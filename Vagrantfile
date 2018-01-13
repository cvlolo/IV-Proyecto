# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://atlas.hashicorp.com/search.

  config.vm.box = "dummy"

  config.vm.define "atpbot" do |host|
    host.vm.hostname = "atpbot"
  end
  config.vm.provider :aws do |aws, override|
    aws.access_key_id = "ASIAJSLTBSM36LRL3ZYA"
    aws.secret_access_key = "C+1drDX0X6s2M8+uOVEdRpEK4TTomO10e1SGC5lg"
    aws.session_token = "FQoDYXdzEEcaDAmVeoHjn2KIuqzbDiKsAYsd51QJZvzo65/GVV8S3kVHNnsN5ih/RTZH91mN+OsDi2Z3vcNX2qgkR2msMNT9YzjowLsPOSPgnal7vEwqr7tDk3wTkwEtpG4czdxzQgSXDuKhNjvoFDNbKR/G6+fM/bbdZTu4zUwIQ48ioFGmgv4t6Qz22AXT7fYfysGipqaPOqlrKEU79bDDi7QqN2OxSzNErNTevaKLq5z7PCzdBNEnYH9BQWJKmcGPy1oog5Lo0gU="
    aws.keypair_name = "Newkey"
    aws.region= "us-west-2"
    aws.security_groups ='atpbot-Nuevo'
    aws.instance_type= 't2.micro'

    aws.ami = "ami-1ee65166"

    override.ssh.username = "ubuntu"
    override.ssh.private_key_path = "Newkey.pem"
  end

    config.vm.provision :ansible do |ansible|
    	ansible.playbook = "ansibleConf.yml"
   	ansible.verbose = "vvv"
    	ansible.force_remote_user= true
    	ansible.host_key_checking=false
  end


end
