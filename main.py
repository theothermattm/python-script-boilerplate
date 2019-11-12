# entrypoint file, calls the main module via command line
import logging
from main.test_module import make_a_request

log = logging.getLogger(__name__)
log.setLevel('INFO')

if __name__ == '__main__':
  logging.basicConfig(level=logging.WARN)
  response = make_a_request()
  log.info(f'The response: {response}')
  log.info(f'The sender: {response["results"][0]["sender"]["senderorganization"]}')
