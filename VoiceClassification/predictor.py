import os
import pickle
from recorder import WaveRecorder
import soundfile as sf
import numpy as np

rec = WaveRecorder()

clf = pickle.load(open('VoiceClassification/model/several_model_add_none_class.sav','rb'))

yesno = ['No','Yes','None','Clap']

def predict():
    rec.record('output.wav')
    wav, _ = sf.read('output.wav')
    wav = np.array(wav[:, 0])
    wf = np.fft.fft(wav)
    wav = np.hstack((wf.real**2 + wf.imag**2, np.arctan2(wf.real, wf.imag)))
    pred = clf.predict(np.array([wav]))
    print("result:",yesno[int(pred)])
    return yesno[int(pred)]

if __name__ == "__main__":
    while True:
        result = predict()
        with open("VoiceClassification/result.txt", mode='w') as f:
            f.write(result)
