import datetime
import os
import pickle


def save_param(param_name, param_value, filename="saved.pkl"):
    params_dict = get_all_params(filename="saved.pkl")
    params_dict[param_name] = param_value

    with open(filename, 'wb') as file_handle:
        pickle.dump(params_dict, file_handle)


def get_all_params(filename="saved.pkl"):
    if not os.path.isfile(filename):
        with open(filename, 'wb') as file_handle:
            pickle.dump({"<ДатаВремя создания>": datetime.datetime.now()}, file_handle)

    with open(filename, "rb") as file_handle:
        params_dict = pickle.load(file_handle)

    return params_dict


def load_param(param_name, default="", filename="saved.pkl"):
    params_dict = get_all_params(filename=filename)

    return params_dict.get(param_name, default)


def is_cyrillic_and_sort(s):
    s = s[0].strip()
    return (not 'А' <= s[0] <= 'я' or 'а' <= s[0] <= 'я', s[0])
