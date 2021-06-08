import atexit
import docker
import os
import json
import subprocess

config_data = {}
command_template = \
    "docker run --name {} --gpus all -d {} --algo {} --proto {} --server {} --user {}"


def exit_callback():
    command = command_template.format(config_data["DOCKER_NAME"],
                                      config_data["DOCKER_IMAGE"],
                                      config_data["ALGORITHM"],
                                      config_data["PROTOCOL"],
                                      config_data['SERVER'],
                                      config_data['USER'] + "." + config_data["MINER_NAME"])
    # print(command.split(" "))
    subprocess.run(command, shell=True, check=True)


config_filename = filename = os.path.join(os.path.dirname(__file__), 'mining_control_config.json')

try:
    config_data = json.loads(open(config_filename, "r").read())
except OSError as e:
    print("Mining Control not configured.")

# Exit if disabled by config
if config_data['MINING_CONTROL_ENABLE'] != "TRUE":
    exit()

client = docker.from_env()

# Kill the target container first
containers = client.containers.list(all=True)
for c in containers:
    if c.attrs["Name"][1:] == config_data["DOCKER_NAME"]:
        c.kill()
        c.remove()

atexit.register(exit_callback)
