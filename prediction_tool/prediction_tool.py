import numpy as np


def prediction_tool(input_file, example_test_data):
    """Main function for the tool that prepares the data."""
    print("Welcome to the house price prediction tool!")
    # Ask user if they want to give data to use (for one or more houses) or use example test data.
    print("Do you want to give data for a house to use or use example test data?")

    input_text = "Enter 1 to give data or enter 2 to use example data "
    invalid_text = "Invalid input! The input needs to be number 1 or 2."
    choice = value_input(input_text, invalid_text, phase=1)

    # Let user input data they want.
    if choice == 2:
        test_data = example_test_data
    else:
        print(
            "Enter house living space size, building year and property size for as many houses you want. "
            "Input sizes in squaremeters to get proper results."
        )

        test_data = []
        more_data = True

        while more_data:
            house_data = []
            input_texts = [
                "Enter value for the house size ",
                "Enter value for the house building year ",
                "Enter value for the property size "
            ]
            for i in range(3):
                value = value_input(input_texts[i])
                house_data.append(value)
            test_data.append(house_data)

            input_text = "Enter 1 to give data for additional house or enter 2 to continue "
            invalid_text = "Invalid input! The input needs to be number 1 or 2."
            choice = value_input(input_text, invalid_text, phase=3)
            # If user doesn't want to add more houses, exit while-loop.
            if choice == 2:
                more_data = False

    # Call the prediction method.
    predict_price(input_file, test_data)

    print("Hopefully that was an useful prediction!")


def predict_price(input_file, test_data):
    """Function to make the prediction with linear regression."""
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
        print(f"The price for the house {i + 1} could be {int(predicted_prices[i])}.")


def value_input(input_text, invalid_text="Invalid input! The input needs to be a number.", phase=0):
    """Function for getting the correct input from user."""
    choice = None
    while choice is None:
        try:
            choice = int(input(input_text))
            if phase in [1, 3]:
                if choice not in [1, 2]:
                    choice = None
                    print(invalid_text)
        except ValueError:
            print(invalid_text)
    return choice
