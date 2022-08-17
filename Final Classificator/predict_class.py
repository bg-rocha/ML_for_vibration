import pandas as pd
import numpy as np
import pickle
from scipy import signal, fft

def to_fft(y):
  return np.abs(fft.fft(y))[0:y.shape[0]//2] / (y.shape[0]//2)

def find_rotation(sinal,fs, h=0.05):
  return signal.find_peaks(to_fft(sinal.values),height=h)[0][0]/ (sinal.shape[0]/fs)  

  #--------------Stats from time domain-------------------
def pico(x):
  return np.max(abs(x))
def rms(x):
  return np.sqrt(np.mean(x**2))
def crista(x):
  return pico(x)/rms(x)
def curtose(x):
  a = 1/x.shape[0] * np.sum((x-np.mean(x))**4)
  b = (1/x.shape[0] * np.sum((x-np.mean(x))**2))**2
  return a/b
#------------------------------------------------------

#Peaks in FFT
def get_peaks(fft, freqs, rot, fs, delta=3):
  values = []
  xvar = (fs//2)/fft.shape[0]
  ref = (np.array(freqs)*rot/xvar).astype(int)
  for freq in ref:
    values.append(np.max(fft[freq-delta:freq+delta+1]))
  return values

class predictUnbalance():

    def __init__(self, df, fs, rot):
        self.df = df.iloc[:,:2].copy()
        self.fs = fs # em Hz
        with open('models/rfc_experimento.sav', 'rb') as f:
            self.model = pickle.load(f)
        if fs >= 5000:
            self.sos = signal.butter(N=10, Wn=[10,5000], btype='bandpass', fs=fs, output='sos')
        else:
            self.sos = signal.butter(N=10, Wn=10, btype='highpass', fs=fs, output='sos')
        
        for col in self.df.columns:
            self.df[col]= signal.sosfilt(self.sos, self.df[col].astype('float'))
        
        self.features =[[]]
        self.features[0].append(rot)
        for col in self.df.columns:
            rms1=rms(self.df[col])
            self.features[0].append(crista(self.df[col]))
            self.features[0].append(curtose(self.df[col]))
            for peak in get_peaks(to_fft(self.df[col].values),[1,2],rot, fs,2):
                self.features[0].append(peak/rms1)

    def predict(self):
        predict = pd.DataFrame(self.features, columns=['rotation', 'X_crista','X_curtose', 'X_1x', 'X_2x', 'Y_crista','Y_curtose', 'Y_1x', 'Y_2x'])
        feats = ['rotation','X_crista','X_1x', 'X_2x','Y_crista','Y_1x', 'Y_2x',  'X_curtose', 'Y_curtose' ]
        return self.model.predict(predict[feats])
    def print_predict(self):
        print(['Normal', 'Desbalanceado'][self.predict()[0]])


        

        
