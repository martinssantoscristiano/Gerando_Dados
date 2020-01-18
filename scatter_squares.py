import matplotlib.pyplot as plt


x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, s=40)
# plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='nome', s=40)

# Definindo o titulo do gráfico e nomeia os eixos x e y
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Define o tamanho dos rótulos das marcações
plt.tick_params(axis='both', labelsize=14)

# Define o intrervalo de para cada eixo
plt.axis([0, 1100, 0, 1100000])


# plt.show() - mostra o  gráfico ao executar o programa
# salavando o gráfico com nome squares_plt.svg
plt.savefig('squares_plot.svg', bbox_inches='tight')