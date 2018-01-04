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
    aws.access_key_id = "ASIAIQF5KQLWHXOQUCYQ"
    aws.secret_access_key = "VwArVv176mT0WVg8OETCwtzYGbhdB1v0gXlfnXOZ"
    aws.session_token = "FQoDYXdzEF0aDEHJs94Djz8MStQmrCKsAQq4cPoEbMGyt6KK8rtgueMl5rtMTMcgrtfjjr5b3UNzMkufbo6iXEe8E6T5mhQNMJLGkFTKsj7TGkv/49ZHFV8SbJGvOXQpqtm0UmLYNysIBKGudDukf7JtS6NvjwxNcmmzGh4ppSa3LkY5dTllaVoNeVIBQNKfjbn2m0MtjwMg3CMtxzRK817dFqxxenCyKIwr4dnk4LITdCt1XGQTuZNqSNxwJotPJLrSSVoo66W40gU="
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
