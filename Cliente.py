from datetime import datetime

class Cliente_bancario:
    def __init__(self, nome, idade, conta, agencia, numero_conta, cheque):
        self.nome = nome
        self.idade = idade
        self.conta = conta
        self.numero_conta = numero_conta
        self.agencia = agencia
        self.movm = []
        self.taxa_contrato = 500.0
        self.taxa_juros_mensal = 0.015
        self.taxa_seguro_mensal = 20.0
        self.cheque = cheque

    def depositar(self, valor):
        self.conta += valor
        data = datetime.now()
        self.movm.append([data.strftime("%d/%m/%Y"), 'Depósito', valor, self.conta])

    def sacar(self, valor):
        taxa = self.cheque 
        if self.conta + taxa >= valor:
            self.conta -= valor
            data = datetime.now()
            self.movm.append([data.strftime("%d/%m/%Y"), 'Saque', -valor, self.conta])
            return True
        else:
            return False

    def financiar(self, valor, nParcelas):
        i = self.taxa_juros_mensal
        n = nParcelas
        parcela_base = valor * (i * (1 + i) ** n) / ((1 + i) ** n - 1)
        parcela_total = parcela_base + self.taxa_seguro_mensal
        total_pago = parcela_total * n + self.taxa_contrato
        juros_total = total_pago - valor - (self.taxa_seguro_mensal * n) - self.taxa_contrato
        cet = ((total_pago / valor) - 1) * 100
        return {
            "valor_financiado": valor,
            "parcelas": n,
            "taxa_juros_mensal": i,
            "taxa_contrato": self.taxa_contrato,
            "taxa_seguro_mensal": self.taxa_seguro_mensal,
            "valor_parcela": parcela_total,
            "total_pago": total_pago,
            "juros_total": juros_total,
            "cet": cet
        }

    def extrato(self, data_inicial=None, data_final=None):
        if not self.movm:
            return []
        resultado = []
        if data_inicial and data_final:
            data_inicial = datetime.strptime(data_inicial, "%d/%m/%Y")
            data_final = datetime.strptime(data_final, "%d/%m/%Y")
            for movimentar in self.movm:
                data = datetime.strptime(movimentar[0], "%d/%m/%Y")
                if data_inicial <= data <= data_final:
                    resultado.append(movimentar)
        else:
            resultado = self.movm
        return resultado

    def saldo(self):
        return self.conta
        