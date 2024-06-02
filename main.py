import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

ecommerce_data = pd.read_csv('Ecommerce_DBS.csv')
ecommerce_data.columns = ecommerce_data.columns.str.strip()

# Verificar valores ausentes
missing_values = ecommerce_data.isnull().sum()

# Remover linhas com valores ausentes
ecommerce_data.dropna(inplace=True)

# Selecionar apenas as colunas necessárias
columns_to_keep = ['Customer ID','Purchase Date','Product Category','Product Price','Quantity','Total Purchase Amount', 'NPS','Customer Age','Gender','Source']
ecommerce_data = ecommerce_data[columns_to_keep]

ecommerce_data['Purchase Date'] = pd.to_datetime(ecommerce_data['Purchase Date'], format='%d/%m/%Y')

# Filtrar dados dos últimos 3 anos
three_years_ago = datetime.now().year - 3
recent_data = ecommerce_data[ecommerce_data['Purchase Date'].dt.year >= three_years_ago]

# Agrupar por produto e somar as quantidades
most_sold_products = recent_data.groupby('Product Category')['Quantity'].sum().sort_values(ascending=False)
print("Produto mais vendido nos últimos 3 anos:\n", most_sold_products.head(1))
print("\n")

# Encontrar o produto mais caro e mais barato
most_expensive_product = ecommerce_data.loc[ecommerce_data['Product Price'].idxmax()]
cheapest_product = ecommerce_data.loc[ecommerce_data['Product Price'].idxmin()]

print("Produto mais caro:\n", most_expensive_product)
print("\n")
print("Produto mais barato:\n", cheapest_product)
print("\n")

# Categorias mais e menos vendidas
category_sales = ecommerce_data.groupby('Product Category')['Quantity'].sum().sort_values(ascending=False)
print("Categoria mais vendida:\n", category_sales.head(1))
print("\n")
print("Categoria menos vendida:\n", category_sales.tail(1))
print("\n")

# Categorias mais caras e menos caras
category_price = ecommerce_data.groupby('Product Category')['Product Price'].mean().sort_values(ascending=False)
print("Categoria mais cara:\n", category_price.head(1))
print("\n")
print("Categoria menos cara:\n", category_price.tail(1))
print("\n")

# Produto com melhor e pior NPS
best_nps_product = ecommerce_data.loc[ecommerce_data['NPS'].idxmax()]
worst_nps_product = ecommerce_data.loc[ecommerce_data['NPS'].idxmin()]

print("Produto com melhor NPS:\n", best_nps_product)
print("\n")
print("Produto com pior NPS:\n", worst_nps_product)
print("\n")

# Análise de público por gênero e idade
public_analysis = ecommerce_data.groupby(['Gender', 'Customer Age', 'Source'])['Quantity'].sum().reset_index()
print("Análise de público por gênero e idade:\n", public_analysis)
print("\n")

# Análise de canal ideal
channel_analysis = ecommerce_data.groupby('Source')['Quantity'].sum().sort_values(ascending=False)
print("Análise de Canal Ideal:\n", channel_analysis)
print("\n")

# Análise de público por gênero, idade e canal
general_analysis = ecommerce_data.groupby(['Gender', 'Customer Age', 'Source'])['Quantity'].sum().sort_values(ascending=False)
print("Análise de público por gênero, idade e canal:\n", general_analysis.head(1))


#Remover """ para plotar

"""# Plotar os produtos mais vendidos
plt.figure(figsize=(10, 6))
sns.barplot(x=most_sold_products.index, y=most_sold_products.values)
plt.title('Produtos mais vendidos nos últimos 3 anos')
plt.xlabel('Categoria de Produto')
plt.ylabel('Quantidade Vendida')
plt.xticks(rotation=45)
plt.show()"""

"""# Plotar a análise
plt.figure(figsize=(14, 8))
sns.barplot(data=public_analysis, x='Customer Age', y='Quantity', hue='Gender')
plt.title('Análise de Público por Gênero e Idade')
plt.xlabel('Idade')
plt.ylabel('Quantidade Vendida')
plt.legend(title='Gênero')
plt.show()"""

"""# Plotar a análise de canal
plt.figure(figsize=(10, 6))
sns.barplot(x=channel_analysis.index, y=channel_analysis.values)
plt.title('Análise de Canal Ideal')
plt.xlabel('Fonte')
plt.ylabel('Quantidade Vendida')
plt.xticks(rotation=45)
plt.show()"""
