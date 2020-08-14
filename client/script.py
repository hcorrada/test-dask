import os
import socket
from dask.distributed import Client

dask_scheduler_host = os.getenv("DASK_SCHEDULER_HOST")
dask_scheduler_port = os.getenv("DASK_SCHEDULER_PORT")
dask_scheduler = "{}:{}".format(dask_scheduler_host, dask_scheduler_port)

print("Connecting with socket")
s = socket.socket()
try: 
    s.connect((dask_scheduler_host, int(dask_scheduler_port)))
except Exception as e:
    print("something's wrong with {} {}".format(dask_scheduler, e))
finally:
    print(s)
    s.close()

print("Connected with socket")

print("Connecting with dask client")
cl = Client(dask_scheduler)
print(cl)
