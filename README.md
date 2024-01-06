# Machine-Learning-Car-Value-Predictor

This Python program predicts the selling price of a car based on user-provided inputs using a linear regression model. The model is trained on a dataset containing information about various cars.

## Dependencies

- `pandas`
- `matplotlib`
- `scikit-learn`

Install these dependencies using:

```bash
pip install pandas matplotlib scikit-learn
```
## Dataset

Ensure you have a CSV file named 'cardekho_data.csv' in the same directory as the script. This file should contain relevant information about cars, including features such as Car Name, Year, Kms Driven, Transmission, and Selling Price.

## Usage

### Running the Program

Execute the script in a Python environment:

```bash
python car_price_prediction.py
```

## Input Information

The program will prompt you to enter specific details about the car you want to predict the selling price for, including Car Name, Year, Kms Driven, and Transmission type.

## Prediction

The program will use a pre-trained linear regression model to predict the selling price based on the entered information.

## Visualization

A bar chart will be displayed comparing the actual average selling price for the entered car in the specified year with the predicted selling price.

## Output

The predicted selling price will be printed to the console.

## Example

```bash
Enter Car Name: City
Enter Year: 2017
Enter Kms Driven: 50000
Enter Transmission (Automatic or Manual): Manual
```
## Note

- The program assumes that the input values are valid and match the format of the training data.
- Ensure the 'cardekho_data.csv' file is in the same directory as the script.
![Screenshot 2024-01-06 162034](https://github.com/mishram123/Machine-Learning-Car-Value-Predictor/assets/56270716/fa00b869-d838-4b74-a72d-9a8d06224975)

