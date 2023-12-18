import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score

# Шаг 1: Загрузка данных
data = pd.read_csv("titanic.csv")

# Шаг 2: Подготовка данных
# Преобразование категориальных признаков в числовой формат
label_encoder = LabelEncoder()
data['SexCode'] = label_encoder.fit_transform(data['Sex'])

# Заполнение пропущенных значений (в данном случае используем среднее значение для возраста)
data['Age'].fillna(data['Age'].mean(), inplace=True)

# Выбор признаков для обучения
features = ['PClass', 'Age', 'SexCode']
X = data[features]
y = data['Survived']

# Шаг 3: Разделение данных на обучающий и тестовый наборы
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Шаг 4: Создание и обучение модели с использованием One-Hot Encoding
# Создаем преобразователь, который преобразует категориальные признаки
# с использованием One-Hot Encoding, а затем создаем модель логистической регрессии
preprocessor = ColumnTransformer(
    transformers=[
        ('num', OneHotEncoder(), ['PClass'])
    ],
    remainder='passthrough'
)

model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', LogisticRegression())
])

model.fit(X_train, y_train)

# Шаг 5: Предсказание на тестовом наборе
predictions = model.predict(X_test)

# Вывод результатов для тестового прохода на 10 пассажирах
sample_passengers = X_test.head(10)
predictions_sample = model.predict(sample_passengers)

# Вывод предсказаний для 10 пассажиров
for i, prediction in enumerate(predictions_sample):
    passenger_data = sample_passengers.iloc[i]
    print(f"Passenger {i + 1}: Predicted Survived={prediction}, Actual Survived={y_test.iloc[i]}")
