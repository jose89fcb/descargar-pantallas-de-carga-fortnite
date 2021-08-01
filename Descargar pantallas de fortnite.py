import requests
import json
import os
import ctypes
from os import remove
import shutil



url = requests.get('https://fortnite-api.com/v2/aes')
AES = json.loads(url.text)




#Video tutorial: https://www.youtube.com/watch?v=0XjEPGLjsCQ
 
#Necesitas instalar python 3.7: https://www.python.org/downloads/release/python-370/
 
 
 #Para poder descargar las pantallas de carga de fortnite necesitaras descargar el programa umodel:
 # -> https://www.gildor.org/en/projects/umodel#files
 #Deberas de añadir el programa umodel.exe en la siguiente ruta:
 # C:\Program Files\Epic Games\Fortnite\FortniteGame\Content\Paks
 
################################################################################
# para hacer todo este proceso necesitaras tener fortnite instalado en tu pc   #
################################################################################
 
# Twitter: https://twitter.com/jose89fcb
# Creador Jose89fcb







 
aesFortnite = url.json()['data']['mainKey']

 

 
ArchivoBat = open('C:\\Program Files\\Epic Games\\Fortnite\FortniteGame\\Content\Paks\\1PantallasDeCargaFN.bat','w')
 
 

 
 
 
 
 
 


ArchivoBat.write('umodel.exe -path="C:\Program Files\Epic Games\Fortnite\FortniteGame\Content\Paks"')

ArchivoBat.write(" -aes=0x" + aesFortnite)




        


for i in AES['data']['dynamicKeys']:
 

 


 ArchivoBat.write(" -aes=0x{}".format(i['key']))
 
 
 



ArchivoBat.write(' -out=\\PantallasDeCargaFn -export */Game/2dAssets/Loadingscreens/* -png')



ArchivoBat.close()

os.system('1PantallasDeCargaFN.bat')




dirPath1 = 'PantallasDeCargaFn/Engine'
dirPath2 ='PantallasDeCargaFn/Game/Athena'
dirPath3 ='PantallasDeCargaFn/Game/Spectating'


try:
    shutil.rmtree(dirPath1)
    shutil.rmtree(dirPath2)
    shutil.rmtree(dirPath3)
except OSError as e:
    print(f"Error:{ e.strerror}")


        
ArchivoBat = open('C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\renombrar.py','w')



ArchivoBat.write('import os')
ArchivoBat.write('\n\n')
ArchivoBat.write('for file in os.listdir("C:/Program Files/Epic Games/Fortnite/FortniteGame/Content/Paks/PantallasDeCargaFn/Game/2dAssets"):')
ArchivoBat.write('\n\n')
ArchivoBat.write('	os.rename(file, "C:/Program Files/Epic Games/Fortnite/FortniteGame/Content/Paks/PantallasDeCargaFn/Game/2dAssets/Pantallas de carga fortnite")')


ArchivoBat.close()
Bat = open('C:\\Program Files\\Epic Games\\Fortnite\FortniteGame\\Content\Paks\\1renombrar.bat','w')

Bat.write('start /d "C:/Program Files/Epic Games/Fortnite/FortniteGame/Content/Paks/PantallasDeCargaFn/Game/2dAssets" renombrar.py')

Bat.close()
os.system('1renombrar.bat') 
os.remove("1renombrar.bat")



MessageBox = ctypes.windll.user32.MessageBoxW
MessageBox(0, 'Finalizado!', 'Pantallas de carga', 0)
remove('1PantallasDeCargaFN.bat')

borrar = open('C:\\Program Files\\Epic Games\\Fortnite\FortniteGame\\Content\Paks\\1borrar.bat','w')

borrar.write('cd "C:/Program Files/Epic Games/Fortnite/FortniteGame/Content/Paks/PantallasDeCargaFn/Game/2dAssets"')
borrar.write('\n')
borrar.write('del /F /S /Q *.py')
borrar.close()
os.system('1borrar.bat') 
os.remove("1borrar.bat")



