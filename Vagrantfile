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

  config.vm.box = "ubuntu_aws"
  config.vm.box_url = "https://github.com/mitchellh/vagrant-aws/raw/master/dummy.box"

  config.vm.define "atp" do |host|
    host.vm.hostname = "atp"
  end
  config.vm.provider :aws do |aws, override|
    aws.access_key_id = ENV['ACCES_KEY']
    aws.secret_access_key = ENV['SECRET_ACCES_KEY']
    aws.session_token = ENV['TOKEN']
    aws.keypair_name = "Secure"
    aws.region= "us-west-2"
    aws.security_groups ='Secure'
    aws.instance_type= 't2.micro'

    aws.ami = "ami-1ee65166"

    override.ssh.username = "ubuntu"
    override.ssh.private_key_path = "Secure.pem"

    
  end

    config.vm.provision :puppet do |puppet|

    	puppet.manifests_path= 'puppet/manifests/'
	puppet.manifest_file = 'recursos.pp'
	puppet.options = [
	'--verbose',
	'--debug',
    	]
  end


end
