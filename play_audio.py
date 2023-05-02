import wave
import pyaudio
def play_audio(audio_file):
    # Open the audio file
    file = wave.open(audio_file, 'rb')

    # Initialize PyAudio
    p = pyaudio.PyAudio()

    # Open a new stream for playing back the audio
    stream = p.open(format=p.get_format_from_width(file.getsampwidth()),
                    channels=file.getnchannels(),
                    rate=file.getframerate(),
                    output=True)

    # Read data from the audio file and play it back in the stream
    data = file.readframes(1024)
    while data:
        stream.write(data)
        data = file.readframes(1024)

    # Close the stream and PyAudio
    stream.stop_stream()
    stream.close()
    p.terminate()

# play_audio("mic_start.wav")
