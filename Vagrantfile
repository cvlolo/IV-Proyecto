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

  config.vm.define "atp" do |host|
    host.vm.hostname = "atp"
  end
  config.vm.provider :aws do |aws, override|
    aws.access_key_id = "ASIAIMF66WWZL3E27M7Q"
    aws.secret_access_key = "roihYG7zDP1nEq3BB+bpoezwvBqW9QKg1Dkj07rL"
    aws.session_token = "FQoDYXdzEFEaDKvn5gqqTgQI82B9XCKsAQYlzczpAPDNVZ3OKsztV9gOsZahkjXcQB+uAPqsP/xJIhW1sO5H+Y0AsY4aZkFwVAU8dsHfeg0FYO2wspWswWfJVLuEd6Mx1wcKaulrRMaJcFWUJxtSrX5KX7T8pL342BY3swMXhpoT6SJ0KzhxxCqO/5nF9vvjMGBRbFNRWws6XbYwGtTsGXtz4Ib9GkPRTY86ik2VlrU40MdoZE5VpaKC93vEO7r7GY846HEo0Lzq0gU="
    aws.keypair_name = "Secure"
    aws.region= "us-west-2"
    aws.security_groups ='Secure'
    aws.instance_type= 't2.micro'

    aws.ami = "ami-1ee65166"

    override.ssh.username = "ubuntu"
    override.ssh.private_key_path = "Secure.pem"
  end

    config.vm.provision :puppet do |puppet|
    	puppet.manifests_path= 'puppet/manifests'
	puppet.manifest_file = 'recursos.pp'
	puppet.options = [
	'--verbose',
	'--debug',
    	]
  end


end
