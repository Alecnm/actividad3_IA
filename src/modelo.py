from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def entrenar_modelo(X, y):
    """
    Entrena un modelo de árbol de decisión con los datos proporcionados.
    
    :param X: Variables independientes
    :param y: Variable dependiente
    :return: El modelo entrenado, X_test, y_test
    """
    # Dividir los datos en conjuntos de entrenamiento y prueba (70% y 30%)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    # Crear el modelo de árbol de decisión
    modelo = DecisionTreeClassifier(max_depth=3)  # Ajuste de hiperparámetros (ejemplo)
    
    # Entrenar el modelo
    modelo.fit(X_train, y_train)
    
    return modelo, X_test, y_test

def evaluar_modelo(modelo, X_test, y_test):
    """
    Evalúa el modelo con el conjunto de prueba y calcula la precisión.
    
    :param modelo: Modelo entrenado
    :param X_test: Conjunto de prueba (variables independientes)
    :param y_test: Conjunto de prueba (variable dependiente)
    :return: Precisión del modelo
    """
    # Predecir valores
    y_pred = modelo.predict(X_test)
    
    # Calcular la precisión
    precision = accuracy_score(y_test, y_pred)
    
    return precision
