pitches = {  # pitches based on central C (C4).
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


def convert_pitch(note_to_convert):
    pitch_val = pitches[note_to_convert]
    return pitch_val
