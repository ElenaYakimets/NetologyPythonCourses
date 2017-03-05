import osa


def read_lines_from_file(input_path):
    with open(input_path) as input_file:
        return input_file.readlines()


def average_temperature_f_to_c(input_path):
    url = 'http://www.webservicex.net/ConvertTemperature.asmx?WSDL'
    client = osa.client.Client(url)
    converted_temperature_c = 0
    file_lines = read_lines_from_file(input_path)
    for temperature_line in file_lines:
        temperature_f = int(temperature_line.split(" ")[0])
        converted_temperature_c += client.service.ConvertTemp(Temperature=temperature_f, FromUnit='degreeFahrenheit',
                                                              ToUnit='degreeCelsius')
    average_temperature_c = converted_temperature_c / len(file_lines)
    print(average_temperature_c)
    return average_temperature_c


average_temperature_f_to_c(
    "C:\\Users\\Taya\\Desktop\\Coursera analytics\\Python\\python-netology\\currency_rate, xml, soap\\temps.txt")