import pandas as pd
import data_processing
import scales
import pitches
import create_midi_file

data = pd.read_csv('data_sets/neo.csv')

df = pd.DataFrame(data=data)

#print(df.columns)

#print(df[['est_diameter_min', 'est_diameter_max', 'hazardous']])


scale = scales.return_scale('A', 'Major')

data_set = pitches.convert_pitch(scales.return_notes(scale, data_processing.data_to_note_processing(df['est_diameter_min'], scale)))
data_set2 = pitches.convert_pitch(scales.return_notes(scale, data_processing.data_to_note_processing(df['miss_distance'], scale)))
data_set3 = pitches.convert_pitch(scales.return_notes(scale, data_processing.data_to_note_processing(df['relative_velocity'], scale)))


create_midi_file.Midifile(data_set=data_set, bpm=80, duration=2, track_name='Test1')
create_midi_file.Midifile(data_set=data_set2, bpm=80, duration=4, track_name='Test2')
create_midi_file.Midifile(data_set=data_set3, bpm=80, duration=8, track_name='Test3')
