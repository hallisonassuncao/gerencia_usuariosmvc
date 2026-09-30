def menu_principal():
 print("\n===== MENU PRINCIPAL =====")
 print("1 - Listar usuários")
 print("2 - Cadastrar usuário")
 print("3 - Atualizar usuário")
 print("4 - Excluir usuário")
 print("0 - Sair")
 return input("\nEscolha uma opção: ")

def mostrar_usuarios(lista):
    print("\n=== Lista de Usuários ===")
    if not lista:
        print("Nenhum usuário encontrado.")
    else:
        for usuario in lista:
            print(f"ID: {usuario[0]} | Nome: {usuario[1]} | Email: {usuario[2]}")

def solicitar_dados_usuario():
 nome = input("Nome: ")
 email = input("E-mail: ")
 return nome, email

def mensagem(texto):
 print(texto)

def solicitar_id():
    try:
        return int(input("Digite o ID do usuário: "))
    except ValueError:
        mensagem("ID inválido.")
        return None

 