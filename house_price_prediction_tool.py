from prediction_tool.prediction_tool import prediction_tool
from data_fetching.data_fetcher import data_fetcher

# Training data file and example test data. To use own data change this to data.csv and add data in that file.
input_file = "example_data.csv"
# In the test data each list has values for house size, building year, and property size.
example_test_data = [
    [296, 1997, 1280],
    [138, 1998, 1841],
    [137, 1986, 1156]
    ]
# Websites to fetch data from.
websites = []


def house_price_prediction_tool(input_file, example_test_data):
    """Main function for the tool."""
    print("Welcome to the house price prediction tool!")
    no_exit = True
    while no_exit:
        chosen_option = option_input()
        match chosen_option:
            case 1:
                prediction_tool(input_file, example_test_data)
            case 2:
                data_fetcher(websites)
            case 3:
                no_exit = False


def option_input():
    """Function for getting options from the user."""
    chosen_option = None
    while chosen_option is None:
        try:
            print("Choose an option to execute.")
            print("1 for the predition tool")
            print("2 for data fetching")
            print("3 for exit")
            chosen_option = int(input())
        except ValueError:
            print("Invalid input! Input needs to be a number.")
    return chosen_option


if __name__ == '__main__':
    house_price_prediction_tool(input_file, example_test_data)
