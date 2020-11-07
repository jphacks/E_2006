import numpy as np
import soundfile as sf
import pyaudio
import wave
import recorder

from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split, cross_val_score
