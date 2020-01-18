from matplotlib import pyplot as plt

# Definindo os dados
x_values = list(range(5001))
cubes = [x**3 for x in x_values]

# plotando os valores dos eixos x e y
#plt.scatter(x_values, cubes, edgecolors='none', s=40)
plt.scatter(x_values, cubes, edgecolor='none', c=cubes, cmap=plt.cm.BuGn, s=40)

# Definindo o titulo do gráfico e nomeia os eixos x e y
plt.title("Cubes", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cube of value", fontsize=14)

# Define o tamanho dos rótulos das marcações
plt.tick_params(axis='both', labelsize=14)

# Define o intrervalo de para cada eixo
plt.axis([0, 5100, 0, 5100**3])

# - mostra o  gráfico ao executar o programa
plt.show() 
# salavando o gráfico com nome squares_plt.svg
# plt.savefig('visualiza_dados.svg', bbox_inches='tight')