FROM ghcr.io/coqui-ai/tts:latest

# Add Tini
ENV TINI_VERSION v0.19.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
RUN chmod +x /tini
ENTRYPOINT ["/tini", "--"]

WORKDIR /app

ADD req.txt req.txt

RUN pip install -r req.txt

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]