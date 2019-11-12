import logging
import requests

log = logging.getLogger(__name__)

def make_a_request():
  '''
  Make a request to something.  Really, just replace me with a real module
  '''
  log.info('Doing something fake, going out to an API to fetch some data!')
  response = requests.get('https://api.fda.gov/drug/event.json?limit=1')
  return response.json()

