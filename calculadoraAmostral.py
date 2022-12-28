quantPop = int(input("Informe a quantidade da população: "))

margemErro = int(input("Informe a margem de erro:"))

mgErro = (margemErro / 100)

def primAprox():
    return ((100 / margemErro) ** 2)

resultado = ((quantPop) * (primAprox())) / ((quantPop) + (primAprox()))


print ("---------------------------------------")
print ("Projeto 2 ANGÉLICA MONTEIRO CORREA")
print ("Curso Análise de Dados - Curso SENAC")
print ("---------------------------------------")

print ("CALCULADORA AMOSTRAL")

print ("Nivel de Confiança: 95%")
print ("Quantidade da população: ", quantPop)
print ("Margem de erro:", margemErro,"%")
print ("Quantidade mínima de pessoas a serem entrevistadas: ","%.0f"%resultado)