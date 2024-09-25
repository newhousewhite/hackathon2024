import os, glob
os.environ['OPENBLAS_NUM_THREADS'] = '1'


from flask import Flask, request, jsonify, send_file
import requests
from TTS.api import TTS
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=True)


ref_wavs = []
for f in glob.glob("/data/wavs/*.wav"):
    ref_wavs.append(f)
ref_wavs = ref_wavs[:5]

app = Flask(__name__)

@app.route('/tts', methods=['POST'])
def generate_tts():
    text = request.json['text']
    lang = request.json['lang']
    print(text, lang, flush=True)

    # generate speech by cloning a voice using default settings
    tts.tts_to_file(text=text,
                    file_path="output.wav",
                    speaker_wav=ref_wavs,
                    language=lang,
                    split_sentences=True
                    )
    no_error = True  #TODO check for this late
    # Return the WAV file as a response
    if no_error:
        return send_file("output.wav", mimetype="audio/wav")
    else:
        return jsonify({"error": "Error generating TTS"})

if __name__ == '__main__':
    app.run(debug=True)