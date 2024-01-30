# MusicTranscription
Exploring the use of neural networks to transcribe music.

# TODO
    - Write script to prepare and clean data from the Slakh dataset.
    - Find reasonable filters for audio.
    - Use reasonable processing method to extract valuable information.
    - Create prototype LSTM (or some other RNN based network) with CNN for midi.
    - Find a MIDI/Chord dataset for second phase of project.

# Setup
The Slakh dataset must be downloaded and then be brought into this folder before training can take place.
Please ensure that you convert the dataset to the Slakh2100-redux which removes duplicate midi files from the training data.

## Initial Notes:
Transcription to MIDI as a first step, transcription to chords afterwards.
Transcription to chords will require chord labeled datasets.

This involves training two models:
    - An initial model translates audio into the most relevant MIDI notes needed for harmonic analysis.
    - A second translates the MIDI notes into a set of chords over time

Songs have a variable number of tracks:
    - These tracks can include any synthesized instrument including drums.
    - Drums can be misleading when attempting to transcribe.
        - Drums sit in the lower register of pitches, can they be filtered out?

Research shows that RNN/CNN combination performs well on single instrument polyphonic recordings.
We do not have extensive research on chord retrieval (or chord transcription) on music from my current findings:
    - HOWEVER, we know that CNNs can work well on categorization tasks AND RNNs work well on sequential data:
        - i.e. a combination of CNN and RNN should work for chord transcription, reducing the dimensionality of the MIDI result
        - Hopefully this will allow us to get far more correct answers with far less resources than the use of (for example) a deep network of dense layers

Hypothesis:
    CONSIDER that if a RNN/CNN performs well in single instrument polyphonic recordings
        - Will the same combination work as effectively on multiple instrument polyphonic recordings?
        - Can we add intuitive filters (i.e. Sleep_2017) to help get better findings?


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