import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
from sklearn.model_selection import train_test_split

# Загрузка данных из файла
# Замените 'data.txt' на путь к вашему файлу данных
data = np.loadtxt('data.txt', delimiter=',')

# Разделение данных на признаки и метки
X = data[:, :-1]
y = data[:, -1]

# Разделение данных на тренировочный и тестовый наборы
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Построение модели
model = Sequential()
model.add(Dense(12, input_dim=X_train.shape[1], activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Компиляция модели
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Обучение модели
model.fit(X_train, y_train, epochs=15, batch_size=10, verbose=2)

# Предсказание по первым трем строкам датасета
predictions = model.predict(X_test[:3])
print("Predictions:", predictions)
