## Utilizando la libreria matplotlib podemos guardar imagenes: por ejemplo

```py
import matplotlib.pyplot as plt
plt.savefig('pie.png')
```

# paquete adicional para entornos virtuales

```sh
sudo apt install -y python3-venv
```

# Crear un entorno virtual

- Ingresa a la carpeta donde quierees aislar el proeso de los demas 

```sh
cd app
```

- luego usa el siguiente comando

```sh
python3 -m venv env
```

donde -m venv levantamos el entorno y env es el nombre a ese entorno

# Activar 

```sh
source {nombre del entorno}/bin/activate
```
# Salir del entorno

```sh
deactivate
```

# requeriments.txt

es un archivo donde se guardan todas las dependencias de python o un entorno virtual que hemos creado

para instalar las dependencias de este archivo lo hacemos con:

```sh
pip3 install -r requeriments.txt
```


