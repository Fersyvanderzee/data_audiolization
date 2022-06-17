# Processes the data set to an array in order to convert to pitches
def data_processing(data_set):
    values = []
    for val in data_set:
        values.append(val)
    return values


# Converts the data set to a general factor to divide or multiply with
def convert_to_factor(data_set_to_convert, min_pitch, max_pitch):
    val_factor = 0
    for val in data_set_to_convert:
        val_factor = val_factor + (val / min_pitch)
        val_factor = val_factor + (val / max_pitch)
    factor = val_factor / len(data_set_to_convert * 2)
    return factor


