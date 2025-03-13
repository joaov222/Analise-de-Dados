file = 'gasolina.csv'  
data = pd.read_csv(file)

plt.figure(figsize=(12, 8))
sns.lineplot(data=data, x='dia', y='venda')

plt.title('Valor do Combustível por Dia')
plt.xlabel('Dia')
plt.ylabel('Valor')

plt.savefig('gasolina.png')
