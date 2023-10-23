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

## Run

```bash
export HSA_OVERRIDE_GFX_VERSION=10.3.0 #solve segfault when reading GPU memory https://www.reddit.com/r/archlinux/comments/12ympb5/segfault_when_using_pytorch_with_rocm/
pytest -s
```