from midiutil.MidiFile import MIDIFile


class Midifile:
    time = 0
    track = 0

    notes_list = []

    def __init__(self, data_set, bpm, duration, track_name):
        mf = MIDIFile(1)

        mf.addTrackName(self.track, self.time, track_name)
        mf.addTempo(self.track, self.time, bpm)
        for pitch in data_set:
            mf.addNote(self.track, 0, pitch, self.time, duration, 100)
            self.time += duration

        with open('output/' + track_name + '.mid', 'wb') as output_file:
            mf.writeFile(output_file)
        print(f'Created midi file: {track_name}.mid')
