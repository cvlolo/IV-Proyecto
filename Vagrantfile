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
    aws.access_key_id = "ASIAJEG3TN3UB76IO6KA"
    aws.secret_access_key = "5jV9Gof0vnCeEKw3RU5xXpVcT8x13mzF4xXydNPi"
    aws.session_token = "FQoDYXdzEIv//////////wEaDBf+wyRSz2I77ETZiyKsAW5cftziO2FUpofFVEJRx77a11tkQv4Zmg06LCfjkx8D2Vl++e73V2daG8BA9BnO2ULN/rXkAHvUTYZ/dNtlgi1UvDFknpB1Ub7/4KAY/+S4bmtMmI1GjkaxDRUZqyJaEUNuMWpj3UI6JUT5zfViPTAMsG8PPLaE5nx//g6DHVWlDtsYtvB7+B8AYntj1jRI/e+HT4X4KoRNT7habv4TpuwklgyBP5s3A17ZkmwoooLZ0QU="
    aws.keypair_name = "keey"
    aws.region= "us-west-2"
    aws.security_groups ='atpbot'
    aws.instance_type= 't2.micro'

    aws.ami = "ami-0def3275"

    override.ssh.username = "ubuntu"
    override.ssh.private_key_path = "keey.pem"
  end

    config.vm.provision :ansible do |ansible|
    	ansible.playbook = "ansibleConf.yml"
   	ansible.verbose = "vvv"
    	ansible.force_remote_user= true
    	ansible.host_key_checking=false
  end


end
