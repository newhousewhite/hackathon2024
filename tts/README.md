 ## TTS server

 Based on Coqui XTTS server. The default server doesn't support conditionining on speaker wav so I built another image based on it as follows:

### Building container
 ```bash
 docker build -f Dockerfile -t xtts:0.0.1 .
 ```

### Run container
```bash
docker run --rm -ti \
    --name tts-server \
    --privileged \
    -v $PWD/../yeonmi/segments:/data/wavs \
    -v $PWD:/app \
    -v $PWD/models:/root/.local/share/tts \
    -p 5000:5000 \
      xtts:0.0.1
```

This script is also found in `run.sh`.

This script mounts the following:
- The flask script `app.py` for easy edits
- The external reference wavs to condition the voice on.
- The tts model folder to persist on drive, so that no re-downloads happen.