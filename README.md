# MusicTranscription
Exploring the use of neural networks to transcribe music.

# TODO
    - Write script to prepare and clean data from the Slakh dataset.
    - Find reasonable filters for audio.
    - Use reasonable processing method to extract valuable information.
    - Create prototype LSTM (or some other RNN based network) with CNN for MIDI.
    - Find a MIDI/Chord dataset for second phase of project.

# Setup
The Slakh dataset must be downloaded and then be brought into this folder before training can take place.
Please ensure that you convert the dataset to the Slakh2100-redux which removes duplicate midi files from the training data.

## Initial Notes:
Transcription to MIDI as a first step, transcription to chords afterwards.
Transcription to chords will require chord labeled datasets.

This involves training two models:

    - An initial model translates audio into the most relevant MIDI notes needed for harmonic analysis.
    - A second translates the MIDI notes into a set of chords over time.

Songs have a variable number of tracks:

    - These tracks can include any synthesized instrument including drums.
    - Drums can be misleading when attempting to transcribe.
        - Drums sit in the lower register of pitches, can they be filtered out?

How do we know which notes are relevant?

    - As previously mentioned, some instruments can be removed from consideration (such as drums).
    - We can also look at the length or frequency a note is played in a bar, louder, frequent or longer notes should have a higher weight for relevance to a chord label. This is because quite, infrequent and faster notes have less impact on the bar, and thus do not have as much impact on the interpretation of a chord (in general terms).

How and where to determine the BPM?

    - BPM should be determined early on while the MIDI is being generated. This will allow the MIDI result
    to have each note's timing quantized before sending to the chord analysis step.

We do not have extensive research on chord retrieval (or chord transcription) on music from my current findings:

    - HOWEVER, we know that CNNs can work well on categorization tasks AND RNNs work well on sequential data:
        - i.e. a combination of CNN and RNN should work for chord transcription, reducing the dimensionality of the MIDI result
        - Hopefully this will allow us to get far more correct answers with far less resources than the use of (for example a deep network of dense layers

Research shows that RNN/CNN combination performs well on single instrument polyphonic recordings.

Hypothesis:
    CONSIDER that if a RNN/CNN performs well in single instrument polyphonic recordings

        - Will the same combination work as effectively on multiple instrument polyphonic recordings?
        - Can we add intuitive filters (i.e. Sleep_2017) to help get better findings?

## Key Questions:
How should chords be labeled and what mechanism should be used for interpreting chords?

    - The labeling of chords is systematic, focusing on the number of notes and their relative distance from the root note.
    - Chords can thus be labeled based on a mapping of MIDI notes and their relative distance to chord labels.

What should the final output look like?

    - As of right now the ideal would be to have a chord sheet that is separated into bars; this requires an element of BPM and rhythm analysis, or for the BPM and rhythm to be a part of the data. For training purposes we will need data with rhythm information either way.

Why is chord analysis the objective?

    - Chord analysis is more abstract than classical music notation, this means that there is often more creative freedom in defining chords; some people may see a piano piece with a C chord in the left hand and a melody focusing on D in the right and label that as a C9 chord, whereas others would label it a plain C chord.

How will we procure data for training the model to identify chords from MIDI?

    - We can generate midi data from a dataset of chords and chord progressions using a library like `https://code.google.com/archive/p/midiutil/`.


# References

## Slakh2100-redux (production) and BabySlakh (testing)
@inproceedings{manilow2019cutting,
  title={Cutting Music Source Separation Some {Slakh}: A Dataset to Study the Impact of Training Data Quality and Quantity},
  author={Manilow, Ethan and Wichern, Gordon and Seetharaman, Prem and Le Roux, Jonathan},
  booktitle={Proc. IEEE Workshop on Applications of Signal Processing to Audio and Acoustics (WASPAA)},
  year={2019},
  organization={IEEE}
}

## Automatic Music Transcription: Generating MIDI From Audio
@misc{Grossman_Grossman_2020,
    title={Automatic Music Transcription: Generating MIDI FROM AUDIO},
    url={http://cs230.stanford.edu/projects_spring_2020/reports/38948801.pdf},
    journal={Stanford.edu},
    publisher={Stanford},
    author={Grossman, Aitan and Grossman, Josh},
    year={2020},
    month={Jun}
}

## Automatic Music Transcription with Convolutional Neural Networks Using Intuitive Filter Shapes
@misc{Sleep_2017,
    title={Automatic music transcription with convolutional neural networks using intuitive filter shapes},
    url={https://core.ac.uk/download/pdf/158452997.pdf},
    journal={Core},
    publisher={California Polytechnic State University},
    author={Sleep, Jonathan},
    year={2017},
    month={Oct}
}