docker run --rm -ti \
    --name tts-server \
    --gpus all \
    -v $PWD/../segments/SPEAKER_01:/data/wavs \
    -v $PWD/app.py:/app/app.py \
    -v $PWD/models:/root/.local/share/tts \
    -p 5000:5000 \
    xtts:0.0.1