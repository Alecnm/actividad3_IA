import pandas as pd
import os
from modelo import entrenar_modelo, evaluar_modelo

current_directory = os.getcwd()
# Cargar datos
df = pd.read_csv(current_directory + '/data/transporte.csv')

# Convertir variables categóricas en numéricas
df['rutas'] = df['rutas'].astype('category').cat.codes
df['clima'] = df['clima'].astype('category').cat.codes
df['congestion'] = df['congestion'].astype('category').cat.codes

# Preparar datos (variables independientes y dependiente)
X = df[['rutas', 'pasajeros', 'tiempo_viaje', 'clima', 'congestion']]
y = df['espera_larga']

# Entrenar el modelo
modelo, X_test, y_test = entrenar_modelo(X, y)

# Evaluar el modelo
precision = evaluar_modelo(modelo, X_test, y_test)

print(f'Precisión del modelo: {precision:.2f}')