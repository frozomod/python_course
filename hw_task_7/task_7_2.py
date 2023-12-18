import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score

data = pd.read_csv("titanic.csv")
label_encoder = LabelEncoder()
data['SexCode'] = label_encoder.fit_transform(data['Sex'])

data['Age'].fillna(data['Age'].mean(), inplace=True)

features = ['PClass', 'Age', 'SexCode']
X = data[features]
y = data['Survived']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

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

predictions = model.predict(X_test)

sample_passengers = X_test.head(10)
predictions_sample = model.predict(sample_passengers)

for i, prediction in enumerate(predictions_sample):
    passenger_data = sample_passengers.iloc[i]
    print(f"Passenger {i + 1}: Predicted Survived={prediction}, Actual Survived={y_test.iloc[i]}")
