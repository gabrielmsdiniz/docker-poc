import redis
import json
from time import sleep
from random import randint

if __name__ == '__main__':
  r = redis.Redis(host='queue', port=6379, db=0)
  while True:
    mensagem = json.loads(r.blpop('sender')[1])
    print('Waiting for new messages...')

    # Simulating email sending...
    print('Sending message:', mensagem['assunto'])
    sleep(randint(15, 45))
    print('Message', mensagem['assunto'], 'has been sent')