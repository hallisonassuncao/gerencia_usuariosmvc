from controller.usuario_controller import UsuarioController
from view.usuario_view import menu_principal


def main():
    controller = UsuarioController()

    while True:
        try:
            opcao = menu_principal()

            if opcao == "1":
                controller.listar()
            elif opcao == "2":
                controller.cadastrar()
            elif opcao == "3":
                controller.atualizar()
            elif opcao == "4":
                controller.excluir()
            elif opcao == "0":
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida. Tente novamente.")

        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")


if __name__ == "__main__":
    main()
