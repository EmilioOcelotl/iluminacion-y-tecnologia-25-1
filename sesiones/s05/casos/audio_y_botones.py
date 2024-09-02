import board
import digitalio
from audiocore import WaveFile
from audioio import AudioOut

# Habilitar el altavoz
spkrenable = digitalio.DigitalInOut(board.SPEAKER_ENABLE)
spkrenable.direction = digitalio.Direction.OUTPUT
spkrenable.value = True

# Configurar los botones
buttonA = digitalio.DigitalInOut(board.BUTTON_A)
buttonA.direction = digitalio.Direction.INPUT
buttonA.pull = digitalio.Pull.DOWN

buttonB = digitalio.DigitalInOut(board.BUTTON_B)
buttonB.direction = digitalio.Direction.INPUT
buttonB.pull = digitalio.Pull.DOWN

# Archivos de audio asignados a los botones A y B
audiofiles = ["/1.wav", "/2.wav"]

def play_file(filename):
    print("Reproduciendo archivo: " + filename)
    try:
        with open(filename, "rb") as wave_file:
            wave = WaveFile(wave_file)
            audio = AudioOut(board.SPEAKER)
            audio.play(wave)
            while audio.playing:
                pass
    except Exception as e:
        print(f"Error al reproducir el archivo {filename}: {e}")

while True:
    if buttonA.value:  # Si se presiona el botón A
        play_file(audiofiles[0])
    if buttonB.value:  # Si se presiona el botón B
        play_file(audiofiles[1])
