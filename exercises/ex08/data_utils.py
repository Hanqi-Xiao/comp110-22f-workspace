"""Dictionary related utility functions."""

__author__ = "730295059"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read rows of a csv file."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values_one_line(table: list[dict[str, str]], column: str) -> list[str]:
    """One line, return column_values for one column."""
    return [idict[key] for idict in table for key in idict if key == column]


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Return column_values for one column."""
    return_list: list[str] = []
    for idict in table:
        for key in idict:
            if key == column:
                return_list.append(idict[key])
    return return_list


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """T transform from row to column wise table."""
    return_dict: dict[str, list[str]] = {}
    for dic in table:
        for key in dic:
            if key in return_dict:
                return_dict[key].append(dic[key])
            else:
                return_dict[key] = [dic[key]]
    return return_dict


def columnar_2(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """T transform from row to column wise table."""
    return_dict: dict[str, list[str]] = {}
    if len(table) == 0:
        return return_dict
    for i in table[0]:
        return_dict[i] = column_values(table, i)
    return return_dict

    
def head(original_dict: dict[str, list[str]], number: int = 5) -> dict[str, list[str]]:
    """Returns the first five rows of a column wise table."""
    head_dict: dict[str, list[str]] = dict()
    first: bool = True
    for key in original_dict:
        if first:
            first = False
            if number >= len(original_dict[key]):
                head_dict = original_dict
                return head_dict
        head_rows: list[str] = list()
        i: int = 0
        while i < number:
            head_rows.append(original_dict[key][i])
            i += 1
        head_dict[key] = head_rows
    return head_dict


def select(original_dict: dict[str, list[str]], columns: list[str]) -> dict[str, list[str]]:
    """Select from the table certain columns to form a new table."""
    head_dict: dict[str, list[str]] = dict()
    for column in original_dict:
        if column in columns:
            head_dict[column] = original_dict[column]
    return head_dict
        

def concat(table_1: dict[str, list[str]], table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combine two column wise tables."""
    new_table: dict[str, list[str]] = dict()
    for table in (table_1, table_2):
        for key in table:
            if key in new_table:
                cur_list: list[str] = table[key]
                for i in cur_list:
                    new_table[key].append(i)
            else:
                new_table[key] = table[key]
    return new_table


def count(input: list[str]) -> dict[str, int]:
    """Count unique features in a list."""
    out_dict: dict[str, int] = dict()
    for feature in input:
        if feature in out_dict:
            out_dict[feature] += 1
        else:
            out_dict[feature] = 1
    return out_dict