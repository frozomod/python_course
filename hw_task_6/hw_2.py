import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split

class CustomModel:
    def __init__(self, input_dim, hidden_dim1, hidden_dim2, output_dim, epochs, batch_size):
        self.input_dim = input_dim
        self.hidden_dim1 = hidden_dim1
        self.hidden_dim2 = hidden_dim2
        self.output_dim = output_dim
        self.epochs = epochs
        self.batch_size = batch_size
        self.model = self.build_model()

    def build_model(self):
        model = Sequential()
        model.add(Dense(self.hidden_dim1, input_dim=self.input_dim, activation='relu'))
        model.add(Dense(self.hidden_dim2, activation='relu'))
        model.add(Dense(self.output_dim, activation='sigmoid'))
        model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
        return model

    def prepare_data(self, data_path):
        data = np.loadtxt(data_path, delimiter=',')
        X = data[:, :-1]
        y = data[:, -1]
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    def train(self):
        self.model.fit(self.X_train, self.y_train, epochs=self.epochs, batch_size=self.batch_size, verbose=2)

    def inference(self, input_data):
        return self.model.predict(input_data)

model_params = {
    'input_dim': 2,
    'hidden_dim1': 12,
    'hidden_dim2': 8,
    'output_dim': 1,
    'epochs': 15,
    'batch_size': 10
}

data_path = 'data.txt'

custom_model = CustomModel(**model_params)
custom_model.prepare_data(data_path)
custom_model.train()

input_data = np.array([[0.2, 0.8], [0.5, 0.3], [0.7, 0.6]])
predictions = custom_model.inference(input_data)
print("Predictions:", predictions)
