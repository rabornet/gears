import logging
logging.info('###~###~###~###~###~###~###~###~###~###~###~###~###~###~###~###~###~')
logging.info('###~###~###~###~###~###~###~###~###~###~###~###~###~###~###~###~###~')
logging.info('###~###~###~###~###~###~###~###~###~###~###~###~###~###~###~###~###~')

from client import ui_handler
import webapp2

app = webapp2.WSGIApplication([
  ('/'          , ui_handler.DefaultPage),
  ('/_ah/start' , ui_handler.StartPage),
  ('/_ah/warmup', ui_handler.WarmUpPage),
  ('(.*)'       , ui_handler.ErrorPage)
  ],
  config = {
    'webapp2_extras.sessions':{
      'secret_key':'074052db3457f798fc9a29b8d80ba42c8b27af307cad48bc245f344094f4fc94',
    } # http://webapp-improved.appspot.com/api/webapp2_extras/sessions.html
  },
  debug = True)