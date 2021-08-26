largura = float(input("Digite a largura da parede em metros que deseja pintar: "))
altura = float(input("Digite a altura da parede em metros que deseja pintar:   "))

area = (largura * altura)

tinta = (area / 2)


print("A largura da parede é de {} metros, com uma altura de {} metros".format(largura,altura)+
     "\ne sua area sendo {} metros quadrados, portanto a quantidade de tinta necessaria será de {} litros" .format(area,tinta))

