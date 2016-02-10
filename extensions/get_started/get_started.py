#-*- coding:utf-8 -*-

"""
This file is part of OpenSesame.

OpenSesame is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

OpenSesame is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with OpenSesame.  If not, see <http://www.gnu.org/licenses/>.
"""

from libopensesame.py3compat import *
import os
import sys
from libopensesame import misc, metadata
from libqtopensesame.extensions import base_extension
from libqtopensesame.misc.translate import translation_context
from libqtopensesame.misc import template_info
_ = translation_context(u'get_started', category=u'extension')

class get_started(base_extension):

	"""
	desc:
		Shows the get-started tab and opens an experiment on startup, if one was
		passed on the command line.
	"""

	def activate(self):

		"""
		desc:
			Is called when the extension is activated through the menu/ toolbar
			action.
		"""

		# Initialize templates
		templates = []
		for i, (path, desc) in enumerate(template_info.templates):
			try:
				path = self.experiment.resource(path)
			except:
				continue
			if not i:
				cls = u'green-button'
			else:
				cls = u'button'
			md = u'<a href="opensesame://%s" class="%s">%s</a><br />' \
				% (path, cls, desc)
			templates.append(md)
		# Initialize recent experiments
		if not self.main_window.recent_files:
			recent = []
			self.ui._label_recent.hide()
		else:
			recent = [_(u'Continue with a recent experiment:')+u'<br />']
			for i, path in enumerate(self.main_window.recent_files):
				if not i:
					cls = u'green-button'
				else:
					cls = u'button'
				md = u'<a href="opensesame://%s" class="%s">%s</a><br />' % \
					(path, cls, os.path.basename(path))
				recent.append(md)
		# Create markdown
		with open(self.ext_resource(u'get_started.md')) as fd:
			md = safe_decode(fd.read())
		md = md % {
			u'version' : metadata.__version__,
			u'codename' : metadata.codename,
			u'templates' : u'  \n'.join(templates),
			u'recent_experiments' : u'  \n'.join(recent)
			}
		self.tabwidget.open_markdown(md, title=_(u'Get started!'),
			icon=u'opensesame')

	def event_startup(self):

		"""
		desc:
			Called on startup.
		"""

		# Open an experiment if it has been specified as a command line argument
		# and suppress the new wizard in that case.
		if len(sys.argv) >= 2 and os.path.isfile(sys.argv[1]):
			path = safe_decode(sys.argv[1], enc=misc.filesystem_encoding(),
				errors=u'ignore')
			self.main_window.open_file(path=path)
			return
		self.activate()
