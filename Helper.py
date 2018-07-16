import os
from global_constants import DB_NAME

def doesDbExist():
    return os.path.exists(DB_NAME)