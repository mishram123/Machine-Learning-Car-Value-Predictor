import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('cardekho_data.csv')

label_encoder_car_name = LabelEncoder()
df['Car_Name'] = label_encoder_car_name.fit_transform(df['Car_Name'])

label_encoder_transmission = LabelEncoder()
df['Transmission'] = label_encoder_transmission.fit_transform(df['Transmission'])

# These are the inputs and output. The learning model will learn from the top 4 to predict the y value
X = df[['Car_Name', 'Year', 'Kms_Driven', 'Transmission']]
y = df['Selling_Price']

model = LinearRegression()

model.fit(X, y)

# these are the inputs the user must give
car_name_input = input("Enter Car Name: ")
year_input = int(input("Enter Year: "))
kms_driven_input = int(input("Enter Kms Driven: "))
transmission_input = input("Enter Transmission (Automatic or Manual): ")

# Here the learning model will transform user inputs
car_name_encoded = label_encoder_car_name.transform([car_name_input])[0]
transmission_encoded = label_encoder_transmission.transform([transmission_input])[0]

# In this code the model will predict the selling price
user_input_data = [[car_name_encoded, year_input, kms_driven_input, transmission_encoded]]
predicted_selling_price = model.predict(user_input_data)[0]

# Here it will the average selling price for the entered car from the given year as a comparison
car_data = df[(df['Car_Name'] == car_name_encoded) & (df['Year'] == year_input)]
actual_prices = car_data['Selling_Price']
car_labels = label_encoder_car_name.inverse_transform([car_name_encoded])[0]

# Now we will plot the visualization
fig, ax = plt.subplots()
ax.bar('Average Selling Price', actual_prices.mean(), label='Actual Selling Price')
ax.bar('Your Predicted Selling Price', predicted_selling_price, label='Predicted Selling Price')
ax.set_title(f'Average Selling Price for {car_labels} in {year_input}')
ax.set_ylabel('Price')
ax.legend()

for p in ax.patches:
    ax.annotate(f'{p.get_height():.2f}', (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', xytext=(0, 10), textcoords='offset points')
plt.show()

print(f'Predicted Selling Price: {predicted_selling_price}')
