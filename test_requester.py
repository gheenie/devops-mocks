from unittest.mock import Mock
from cruncher import NumberRequester
from unittest.mock import patch
import datetime


def test_number_requester_returns_a_valid_result_when_called():
    """Test that the call method returns a valid item.
    
    Given:
         A NumberRequester instance making a successful call

    Result:
        A result as a dict in the form {'result': 'SUCCESS', 'number': 13, "fact": "13 is lucky for some."}

    """
    
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.text = '13 is lucky for some.'

    # Doesn't need to be inside with block.
    number_requester = NumberRequester()

    with patch('cruncher.requests.get', return_value=mock_response):
        assert number_requester.call() == {
            'result': 'SUCCESS', 
            'number': 13, 
            "fact": "13 is lucky for some."
        }


def test_number_requester_returns_a_valid_result_when_called__using_MagicMock():
    with patch('cruncher.requests.get') as magicmock_requests_get:
        magicmock_response = magicmock_requests_get.return_value
        magicmock_response.status_code = 200
        magicmock_response.text = '13 is lucky for some.'

        number_requester = NumberRequester()

        assert number_requester.call() == {
            'result': 'SUCCESS', 
            'number': 13, 
            "fact": "13 is lucky for some."
        }


@patch('cruncher.requests.get')
def test_number_requester_returns_error_result_for_non_200_response(magicmock_requests_get):
    """Test that the call method returns a valid item when a request fails.
    
    Given:
         A NumberRequester instance making an unsuccessful call

    Result:
        A result as a dict in the form {'result': 'FAILURE', 'error_code': 404}
    
    """
    
    magicmock_response = magicmock_requests_get.return_value
    magicmock_response.status_code = 404

    number_requester = NumberRequester()

    assert number_requester.call() == {
        'result': 'FAILURE', 
        'error_code': 404
    }


@patch('cruncher.requests.get')
def test_number_requester_keeps_log_of_requests(magicmock_requests_get):
    """Test that a NumberRequester instance keeps a log of its own requests.

    Given:
        A NumberRequester is instantiated.
        The NumberRequester.call method is called 5 times at known times.

    Result:
        The NumberRequester.log attribute returns a array of five valid results. Each result
        is a serialisable dict in the form:
        {'request_number': 1, 'call_time': '2022-11-09T16:38:23.417667', 'end_point': 'http://numbersapi.com/random/math',
        'result': 'SUCCESS', 'number': 49}
    Ensure that you test that each dict is exactly correct - including the 'call_time'.
    """
    
    magicmock_response = magicmock_requests_get.return_value
    magicmock_response.status_code = 200
    magicmock_response.text = '23 random fact'

    with patch('cruncher.dt') as magicmock_dt:
        mock_isoformat = Mock()
        mock_isoformat.isoformat = lambda: datetime.date(2019, 3, 15)
        magicmock_dt.now.return_value = mock_isoformat

        number_requester = NumberRequester()
        number_requester.call()
        number_requester.call()
        number_requester.call()
        number_requester.call()
        number_requester.call()

        # need to check for len() == 0
        for i, each_log in enumerate(number_requester.log):
            assert each_log == {
                'request_number': i + 1, 
                'call_time': datetime.date(2019, 3, 15), 
                'end_point': 'http://numbersapi.com/random/math',
                'result': 'SUCCESS', 
                'number': 23
            }
