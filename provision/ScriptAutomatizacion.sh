ACCES_KEY="tuclave" SECRET_ACCES_KEY="tuclavesecreta" TOKEN="tu_token-access" vagrant up --provider=aws




#El despliegue quedará realizado por completo con los siguientes comandos:

fab -i tuclave.pem -f rutaFabFile -H ubuntu@DNS Install
fab -i tuclave.pem -f rutaFabFile -H ubuntu@DNS RunDosRun


#Pueden desplegarse los dos servicios, web y bot de forma individual con:

#fab -i tuclave.pem -f rutaFabFile -H ubuntu@DNS DjangoUp
#fab -i tuclave.pem -f rutaFabFile -H ubuntu@DNS botUp

#Para acabar con el proceso de gunicorn utilizar:

#fab -i tuclave.pem -f rutaFabFile -H ubuntu@DNS killGunicorn

#Para eliminar el despliegue:

#fab -i tuclave.pem -f rutaFabFile -H ubuntu@DNS Uninstall

#Para saber si django posee algun fallo:

#fab -i tuclave.pem -f rutaFabFile -H ubuntu@DNS TestDjango

#tuclave.pem hace referencia a la clave creada desde AWS para acceder por SSH a la instancia
#Utiliza el DNS de la misma instancia
# rutaFabFile sera del tipo /ruta/hacia/fabfile.py
