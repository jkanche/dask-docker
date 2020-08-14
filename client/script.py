import os
from dask.distributed import Client

dask_scheduler = os.getenv("DASK_SCHEDULER_ADDRESS")
print(dask_scheduler)
print("#################")
cl = Client()
print(cl)
