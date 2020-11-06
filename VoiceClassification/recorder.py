import pyaudio
import wave


class WaveRecorder():

    def __init__(self, chunc=1024, fmt=pyaudio.paInt16, channels=2, rate=44100, record_sec=2):
        self.CHUNK = chunc
        self.FORMAT = fmt
        self.CHANNELS = channels
        self.RATE = rate
        self.RECORD_SECONDS = record_sec

    def record(self, fname):
        p = pyaudio.PyAudio()
        stream = p.open(format=self.FORMAT,
                        channels=self.CHANNELS,
                        rate=self.RATE,
                        input=True,
                        frames_per_buffer=self.CHUNK)

        print("* recording")

        frames = []

        for i in range(0, int(self.RATE / self.CHUNK * self.RECORD_SECONDS)):
            data = stream.read(self.CHUNK)
            frames.append(data)

        print("* done recording")
        stream.stop_stream()
        stream.close()
        p.terminate()

        with wave.open(fname, 'wb') as f:
            f.setnchannels(self.CHANNELS)
            f.setsampwidth(p.get_sample_size(self.FORMAT))
            f.setframerate(self.RATE)
            f.writeframes(b''.join(frames))