
import requests
import math
import json
from investidor10 import body, headers

def calcular_diferenca_percentual(numero1, numero2):
    diferenca = numero1 - numero2
    percentual = (diferenca / numero2) * 100
    return percentual

with requests.post(url="https://investidor10.com.br/api/advanced-search/", data=body, headers=headers) as response:
    print(response)
    print(response.status_code)
    # print(response.json())
    data = response.json()['data']
    print("total:", response.json()['total'])

for item in data:
    item['graham'] = math.sqrt(22.5 * item['lpa'] * item['vpa'])
    diferenca = calcular_diferenca_percentual(item['graham'], item['price'])
    item['upside_graham'] = diferenca

data.sort(reverse=True, key=lambda x : x["upside_graham"])

# for item in data:
#     print(f"{item['name']}: Preço R${item['price']} | Preço Justo de Graham: R${item['graham']:.2f} | UPSIDE (GRAHAM): {item['upside_graham']:.2f}%")
#     print(f"DY: {item['dy']} | LPA {item['lpa']} | VPA {item['vpa']} | P/VP {item['p_vp']} | P/L {item['p_l']}\n")

with open('./acoes.json', 'w', encoding="utf-8") as arquivo_json:
    json.dump(data, arquivo_json, indent=4, ensure_ascii=False)
# print(body)
