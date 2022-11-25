import os
import ProxyCloud

BOT_TOKEN = '5194747336:AAHM7f-BIte_ZGhbsV8sNO6hJMHqmicVYcU' #Aqui va el token del bot
API_ID =  12609125 #Tu api id de telegram
API_HASH = '384e99809859bce23cc61dd0a3f4dd23' #Tu api id de telegram
SPLIT_FILE = 1024 * 1024 * int(os.environ.get('split_file','99'))
ROOT_PATH = 'root/'
ACCES_USERS = os.environ.get('tl_admin_user','Gerpv76').split(';')

static_proxy = '' #agrega si kieres tener un proxy statico Con @raydel0307 si kieres comprar un proxy
PROXY = ProxyCloud.parse(static_proxy)

if PROXY:
  print(f'Proxy {PROXY.as_dict_proxy()}')
  
#Lo siguiente son las tablas de la base de datos de usarios, 
#es obligatorio agregar a aquellos usarios estaticos puestos en el main.py
#los agregados mediante /add no es necesario
#ponerlos valor 0 siempre

space = {}
space['raydel0307'] = 0
