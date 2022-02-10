# import datetime
from datetime import datetime
import time

print('\nWhile:')

# { } nao preciso de chaves para blocos
while(True):
    time.sleep(1)
    print(datetime.now().time())
    second = datetime.now().second

    if second % 2 == 0:
        print('pulei')
        # pula para o proximo laço da iteração
        # continue

    print('Pós IF')
    if second == 50:
        break
