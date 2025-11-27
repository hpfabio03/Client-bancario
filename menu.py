from Cliente import Cliente_bancario

cliente = Cliente_bancario("Fabio", 20, 10000, "0001", "12345-6", 500)

def mostrar_extrato(movimentacoes):
    if not movimentacoes:
        print("n/a")
    else:
        for mov in movimentacoes:
            print(f"{mov[0]} | {mov[1]} | {mov[2]:.2f} | saldo: {mov[3]:.2f}")

while True:
    print(f"\nCliente: {cliente.nome} | Conta: {cliente.numero_conta} | Agência: {cliente.agencia}")
    print("Saldo atual: R$", cliente.saldo())
    print("[1] Depositar")
    print("[2] Sacar")
    print("[3] Extrato")
    print("[4] Simular Financiamento")
    print("[0] Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        valor = float(input("Valor a depositar: "))
        cliente.depositar(valor)
        print(f"Depósito de {valor}R$ efetuado.")
    elif opcao == '2':
        valor = float(input("Valor a sacar: "))
        if cliente.sacar(valor):
            if cliente.saldo() < 0:
                print(f"Saque de {valor}R$ realizdo ultilizando o cheuque especial\nSaldo atual: {cliente.saldo():.2f}")
            else:
                print(f"saque efetuado no valor de {valor}")
        else:
            print(f"Saldo insuficiente")
    elif opcao == '3':
        data_inicial = input("Data inicial (dd/mm/yyyy) ou Enter para tudo: ")
        data_final = input("Data final (dd/mm/yyyy) ou Enter para tudo: ")
        if data_inicial and data_final:
            mostrar_extrato(cliente.extrato(data_inicial, data_final))
        else:
            mostrar_extrato(cliente.extrato())
    elif opcao == '4':
        valor = float(input("Valor do financiamento: "))
        nParcelas = int(input("Número de parcelas: "))
        resultado = cliente.financiar(valor, nParcelas)
        print("\n--- Simulação de Financiamento ---")
        print(f"Valor financiado: R$ {resultado['valor_financiado']:.2f}")
        print(f"Parcelas: {resultado['parcelas']}")
        print(f"Taxa de juros mensal: {resultado['taxa_juros_mensal']*100:.2f}%")
        print(f"Taxa de contrato: R$ {resultado['taxa_contrato']:.2f}")
        print(f"Taxa mensal de seguro: R$ {resultado['taxa_seguro_mensal']:.2f}")
        print(f"Valor da parcela (com seguro): R$ {resultado['valor_parcela']:.2f}")
        print(f"Total pago: R$ {resultado['total_pago']:.2f}")
        print(f"Juros total: R$ {resultado['juros_total']:.2f}")
        print(f"Custo Efetivo Total (CET): {resultado['cet']:.2f}%")
    elif opcao == '0':
        break
    else:
        print("Opção inválida.")