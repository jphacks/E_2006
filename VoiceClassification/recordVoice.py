import sys
import pyaudio
import wave
import recorder


cnt = 0
print('input prefix of output filename:')
fname = input()
print('input number to start with:')
cnt = int(input())
rec = recorder.WaveRecorder()
while True:
    print(cnt)
    rec.record('data/{}_{}.wav'.format(fname, cnt))
    cnt += 1
