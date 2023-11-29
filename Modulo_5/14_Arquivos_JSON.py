import json
from pathlib import Path

carros = [
    {'Marca': 'Nissan', "Preco": 45.000, 'Cor': 'Azul'},
    {'Marca': 'Chevrolet', "Preco": 50.000, 'Cor': 'Prata'},
    {'Marca': 'BMW', "Preco": 100.000, 'Cor': 'Vermelho'}
]

carros_json = json.dumps(carros)
Path('carros.json').write_text(carros_json)

# Para acessar json

arquivo_carros_json = Path("carros_json").read_text()
arquivo_json = json.loads(arquivo_carros_json)
print(arquivo_json[0]['Marca'])
