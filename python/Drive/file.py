from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Carga las credenciales desde el archivo JSON que descargaste desde la página de credenciales de Google
creds = Credentials.from_authorized_user_file('./token.json')

# Crea un objeto de servicio de la API de Google Drive
service = build('drive', 'v3', credentials=creds)

# Busca la carpeta que deseas montar
folder_name = 'stable_diffusion_weights'
query = "mimeType='application/vnd.google-apps.folder' and trashed = false and name='" + folder_name + "'"
response = service.files().list(q=query, fields='files(id)').execute()

# Obtiene el ID de la carpeta
folder_id = response['files'][0]['id']

# Monta la carpeta en tu sistema de archivos local
import os
mount_path = '/tmp/tmp.FK7V3oAzvu'
if not os.path.exists(mount_path):
    os.makedirs(mount_path)
os.system('google-drive-ocamlfuse -headless -label ' + folder_name + ' ' + mount_path + ' -o uid=1000,gid=1000,allow_other')
