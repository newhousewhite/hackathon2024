docker run --rm -ti \
    --name response-rag-orchestration   \
    -p 5001:5001 \
    -e GOOGLE_API_KEY="..." \
    -e OPENAI_API_KEY="..." \
    -v $PWD:/app \
    -v $PWD/../transcription.txt:/data/transcription.txt \
    response-rag:latest