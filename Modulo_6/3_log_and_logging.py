import logging
# Niveis de logging
""" 
debug - Só estou informando informaçoes para os desenvolvedores.

info - Só quero informar algo que está acontecendo no programa, mas que nao é um erro.

warning - Quero alerta sobre algo quue está acontecendo, possívelmente fora do esperado, porém ainda não é m erro,
mas pode gerar um futuramente.

error - Um erro que aconteceu na aplicação.

critical - Um erro com consequências graves acaba de ocorrer na aplicação.

 """
logging.basicConfig(level=logging.DEBUG, filename='app.log', filemode='a',
                    format='%(levelname)s - %(message)s')  # Setar o nível
logging.debug('Logging nível debug')
logging.basicConfig(level=logging.INFO)
logging.info('Logging nível info')
logging.warning('Logging nível warning')
logging.error('Logging nível error')
logging.critical('Logging nível crítico')
