from configs.settings import *

ALLOWED_HOSTS = [
    '.spacelog.org',
]

# The following MUST be an absolute URL in live deploys (it's given out
# to other systems).
STATIC_URL = 'http://cdn.spacelog.org/assets/website/'
MISSIONS_IMAGE_URL = 'http://media.spacelog.org/'

# allow local overrides, probably built during deploy
try:
    from local_settings import *
except ImportError:
    pass
