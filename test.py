import pandas as pd
import data_processing
import scales
import pitches
import create_midi_file

data = pd.read_csv('data_sets/neo.csv')

df = pd.DataFrame(data=data)

scale = scales.return_scale('A', 'Major')

data_set = pitches.convert_pitch(scales.return_notes(scale, data_processing.data_to_note_processing(df['est_diameter_min'], scale)))
data_set2 = pitches.convert_pitch(scales.return_notes(scale, data_processing.data_to_note_processing(df['miss_distance'], scale)))
data_set3 = pitches.convert_pitch(scales.return_notes(scale, data_processing.data_to_note_processing(df['relative_velocity'], scale)))
data_set4 = pitches.convert_pitch(scales.return_notes(scale, data_processing.data_to_note_processing(df['absolute_magnitude'], scale)))


def create_test(max_length, bpm):

    create_midi_file.Midifile(data_set=data_set, bpm=bpm, duration=2, track_name='Test1', max_length=max_length)
    create_midi_file.Midifile(data_set=data_set2, bpm=bpm, duration=4, track_name='Test2', max_length=max_length)
    create_midi_file.Midifile(data_set=data_set3, bpm=bpm, duration=8, track_name='Test3', max_length=max_length)
    create_midi_file.Midifile(data_set=data_set4, bpm=bpm, duration=2, track_name='Test4', max_length=max_length)


def describe_columns(data_set_to_desc):
    print(data_set_to_desc.columns)


#create_test(80, 120)

print(data_processing.data_to_duration_processing(data_set))