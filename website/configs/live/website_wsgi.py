import os
import site
import sys

prev_sys_path = list(sys.path) 

site.addsitedir(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))
site.addsitedir(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
site.addsitedir(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../apps/')))

import ext

# Reorder sys.path so new directories at the front.
new_sys_path = [] 
for item in list(sys.path): 
    if item not in prev_sys_path: 
        new_sys_path.append(item) 
        sys.path.remove(item) 
sys.path[:0] = new_sys_path

os.environ["DJANGO_SETTINGS_MODULE"] = "website.configs.live.settings"
 
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
