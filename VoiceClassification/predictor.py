import pickle
import recorder
import soundfile as sf
import numpy as np

rec = recorder.WaveRecorder()

clf = pickle.load(open('model/yesno_model.sav','rb'))

yesno = ['No', 'Yes']

while True:
    # print('Press enter to start recording. Type end to finish recording.')
    # if input() == 'end':
    #     break

    rec.record('output.wav')
    wav, _ = sf.read('output.wav')
    wav = np.array(wav[:, 0])
    wf = np.fft.fft(wav)
    wav = np.hstack((wf.real**2 + wf.imag**2, np.arctan2(wf.real, wf.imag)))
    pred = clf.predict(np.array([wav]))
    print("result:",yesno[int(pred)])