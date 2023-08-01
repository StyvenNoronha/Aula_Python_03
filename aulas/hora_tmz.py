from datetime import datetime
from pytz import timezone

dataA = datetime.now(timezone('Asia/Tokyo'))
data = datetime.now(timezone('America/Sao_Paulo'))
#print(data.strftime('%d/%m/%Y %H:%M:%S'))
#print(data.timestamp())
print(datetime.fromtimestamp(1690464244).strftime('%d/%m/%Y %H:%M:%S'))
print(data.strftime('%d/%m/%Y %H:%M:%S'))