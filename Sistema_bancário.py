import textwrap

def menu():
    menu = """\n
    ___________menu__________
    [d]\t Depositar
    [s]\t Sacar
    [e]\t Extrato
    [nc]\t Nova Conta
    [lc]\t Listar Contas
    [nu]\t Novo Usuario
    [q]\t Sair
    => """
    return input( textwrap.dedent(menu))

def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR${valor:.2f}\n"
        print("\n===Depósito realizado com sucesso!===")

    else:
      print("\n@@@ Operação Falhou! o valor informado é invalido.@@@")

    return saldo, extrato
    

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques > limite_saques

    if excedeu_saldo:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente.@@@")

    elif excedeu_limite:
        print("\n@@@ Operação falhou! O valor do saque excede o limite.@@@")

    elif excedeu_saques:
        print("\n@@@ Operação falhou! Número máximo de saques excedido.@@@")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR${valor:.2f}\n"
        numero_saques += 1
        print("\n===Saque realizado com sucesso!")    

    else:
        print("n@@@ Operção falhou! O valor informado é inválido.@@@") 

    return saldo, extrato


def exibir_extrato(saldo, extrato):   
    print("\n============EXTRATO============")  
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("=====================")


def criar_usuario(usuarios): 
    cpf = input("Informe o CPF(somente o número):")   
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@Já existe usuario com esse CPF!@@@")
        return
    
    nome = input("Informe o nome completo:")
    data_nascimento = input("Informe a data de nascimeneto(dd-mm-aaa):")
    endereco = input("Informe o endereço(logradouro, nro - bairro - cidade/ siga do estado):")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("====Usuario criado com sucesso!===")

def filtrar_usuario(cpf, usuarios): 
   usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]   
   return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta,usuarios):  
   cpf = input("Informe o cpf do usuario:")
   usuario = filtrar_usuario(cpf,usuarios)

   if usuario:
       print("\n===Conta criada com sucesso!===")  
       return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
   
   print("\n@@@ Usuario não encontrado, fluxo de criação de conta encerrado!@@@")


def listar_contas(contas):
   for conta in contas:
        linha = f"""\
           Agência:\t{conta['agencia']}
           C/C:\t\t{conta['numero_conta']} 
           Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))   

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []


    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":  
              valor = float(input("Informe o valor do saque: ")) 
              saldo, extrato =  sacar(
              saldo = saldo,
              valor = valor,
              extrato = extrato,
              limite = limite,
              numero_saques = numero_saques,
              limite_saques = LIMITE_SAQUES,
            )


        elif opcao == "e":
          exibir_extrato(saldo, extrato)

        elif opcao == "nu":  
          criar_usuario(usuarios)

        elif opcao == "nc": 
          numero_conta = len(contas) +1
          conta = criar_conta("AGENCIA", numero_conta, usuarios)

          if conta:
            contas.append(conta)

        elif opcao == "lc":
          listar_contas(contas)

        elif opcao == "q":  
           break 


        else:
         print("Operação inválida, por favor selecione a operação desejada.")  

main()













       
       

                

 

