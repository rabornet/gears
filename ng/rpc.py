""" RaborNet Gears
"""
from google.appengine.ext.webapp import template
import logging, os, webapp2


class BasePage(webapp2.RequestHandler):
  def __init__(self, request=None, response=None):
    super(BasePage, self).__init__(request, response)

  def get(self, path=None):
    if path:
      template_path = os.path.abspath(os.path.join(os.path.dirname(__file__), path))
      logging.info('#####{}'.format(template_path))
      self.response.out.write(template.render(template_path=template_path, template_dict={}))
    else:
      self.response.out.write('PATH NOT FOUND')


class GearsPage(BasePage):
  def get(self):
    super(GearsPage, self).get(path='./sites/developer/dist/developer/index.html')


class PublicPage(BasePage):
  def get(self):
    super(PublicPage, self).get(path='./sites/public/dist/public/index.html')