model_backend = 'sqlite3'

if model_backend == 'sqlite3':
    from .model_sqlite3 import model
else:
    raise ValueError("Not the right database")

appmodel = model()

def get_model():
    return appmodel
