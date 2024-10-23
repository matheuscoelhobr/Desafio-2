import textwrap


def menu():
    menu = """\n
    ================ MENU =================
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [0]\tSair
    =======================================
    => """
    return input(textwrap.dedent(menu))



def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação errada! Você não tem saldo na conta suficiente.")
    
    elif excedeu_limite:
        print("Operação errada! O valor do saque excede o limite da sua conta.")
    
    elif excedeu_saques:
        print("Operação errada! Número máximo de saque excedido.")
    
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    
    else:
        print("Operação errada! O valor informado é inválido.")
    
    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print("\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ EXTRATO ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
    print("Os processos não foram realizados com sucesso." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")


def criar_usuario(usuarios):
    cpf = input("Informe o seu CPF(somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Já existe o usuário com esse CPF! Por favor tente outro.")
        return
    
    nome = input("informe o seu nome completo: ")
    data_de_nascimento = input("Informe sua data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe seu enderço (logradouro, num - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_de_nascimento": data_de_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o seu CPF de usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("Usuário não encontrado, encerrando a criação de conta!")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def main():
    usuarios = []
    contas = []
    agencia = "0001"
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:
        opcao = menu()

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)
        
        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
        
        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)
    
        elif opcao =="nu":
            criar_usuario(usuarios)
    
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(agencia, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        
        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "0":
            break

        else:
            print("Operação incorreta, por favor selecione novamente a operação desejada.")

main()