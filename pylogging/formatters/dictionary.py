def format_dict(data: dict):
    for element in data.keys():
        print('\u0009' '\u0009' '\u0009' + '\033[1;36m' + element + ":" + data.get(element))
