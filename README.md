# ZBatcher

Runs multiple commands in parallel. Commands are split up into stages. ZBatcher
will wait for all commands within a stage to finish before progressing to the next stage.

```python
from zbatcher import Batcher

Batcher([
  #first stage -- a single command
  ['python scripts/builder.py -i 8 -o 4 -s 64 -a relu -A softmax -f models/slp/1.h5'],
  #second stage -- all commands will be run in parallel with a default 1s delay
  [
    'python scripts/run_reward_proxy.py -u http://localhost:8001 -p 8002 -s -0.1',
    'python scripts/run_env.py -u http://localhost:8001 -x http://localhost:8001 -p 8000 -s -0.1 -n simple_lunar_proxy -e "LunarLander-v2"',
    'python scripts/run_pget.py -u http://localhost:8000 -p 8001 -m models/slp/1.h5 -d True -s -0.1 -n 0.01 -a 1e-3'
  ]
]).run()
```
