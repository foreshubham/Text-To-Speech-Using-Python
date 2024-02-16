from gtts import gTTS
import os

def text_to_speech(text, language='en', output_file='output.mp3'):
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save(output_file)
    os.system(f'start {output_file}')  # This opens the generated audio file

# Example usage
text = """
Programming languages are crucial for developing software for embedded systems and Internet of Things (IoT) devices.
C and C++ are commonly used for programming microcontrollers and embedded systems due to their efficiency and low-level capabilities.
IoT devices rely on programming languages to control sensors, process data, and communicate with other devices over networks.
"""

text_to_speech(text, language='en', output_file='output.mp3')
