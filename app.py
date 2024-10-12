#função do menu 
def exebir_menu():
    print("0 - Sair do programa.")
    print("1.Quadrado")
    print("2.Triângulo")
    print("3.Círculo")
    print("4.Trapézio")

#lambdas
circulo = lambda R: 3.14 * R ** 2
quadrado = lambda L: L**2
triangulo = lambda B, A: B*A / 2 
trapezio = lambda BM, bm, h: ((BM + bm) * h) / 2

   
   
while True:
    exebir_menu()
    opcao = input("Opção desejada: ")
    
    match opcao:
        case "0":
             print("Programa encerrado!")
             break
        case '1':
            r = float(input("Digite o raio do Círculo: ").replace(",","."))
            print(f"A área do Círculo é: {circulo(r)}")
            continue
        case'2':
          l = float(input("Digite o lado do Quadrado: ").replace(",","."))
          print(f"A area do Quadrado é: {quadrado(l)}.")
          continue
        case '3':
         base = float(input("Digite a base do Triângulo: ").replace(",","."))
         altura = float(input("Digite a altura do Triângulo: ").replace(",","."))
         print(f"A area do Triângulo é: {triangulo(base,altura)}.")
         continue
        case '4':
         base_maior = float(input("Digite a base maior do Trapézio: ").replace(",","."))
         base_menor = float(input("Digite a base menor do Trapézio: ").replace(",","."))
         altura = float(input("Digite a altura do Trapézio: "))
         print(f"A área do Trapézio é: {trapezio(base_maior, base_menor, altura)}")
         continue
        case _ :
         print("Opção inválida!")



