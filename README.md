# rl

## Install

```bash
Install AMD's ROCm
```

```bash
sudo apt-get update
sudo apt-get install -y python3-opengl ffmpeg xvfb
poetry install
```

Due to a bug in box2d-py, install `gymnasium[box2d]` with:

```bash
poetry shell
pip3 install gymnasium[box2d]
```