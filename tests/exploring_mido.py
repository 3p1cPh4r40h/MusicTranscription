import mido
import os

path="babyslakh_16k/Track00004/MIDI/S00.mid"

midi_file = mido.MidiFile(path)

print(midi_file)