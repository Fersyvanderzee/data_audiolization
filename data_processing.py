import numpy as np


# Converts the data set to a general factor to divide or multiply with
def data_processing(data_set_to_convert, allowed_notes):
    mean = np.mean(data_set_to_convert)
    factor = mean / len(allowed_notes)
    values = []

    for val in data_set_to_convert:
        value = val / factor
        if value > len(allowed_notes):
            value = len(allowed_notes)
        elif value < 0:
            value = 0
        values.append(round(value))

    return values
