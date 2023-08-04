import csv
import json
import time


class SomaInvestimentos:
    def __init__(self, nome_arquivo, percentual_desejado):
        self.nome_arquivo = nome_arquivo
        self.percentual_desejado = percentual_desejado
        self.titulos = []
        self.resumo = {}

    def le_csv(self):
        with open(self.nome_arquivo, 'r', newline='', encoding='utf-8') as arquivo:
            leitor_csv = csv.reader(arquivo, delimiter=';')
            for i, linha in enumerate(leitor_csv):
                if i > 1:  # Ignora as duas primeiras linhas (cabeçalho)
                    if len(linha) > 6:  # Verifica se a linha tem índice 6 (coluna G)
                        valor = linha[6]  # Valor da coluna G
                        valor = valor.replace("R$", "").strip()  # Remove o prefixo "R$" e espaços em branco
                        valor = valor.replace(".", "").replace(",", ".")  # Remove milhares e substitui vírgula por ponto decimal
                        valor = float(valor)  # Converte para formato numérico

                        tipo_investimento = linha[0]  # Valor da coluna A (grupo)
                        descricao = linha[1]  # Valor da coluna B

                        self.titulos.append({
                            'tipo': tipo_investimento,
                            'descricao': descricao,
                            'valor': valor
                        })

                        grupo = self.resumo.get(tipo_investimento, 0.0)
                        grupo += valor
                        self.resumo[tipo_investimento] = grupo

    def calcular_percentual(self, valor, total):
        return (valor / total) * 100
    
    def calcular_porcentagens(self):
        total_soma = sum(self.resumo.values())

        for grupo, soma in self.resumo.items():
            porcentagem_ideal = self.percentual_desejado.get(grupo, 0)

            self.resumo[grupo] = {
                'valor_investido': soma,
                'valor_ajustado': soma,
                'porcentagem_investido': self.calcular_percentual(soma, total_soma),
                'porcentagem_ajustada': self.calcular_percentual(soma, total_soma),
                'porcentagem_ideal': porcentagem_ideal,
                'quantia_adicional': 0
            }
    
    def get_total_investido(self):
        return sum(grupo["valor_ajustado"] for grupo in self.resumo.values())

    def calcular_quantia_adicional(self, valor_atual, total_inicial, percentual_desejado):
        valor_adicional = 0

        while percentual_desejado - self.calcular_percentual(valor_atual + valor_adicional, total_inicial + valor_adicional) > 0:
            valor_adicional += 0.01

        return valor_adicional


    def calcular_percentual_atual(self):
        total = self.get_total_investido()

        for grupo in self.resumo.values():
            grupo["porcentagem_ajustada"] = self.calcular_percentual(grupo["valor_ajustado"], total)


    def calcula_valores_ideias(self, iteracao = 0):
        self.calcular_percentual_atual()
        self.mostrar_percentuais()

        for grupo in self.resumo.values():
            if grupo["porcentagem_ideal"] - grupo["porcentagem_ajustada"] > 0.001:
                total = self.get_total_investido()
                quantia_adicional = self.calcular_quantia_adicional(grupo["valor_ajustado"], total, grupo["porcentagem_ideal"])

                grupo["valor_ajustado"] += quantia_adicional
                self.calcular_percentual_atual()

                grupo["quantia_adicional"] += quantia_adicional

                if iteracao > 2:
                    return
                                
                self.calcula_valores_ideias(1 + iteracao)

        self.calcular_percentual_atual()
    
    def mostrar_percentuais(self):
        print("")

        for tipo, grupo in self.resumo.items():
            valor = grupo['valor_ajustado']
            quantia_adicional = grupo.get('quantia_adicional', 0)
            percentual = grupo['porcentagem_ajustada']
            percentual_ideal = grupo['porcentagem_ideal']
            print(f"{tipo}: valor: {valor:.2f} | valor adicional: {quantia_adicional:.2f} | {percentual:.2f}% | ideal: {percentual_ideal:.2f}%")

        print("-" * 60)

    def calcular_soma_investimentos(self, valor_em_conta):
        self.le_csv()
        self.calcular_porcentagens()
        self.calcula_valores_ideias()

        total_investido = sum(valores['valor_investido'] for valores in self.resumo.values())
        aporte_necessario_para_igular = sum(valores.get('quantia_adicional', 0) for valores in self.resumo.values())

        resultado = {
            'titulos': self.titulos,
            'resumo': self.resumo,
            'valor_em_conta': valor_em_conta,
            'total_investido': total_investido,
            'patrimonio': valor_em_conta + total_investido,
            'aporte_necessario_para_igular': aporte_necessario_para_igular
        }

        return resultado
    

def main():
    nome_do_arquivo = 'Exportar_custodia_2023-07-15.csv'  # Substitua pelo nome do seu arquivo CSV

    percentual_desejado = {
        'CDB': 50,
        'FII': 25,
        'Ação': 16,
        'ETF': 4,
        'BDR': 4,
        'Renda Variável - Outros': 1
    }

    valor_input = float(input("Digite o valor em conta: "))

    soma_investimentos = SomaInvestimentos(nome_do_arquivo, percentual_desejado)
    resultado = soma_investimentos.calcular_soma_investimentos(valor_input)

    # Guardar o resultado em um arquivo JSON
    with open('resultado.json', 'w', encoding="utf-8") as arquivo_json:
        json.dump(resultado, arquivo_json, indent=4, ensure_ascii=False)

    print("Resumo dos valores:")
    for grupo, valores in resultado['resumo'].items():
        valor_investido = valores['valor_investido']
        porcentagem_investida = valores['porcentagem_investido']
        porcentagem_ideal = valores['porcentagem_ideal']
        print(f"Grupo: {grupo} | Valor Investido: {valor_investido:.2f} | Porcentagem Investida: {porcentagem_investida:.2f}% | Porcentagem Ideal: {porcentagem_ideal:.2f}%")

    print("\nPorcentagens Ajustadas:")
    for grupo, valores in resultado['resumo'].items():
        valor_ajustado = valores['valor_ajustado']
        quantidade_adicional = valores.get('quantia_adicional', 0)
        porcentagem_ajustada = valores['porcentagem_ajustada']
        porcentagem_ideal = valores['porcentagem_ideal']
        print(f"Grupo: {grupo} | Valor Ajustado: {valor_ajustado:.2f} | Quantidade Adicional: {quantidade_adicional:.2f} | Porcentagem Ajustada: {porcentagem_ajustada:.2f}% | Porcentagem Ideal: {porcentagem_ideal:.2f}%")

    print("\nDetalhamento dos valores:")
    for titulo in resultado['titulos']:
        tipo = titulo['tipo']
        descricao = titulo['descricao']
        valor_investimento = titulo['valor']
        print(f"Tipo: {tipo} | Descrição: {descricao} | Valor: {valor_investimento:.2f}")

    valor_total = resultado['patrimonio']
    valor_em_conta = resultado['valor_em_conta']
    total_investido = resultado['total_investido']
    aporte_necessario = resultado['aporte_necessario_para_igular']
    print(f"\nTotal Investido: R$ {total_investido:.2f}")
    print(f"Valor em conta: R$ {valor_em_conta:.2f}")
    print(f"Patrimônio Total: R$ {valor_total:.2f}")
    print(f"Aporte Necessário para Igualar: R$ {aporte_necessario:.2f}")


if __name__ == '__main__':
    main()
