import osa


def read_lines_from_file(input_path):
    with open(input_path) as input_file:
        return input_file.readlines()


def count_route_length(input_path):
    url = 'http://www.webservicex.net/length.asmx?WSDL'
    client = osa.client.Client(url)
    route_length = 0
    file_lines = read_lines_from_file(input_path)
    for route_line in file_lines:
        single_route_length = route_line.split(" ")[1].replace(",", "")
        route_length += client.service.ChangeLengthUnit(LengthValue=single_route_length, fromLengthUnit='Miles',
                                                        toLengthUnit='Kilometers')
    print("%.2f" % route_length)
    return route_length


count_route_length(
    "/Users/crashover/PycharmProjects/Netology/converter/travel.txt")