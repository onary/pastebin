from datetime import datetime
import logging
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
    "../../"))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
    "../"))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

from django.conf import settings
from paste.models import Paste

logger = logging.getLogger('cron')

p = Paste.objects.filter(expiration__lte=datetime.utcnow().replace(tzinfo=utc))
if p:
	logger.warning(':WARNING: cron working')
	logger.warning(':Deleting Paste items: %s' % p.count())
	p.delete()