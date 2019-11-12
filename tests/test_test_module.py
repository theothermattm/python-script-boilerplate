from unittest import mock
from unittest import TestCase
from unittest.mock import Mock
from unittest.mock import patch
from main.test_module import make_a_request
import json

# bottom up order for mocks and injection!
@mock.patch('main.test_module.requests', autospec=True)
class TestTestModule(TestCase):
  '''
  Replace me with some real tests!
  '''

  def test_request_something(self, mock_requests):
    mock_response = Mock()
    mock_response.json.return_value = {"results": [ { "sender" : { "senderorganization" : "test123"}}]}
    mock_requests.get.return_value = mock_response
    response = make_a_request()
    assert response["results"][0]["sender"]["senderorganization"] == "test123"


