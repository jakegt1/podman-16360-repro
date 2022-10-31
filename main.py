import os

from docker import APIClient

last_line = list(APIClient().build(os.getcwd()))[-1]

print(last_line)

assert "aux" not in last_line.decode("utf-8")
