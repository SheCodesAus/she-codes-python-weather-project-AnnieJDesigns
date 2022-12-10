import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"



def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    #Answer
    date = datetime.fromisoformat(iso_string)
    return(date.strftime("%A %d %B %Y"))


# def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
#Answer
# def convert_f_to_c(temp_in_farenheit):
#     temp = float(temp_in_farenheit)
#     return(round(float((temp - 32) / 1.8), 1))

#tutor's help
# def convert_politely(farenheit):
#     celsius = convert_f_to_c(farenheit)
#     celsius = str(celsius)
#     formatted_celsius = format_temperature(celsius)
#     polite_statement = format_temperature + "Have a nice day"
#     return polite_statement

def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    pass

#Answer:
# def calculate_mean(weather_data):
#     total = 0
#     for data in weather_data:
#         total += float(data)
#     mean = total/ len(weather_data)
#     return float(mean)




def load_data_from_csv(csv_file):

    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """

   #Answer:
    # weather_data = []
    # with open(csv_file) as csv_file:
    #     results = csv.reader(csv_file)
    #     count = 0
    #     for row in results:
    #         if row == []:
    #             pass
    #         elif count != 0:
    #             updated_row = line
    #             updated_row[0]= row[0]
    #             updated_row[1]= int(row[1])
    #             updated_row[2]= int(row[2])
    #             weather_data.append(updated_row)
    #         count += 1
    # return weather_data



weather_data = []

def find_min(weather_data):

    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """

    if len(weather_data) == 0:
        return ()
    min_temp  = 999999999999
    min_index = 0
    index    = 0
    for element in weather_data:
        if int(element) <= int(min_temp):
            min_temp = float(element)
            min_index = index
        index += 1
    return(min_temp, min_index)
   
    # for row in weather_data:
    #     if row == []:
    #         pass
    #     elif row != 0:
    #         min_list.append(int(row[1])
    # minpos = int(min_list.index(min(min_list)))
       

  


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """




def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass
