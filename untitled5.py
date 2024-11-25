# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Olr_5LdlyZVU_Hsb3zgi1F0Bx65AdvDQ
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

def generate_spectrogram(wav_file):
    # Read the WAV file
    sample_rate, data = wavfile.read(wav_file)

    # Check if data is stereo or mono
    if len(data.shape) > 1:
        data = data[:, 0]  # Use one channel if stereo

    # Create a spectrogram
    plt.figure(figsize=(12, 6))
    plt.specgram(data, Fs=sample_rate, NFFT=1024, noverlap=512, cmap='inferno')

    plt.title(f'Spectrogram of {wav_file}')
    plt.xlabel('Time (s)')
    plt.ylabel('Frequency (Hz)')
    plt.colorbar(label='Intensity (dB)')
    plt.xlim(0, len(data) / sample_rate)  # Set x-axis limit
    plt.ylim(0, sample_rate / 2)           # Frequency range from 0 to Nyquist frequency
    plt.grid(True)
    plt.show()

# Example usage
wav_file_path = 'ahem_x.wav'  # Replace with your WAV file path
generate_spectrogram(wav_file_path)

from gtts import gTTS
import os

# Matnni belgilash
text = """odamlar nima deydi?
os.O_ACCMODEzingni bosvol, hammaga oxsha
Yigishtir! Qanaqa muzika? Qanaqa sanat?
Muhimroq hammadan o'qishing
odamlar nima deydi?
Katta bopqoldingku! Qachonga to'y endi?
Qanaqa ishmi? Karyerangni qo'y endi
Shu yoshdayam endi qanaqa o'yin bu, ey?
Yig'ishtir tepishni koptok!
Qanaqa futbalistmi? Ishingni top kel!
Qanaqa qutilari? Qanaqa kurash?
Shunchasi chempion bo'pqoptimi?
odamlar nima deydi?
Bu yil ham bolasi o'qishdan qoptimi?
Senga shuncha umrimni yo'qotib
Natijasiga men shuni topdimmi?
odamlar nima deydi?
Indama, gapirma, ko'tarma boshni
Qattan bo'sayam topish kere to'yga
Nima deydi qo'ni-qo'shni? Zo'r qil oshni!
odamlar nima deydi?
Tengdoshmi? Kelin qimiman sinfdoshni!
odamlar nima deydi?
Qilma ko'z yoshlar, qizim joyingda qolgin toshday """

# Ovoz yaratish (gTTS - Google Text-to-Speech)
language = 'en'  # Changed to English ('en')
tts = gTTS(text=text, lang=language, slow=False)

# Ovoz faylini saqlash
audio_file = "output.mp3"
tts.save(audio_file)

# Ovoz faylini tinglash (Google Colab-da)
from IPython.display import Audio
Audio(audio_file)