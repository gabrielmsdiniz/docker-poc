import psycopg2
from bottle import route, run, request

DSN = 'dbname=email_sender user=postgres host=db'
SQL = 'INSERT INTO emails (assunto, mensagem) VALUES (%s, %s)'

def register_message(assunto, mensagem):
  conn = psycopg2.connect(DSN)
  cur = conn.cursor()

  cur.execute(SQL, (assunto, mensagem))
  conn.commit()

  cur.close()
  conn.close()

  print('Message has been registered!')

@route('/', method='POST')
def send():
  subject = request.forms.get('assunto')
  message = request.forms.get('mensagem')

  register_message(subject, message)
  return 'Message queued! Subject: {} Message: {}'.format(subject, message)

if __name__ == '__main__':
  run(host='0.0.0.0', port=8080, debug=True)