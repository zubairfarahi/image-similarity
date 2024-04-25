# image-similarity

[![pipeline status](https://git.ghpcard.local/dbelii/odapi-compare/badges/master/pipeline.svg)](https://git.ghpcard.local/dbelii/odapi-compare/-/commits/master)

<div style="text-align:center"><img src="docs/intro.jpg" /></div>

### Description

`image-similarity
` focuses on comparing two images and detecting similars.


#### SIFT Algorithm 

Learn more about SIFT Algorithm from this [source](https://pyimagesearch.com/2016/01/11/opencv-panorama-stitching/).

##### Parameters
- **RatioThreshold**: Ratio threshold for Lowe's ratio test. Default value is `0.60`.
- **MatchThreshold**: Minimum number of good matches required to consider images as matching.


### Dependencies
```
sudo apt-get update && apt-get install libmagic1 -y
```
### Getting Started

Run the application with:
```
CONFIG_FILE=configs/.i1.config.ini UVICORN_PORT=6000 UVICORN_HOST=0.0.0.0 uvicorn main:app
```
or
```
CONFIG_FILE=configs/.i1.config.ini python3 main.py
```

> Note: You can define environment variables with the prefix `UVICORN_` or you can set them in config file.


### Docker

To build and start the docker image use:

```
make up
```

> Note: If you want to start locally app in a docker instance, copy file from `docs/.env.example` to `.env` in main folder.

### Makefile

Use to remove dangling Docker images that are no longer needed:
```
make clean
``` 

Use to stop and then start the container, restarting any processes running inside it:
```
make restart
``` 

Use to check the code formatting:
```
make check
``` 

Use to format the code:
```
make format
``` 

Use to run the linter:
```
make lint
```


### External resources
🔸[Testing different image hash functions](https://content-blockchain.org/research/testing-different-image-hash-functions/)