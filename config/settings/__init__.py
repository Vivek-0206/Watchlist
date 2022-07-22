import os
if 'ENVIRONMENT' in os.environ and os.environ['ENVIRONMENT'] == 'production':
    from .production_settings import *
else:
    from .local_settings import *
