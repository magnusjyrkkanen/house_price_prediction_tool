from prediction_tool.prediction_tool import prediction_tool

# Training data file and example test data. To use own data change this to data.csv and add data in that file.
input_file = "example_data.csv"
# In the test data each list has values for house size, building year, and property size.
example_test_data = [
    [296, 1997, 1280],
    [138, 1998, 1841],
    [137, 1986, 1156]
    ]


def house_price_prediction_tool(input_file, example_test_data):
    """Main function for the tool."""
    prediction_tool(input_file, example_test_data)


if __name__ == '__main__':
    house_price_prediction_tool(input_file, example_test_data)
