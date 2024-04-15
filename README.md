# Speaker diarisation service

This repository contains a Speaker Diarisation Webservice powered by [pyannote](https://github.com/pyannote/pyannote-audio).
and [CLAM](https://proycon.github.io/clam/). This webservice is developed at the Centre of Language and Speech Technology, Radboud University, Nijmegen.

## Installation

For end-users and hosting partners, we provide a container image that ships with a web interface. 
You can pull a prebuilt image from the Docker Hub registry using docker as follows:

```
$ docker pull proycon/diarisationservice
```

Run the container as follows:

```
$ docker run -v /path/to/your/data:/data --env HF_TOKEN=$HF_TOKEN -p 8080:80 proycon/diarisationservice
```

Ensure that the directory you pass is writable. Replace `$HF_TOKEN` with your Huggingface token and accept the license agreements for the following models:
* <https://huggingface.co/pyannote/speaker-diarization-3.1>
* <https://huggingface.co/pyannote/segmentation-3.0>

Assuming you run locally, the web interface can then be accessed on ``http://127.0.0.1:8080/``.

If you want to deploy this service on your own infrastructure, you will want to set some of the environment variables
defined in the `Dockerfile` when running the container, most notably the ones regarding authentication, as this is by
default disabled and as such *NOT* suitable for production deployments.

