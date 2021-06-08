import atexit
import docker
import os
import json
import subprocess

config_data = {}
command_template = \
    "docker run --name {} --gpus all -d {} --algo {} --proto {} --server {} --user {}"

__version__ = "0.0.1"
__author__ = 'Entropy Xu'
__credits__ = 'Duke University'

enable = False

CONFIG_TEMPLATE = """
{
  "MINING_CONTROL_ENABLE": "FALSE",
  "DOCKER_IMAGE": "dockminer/gminer:latest",
  "DOCKER_NAME": "eth_mine",
  "SERVER": "daggerhashimoto.eu.nicehash.com:3353",
  "PROTOCOL": "stratum",
  "USER": "38N79xmrAhMhHuxSLSJpFZm6BXEsL4Tg4q",
  "MINER_NAME": "nvdocker",
  "ALGORITHM": "ethash",
  "QUIET": "FALSE"
}
"""


def exit_callback():
    command = command_template.format(config_data["DOCKER_NAME"],
                                      config_data["DOCKER_IMAGE"],
                                      config_data["ALGORITHM"],
                                      config_data["PROTOCOL"],
                                      config_data['SERVER'],
                                      config_data['USER'] + "." + config_data["MINER_NAME"])
    # print(command.split(" "))
    if config_data["QUIET"] == "TRUE":
        subprocess.run(command, shell=True, check=True, stdout=subprocess.DEVNULL)
    else:
        subprocess.run(command, shell=True, check=True)


config_dir = os.path.dirname(__file__)
config_filename = os.path.join(config_dir, 'mining_control_config.json')

# print(config_filename)


if not os.path.isfile(config_filename):
    # Create config file
    print("Creating Config File at: ", config_filename)
    config_file = open(config_filename, "w")
    config_file.write(CONFIG_TEMPLATE)
    config_file.close()

config_data = json.loads(open(config_filename, "r").read())

# Exit if disabled by config
if "MINING_CONTROL_ENABLE" in config_data.keys():
    if config_data['MINING_CONTROL_ENABLE'] == "TRUE":
        enable = True

if enable:
    client = docker.from_env()

    # Kill the target container first
    containers = client.containers.list(all=True)
    for c in containers:
        if c.attrs["Name"][1:] == config_data["DOCKER_NAME"]:
            c.kill()
            c.remove()

    atexit.register(exit_callback)
else:
    if config_data["QUIET"] == "FALSE":
        print("Mining Control is Disabled")
