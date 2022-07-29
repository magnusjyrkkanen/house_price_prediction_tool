import numpy as np

# Training data file and example test data. To use own data change this to data.csv and add data in that file.
input_file = "example_data.csv"
# In the test data each list has values for house size, building year, and property size.
example_test_data = [
    [296, 1997, 1280],
    [138, 1998, 1841],
    [137, 1986, 1156]
    ]


def house_price_prediction_tool(input_file, example_test_data):
    print("Welcome to the house price prediction tool!")
    test_data = example_test_data

    predict_price(input_file, test_data)


def predict_price(input_file, test_data):
    # Set the output settings for easier reading.
    np.set_printoptions(precision=1)

    # Prepare learning data.
    # Preparing list for the house prices.
    prices = []
    # Preparing list for the rest of the data.
    values = []
    data = np.genfromtxt(input_file, dtype='int64', delimiter=",", skip_header=1)
    # print(f"Data {data}")

    for line in data:
        prices.append(line[len(line)-1])
        values.append(line[:len(line)-1])
    y = np.asarray(prices)
    x = np.asarray(values)
    c = np.linalg.lstsq(x, y, rcond=None)[0]

    x_test = np.asarray(test_data)
    predicted_prices = x_test @ c

    for i in range(len(test_data)):
        print(f"For the given data the price for the house {i + 1} could be {int(predicted_prices[i])}.")


if __name__ == '__main__':
    house_price_prediction_tool(input_file, example_test_data)
