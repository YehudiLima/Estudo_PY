import logging

logging.basicConfig(level=logging.DEBUG, filename='app.log', filemode='a',
                    format='%(levelname)s - %(message)s - %(asctime)s')

try:
    email = input('Digite seu e-mail principal:',)
    senha = int(input('Digite sua senha:',))
    if senha == 1234:
        print('Login feito com sucesso!')
        logging.info(f'{email} entrou na conta bancária')
except ValueError as erro_value:
    print('Digite apenas numeros')
    logging.info(erro_value)
