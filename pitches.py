# pitches based on central C (C4)

pitches = {
    'C': 48,
    'C#': 49,
    'Db': 49,
    'D': 50,
    'D#': 51,
    'Eb': 51,
    'E': 52,
    'F': 53,
    'F#': 54,
    'Gb': 54,
    'G': 55,
    'G#': 56,
    'Ab': 56,
    'A': 57,
    'A#': 58,
    'Bb': 58,
    'B': 59
}


# Converts the value to a pitch
def convert_pitch(note_to_convert):
    pitch_val = pitches[note_to_convert]
    return pitch_val


# Converts the value to the nearest pitch.
# Takes 2 arguments:
# - pitches to allow --> which pitches can be chosen
# - pitch --> the pitch to process
def return_closest_pitch(pitches_to_allow, pitch):
    return min(pitches_to_allow, key=lambda x: abs(x - pitch))