dia = int(input("Digite um número inteiro entre 1 e 7: "));
mensagem = "Hoje é um bom dia para aprender Python"

match dia:
    case 1:
        print("Domingo, "+mensagem);
    case 2:
        print("Segunda-Feira, "+mensagem);
    case 3:
        print("Terça-Feira, "+mensagem);
    case 4:
        print("Quarta-Feira, "+mensagem);
    case 5:
        print("Quinta-Feira, "+mensagem);
    case 6:
        print("Sexta-Feira, "+mensagem);
    case 7:
        print("Sabado, "+mensagem);
    case _:
        print("Dia Invalido");