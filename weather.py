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


def convert_f_to_c(temp_in_farenheit):
    temp = float(temp_in_farenheit)
    return(round(float((temp - 32) / 1.8), 1))

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
def calculate_mean(weather_data):
    total = 0
    for data in weather_data:
        total += float(data)
    mean = total/ len(weather_data)
    return float(mean)




def load_data_from_csv(csv_file):

    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """

#    Answer:
    weather_data = []
    with open(csv_file) as csv_file:
        results = csv.reader(csv_file)
        count = 0
        for row in results:
            if row == []:
                pass
            elif count != 0:
                updated_row = row
                updated_row[0]= row[0]
                updated_row[1]= int(row[1])
                updated_row[2]= int(row[2])
                weather_data.append(updated_row)
            count += 1
    return weather_data

def find_min(weather_data):

    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """
    if len(weather_data) == 0:
        return ()
    min_temp  = 9999999999
    min_index = 0
    index    = 0
    for element in weather_data:
        if int(element) <= int(min_temp):
            min_temp = float(element)
            min_index = index
        index += 1
    return(min_temp, min_index)

def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    if len(weather_data) == 0:
        return ()
    max_temp  = 0
    max_index = 0
    index    = 0
    for element in weather_data:
        if int(element) >= int(max_temp):
            max_temp = float(element)
            max_index = index
        index += 1
    return(max_temp, max_index)

def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    
#5 Day Overview
      # The lowest temperature will be 9.4°C, and will occur on Friday 02 July 2021.
      # The highest temperature will be 20.0°C, and will occur on Saturday 03 July 2021.
      # The average low this week is 12.2°C.
      # The average high this week is 17.8°C.

    #now we need to calculate each element in the output string and insert them in
    num_days = len(weather_data)

    #create arrays with the min_temp and max_temps
    min_temps = []
    max_temps = []
    for element in weather_data:
        min_temps.append(element[1])
        max_temps.append(element[2])

    #use the min temp function to get the min_temp and index
    low_temp_day = find_min(min_temps)
    high_temp_day = find_max(max_temps)

    #get the low temp number, convert to farenheit, add the degrees symbol and get day details
    low = convert_f_to_c(low_temp_day[0])
    low_str = format_temperature(low)
    low_index = low_temp_day[1]
    low_day_str = convert_date(weather_data[low_index][0])

    high = convert_f_to_c(high_temp_day[0])
    high_str = format_temperature(high)
    high_index = high_temp_day[1]
    high_day_str = convert_date(weather_data[high_index][0])

    #calculate the mean low and mean high, convert to celsius and add the degrees symbol
    mean_low = convert_f_to_c(calculate_mean(min_temps))
    mean_low_str = format_temperature(mean_low)
    mean_high = convert_f_to_c(calculate_mean(max_temps))
    mean_high_str = format_temperature(mean_high)

    output = []
    output.append(f"{num_days} Day Overview\n")
    output.append(f"  The lowest temperature will be {low_str}, and will occur on {low_day_str}.\n")
    output.append(f"  The highest temperature will be {high_str}, and will occur on {high_day_str}.\n")
    output.append(f"  The average low this week is {mean_low_str}.\n")
    output.append(f"  The average high this week is {mean_high_str}.\n")

    output_string = ''.join(output)

    #input these variables into the preformatted string
    return output_string


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    daily_summary_template = "---- {day} ----\n  Minimum Temperature: {min}\n  Maximum Temperature: {max}\n"

    if not weather_data:
        return

    daily_summaries = []

    for element in weather_data:
        temp_day = convert_date(element[0])
        temp_min = format_temperature(convert_f_to_c(element[1]))
        temp_max = format_temperature(convert_f_to_c(element[2]))

        temp_summary = daily_summary_template.format(day=temp_day, min=temp_min, max=temp_max)

        daily_summaries.append(temp_summary)

    result_string = "\n".join(daily_summaries) + "\n"

    return result_string
