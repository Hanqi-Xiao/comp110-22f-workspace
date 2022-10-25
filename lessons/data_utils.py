"""Working with CSV files custom scripts for practice."""

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read rows of a csv file."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    return [idict[key] for idict in table for key in idict if key == column]


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    return_list = []
    for idict in table:
        print(idict)
        for key in idict:
            print(type(key), type(column))
            if key == column:
                print("YESYESYES")
                return_list.append(idict[key])
    return return_list


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    return_dict = {}
    for dic in table:
        for key in dic:
            if key in return_dict:
                return_dict[key].append(dic[key])
            else:
                return_dict[key] = [dic[key]]
    return return_dict
