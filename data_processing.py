import numpy as np


# Converts the data set to a general factor to divide or multiply with
def data_to_note_processing(data_set_to_convert, allowed_notes):
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


#Does not work yet!
def data_to_duration_processing(data_set_to_convert):
    durations = []
    max_val = max(data_set_to_convert)
    min_val = min(data_set_to_convert)
    for val in data_set_to_convert:
        if val < (max_val * 0.33):
            duration = 2
        elif (max_val * 0.33) < val < (max_val * 0.66):
            duration = 4
        else:
            duration = 8
        durations.append(duration)
    return durations

