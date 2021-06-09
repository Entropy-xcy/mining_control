# Mining Control
Mining Control is a package that allows easy integration of cryptocurrency mining control in any deep-learning programs.

Mining Control does the following:
* Start all the cryptocurrency mining container when the deep-learning program launches.
* Restart the cryptocurrency mining container after the deep-learning program finishes.

By not letting the mining software and deep-learning program racing for GPU resources,
it avoids degraded performance as well as preventing the racing for VRAM.

# Installation
Requirements:
* Works only on Linux-based platforms
* Nvidia GPU Driver
* Docker and nvidia-docker
* Python 3.6+

```pip install mining_control```

# Usage
Simply 
```
import mining_control
``` 
at the beginning of your deep-learning program.
Please refer to `tests/example.py` for how to integrate mining_control into a PyTorch MNIST training program.

The first time you `import mining_control`, you will get the following output:
```
Creating Config File at: <mining_control_config_filepath>
Mining Control is Disabled
```
This is because the mining_control is disabled by default and it is needed to edit the config of it first.
<br>
Edit the config file at `<mining_control_config_filepath>` and set `MINING_CONTROL_ENABLE` to `TRUE`.
```json
{
  "MINING_CONTROL_ENABLE": "TRUE",
  "DOCKER_IMAGE": "dockminer/gminer:latest",
  "DOCKER_NAME": "eth_mine",
  "SERVER": "daggerhashimoto.eu.nicehash.com:3353",
  "PROTOCOL": "stratum",
  "USER": "38N79xmrAhMhHuxSLSJpFZm6BXEsL4Tg4q",
  "MINER_NAME": "nvdocker",
  "ALGORITHM": "ethash",
  "QUIET": "FALSE"
}
```
Then, restart the python script. You will notice a base64 string printed out when the python script exits.<br>

Such base64 is the id for the docker container created for mining.
