import wave
import numpy as np
import matplotlib.pyplot as plt


def main():

    wav_file = '../data/wav/BASIC5000_0001.wav'
    out_plot = './plot.png'

    # wavファイルを開き、以降の処理を行う
    with wave.open(wav_file) as wav:
        # サンプリング周波数 [Hz] を取得
        sampling_frequency = wav.getframerate()

        # サンプルサイズ [Byte] を取得
        sample_size = wav.getsampwidth()

        # チャネル数を取得
        num_channels = wav.getnchannels()

        # wavデータのサンプル数を取得
        num_samples = wav.getnframes()

        # wavデータを読み込む
        waveform = wav.readframes(num_samples)

        # 読み込んだデータはバイナリ値(16bit integer)
        # なので，数値(整数)に変換する
        waveform = np.frombuffer(waveform, dtype=np.int16)

    print("Sampling Frequency: %d [Hz]" % sampling_frequency)
    print("Sample Size: %d [Byte]" % sample_size)
    print("Number of Channels: %d" % num_channels)
    print("Number of Samples: %d" % num_samples)
    
    # 横軸(時間軸)を作成する
    time_axis = np.arange(num_samples) / sampling_frequency

    # プロットの描画領域を作成
    plt.figure(figsize=(10,4))
    plt.plot(time_axis, waveform)

    plt.xlabel("Time [sec]")
    plt.ylabel("Value")

    plt.xlim([0, num_samples / sampling_frequency])
    plt.savefig(out_plot)


if __name__ == "__main__":
    main()