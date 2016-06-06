from audio_preprocessing.pipeline import AudioPipeline
from conv_autoencoder import ConvAutoencoder

myAudios = AudioPipeline()
# load 2 audio files
myAudios.load_data(1)
myAudios.down_sampling()
audio_data = next(myAudios.next_sample('sampled'))
x_data = audio_data.normalized_signal_matrix


train_audio = x_data[:800, :]
test_audio = x_data[800:, :]

auto = ConvAutoencoder(train_audio, test_audio)

auto.train(10, 100, True)
