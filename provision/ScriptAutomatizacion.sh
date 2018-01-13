vagrant up --provider=aws

fab -i tuclave.pem -f rutaFabFile -H ubuntu@DNS install
fab -i tuclave.pem -f rutaFabFile -H ubuntu@DNS web

#Cambiar tuclave.pem por el archivo correspondiente de AWS
#Cambiar DNS por el correspondiente de la instancia creada con Vagrant
