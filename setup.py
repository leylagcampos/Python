#36 paquetes distribuibles
#>python setup.py sdist  desde el cmd para que se pueda crear el dist
#para instalar el paquete y 35.py pueda ejecutarse desde cualquier lugarr
#>pip3 install pa..(aqui presionar tabulador para autocompletar) se refiere al rar que se creó
#desintalar el paquete:
#>pip3 uninstall PaqueteCalculos



from setuptools import setup

setup(
	name="PaqueteCalculos",
	version="1.0",
	description="paquete de operaciones",
	author="Leyla",
	author_email="leyla.campos1@unmsm.edu.pe",
	url="www.hotmail.com",
	packages=["paquete","paquete.subpaquete"]


	)