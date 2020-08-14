import os
from dask.distributed import Client

dask_scheduler = os.getenv("DASK_SCHEDULER_ADDRESS")
cl = Client(dask_scheduler)
print(cl)
