from .local_settings import *
if DEBUG != True:
    from .production_settings import *
