import subprocess
import time

class Batcher():
  def __init__(self, stages, delay=1):
    self.stages = stages
    self.delay = delay
    self.processes = []

  def run(self):
    for stage in self.stages:
      for command in stage:
        #run command
        self.processes.append(subprocess.Popen(command))
        #wait for a bit
        time.sleep(self.delay)
      #wait for stage to complete
      self.wait_for_all()

  def wait_for_all(self):
    while len(self.processes) > 0:
      #if first process is closed
      if self.processes[0].poll() is not None:
        #remove
        self.processes.pop(0)
      #otherwise wait a bit
      else:
        time.sleep(self.delay)
