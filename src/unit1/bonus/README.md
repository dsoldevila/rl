Download and unzip https://drive.google.com/uc?export=download&id=1zv3M95ZJTWHUVOWT6ckq_cm98nft8gdF to trained-envs-esxecutables/linux/Huggy

```bash
cd src/unit1/bonus
poetry run mlagents-learn ./ml-agents/config/ppo/Huggy.yaml --env=./trained-envs-executables/linux/Huggy/Huggy --run-id="Hug
gy" --no-graphics
```