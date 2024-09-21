docker run --rm -ti \
    --name tts-server \
    --privileged \
    -v $PWD/../yeonmi/segments:/data/wavs \
    -v $PWD:/app \
    -v $PWD/models:/root/.local/share/tts \
    -p 5000:5000 \
    xtts:0.0.1