vagrant up --provider=aws

fab -i tuclave.pem -H ubuntu@DNS install
fab -i tuclave.pem -H ubuntu@DNS services

#Cambiar tuclave.pem por el archivo correspondiente de AWS
#Cambiar DNS por el correspondiente del a instancia creada con Vagrant
