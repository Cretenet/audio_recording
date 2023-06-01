"""from pydub import AudioSegment
import numpy as np


def clear_audio(audio_number):
    # Set the threshold for what constitutes silence
    SILENCE_THRESHOLD = -40  # dB
    # Load the audio file
    audio = AudioSegment.from_wav(f'audios/audio{audio_number}.wav')
    # Convert audio to numpy array
    samples = np.array(audio.get_array_of_samples())

    # Convert to mono
    if audio.channels == 2:
        samples = samples.reshape((-1, 2))
        samples = samples.mean(axis=1)

    # Find points that cross the silence threshold
    above_threshold = np.where(samples > SILENCE_THRESHOLD)[0]

    # Get start and end points of speech (in milliseconds)
    start = above_threshold[0] * 1000 / audio.frame_rate
    end = above_threshold[-1] * 1000 / audio.frame_rate

    # Slice audio to keep only the speech
    speech_audio = audio[start:end]

    # Save the speech to a new .wav file
    speech_audio.export(f'audios/clean_audio{audio_number}.wav')"""
