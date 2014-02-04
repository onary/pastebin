from datetime import datetime, timedelta
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import utc

EXPIRATION_CHOICE = (
	('minutes=10', _('10 Minutes')),
	('hours=1', _('1 Hour')),
	('days=1', _('1 Day')),
	('weeks=1', _('1 Week')),
	('weeks=2', _('2 Weeks')),
	('days=30', _('1 Month (30 days)')),
	)

SYNTAX_CHOICE = (
	('plain', 'Plain'),
	('bash', 'Bash'),
	('c', 'C'),
	('css', 'CSS'),
	('diff', 'Diff'),
	('django', 'Django/Jinja'),
	('html', 'HTML'),
	('irc', 'IRC logs'),
	('js', 'JavaScript'),
	('perl', 'Perl'),
	('php', 'PHP'),
	('pycon', 'Python console session'),
	('pytb', 'Python Traceback'),
	('python', 'Python'),
	('python3', 'Python 3'),
	('sql', 'SQL'),
	('text', 'Text only'),
	)

class Paste(models.Model):
	code = models.TextField(_('Code'))
	title = models.CharField(_('Title'), blank=False, max_length=255)
	created = models.DateTimeField(_('Created'), auto_now_add=True)
	expiration = models.DateTimeField(_('Expiration'))

	syntax = models.CharField(
		_('Syntax'),
		max_length=255,
		choices=SYNTAX_CHOICE,
		default='plain'
		)

	expiration_choice = models.CharField(
		_('Expiration date'),
		max_length=255,
		choices=EXPIRATION_CHOICE,
		default='weeks=1'
		)

	def save(self, **kwargs):
		if not self.expiration:
			k, v = self.expiration_choice.split('=')
			self.expiration = datetime.utcnow().replace(tzinfo=utc) + timedelta(**{k: int(v)})
		super(Paste, self).save(**kwargs)

	def __unicode__(self):
		return u'#%s - %s' % (self.pk, self.title)

	@models.permalink
	def get_absolute_url(self):
		return 'paste', (self.id,)