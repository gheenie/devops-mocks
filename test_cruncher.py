def test_number_cruncher_likes_even_numbers():
    """Test that the crunch method saves number facts for even numbers.
    
    Given:
         A Number cruncher instance getting an even result for its "crunch" method (eg 42)

    Result:
        Method returns "Yum! 42"
        The tummy attribute contains a dict such as {'number': 42, "fact": "42 is the meaning of life."}
    
    """
    pass


def test_number_cruncher_hates_odd_numbers():
    """Test that the crunch method rejects number facts for odd numbers.
    
    Given:
         A Number cruncher instance getting an odd result for its "crunch" method eg 13

    Result:
        Method returns "Yuk! 13"
        The tummy attribute is unchanged.
    
    """
    pass


def test_number_cruncher_discards_random_item_when_tummy_full():
    """Test that the crunch method maintains a maximum number of facts.
    
    Given:
         A Number cruncher instance with tummy size 3 having 3 items in tummy getting 
         an even result for its "crunch" method, eg 24.

    Result:
        Method deletes one result from tummy (eg 42)
        Method returns "Burp! 42"
        The tummy attribute contains 24 but not 42.
    
    """
    pass

def test_number_requester_returns_a_valid_result_when_called():
    """Test that the call method returns a valid item.
    
    Given:
         A NumberRequester instance making a successful call

    Result:
        A result as a dict in the form {'result': 'SUCCESS', 'number': 13, "fact": "13 is lucky for some."}

    """
    pass


def test_number_requester_returns_error_result_for_non_200_response():
    """Test that the call method returns a valid item when a request fails.
    
    Given:
         A NumberRequester instance making an unsuccessful call

    Result:
        A result as a dict in the form {'result': 'FAILURE', 'error_code': 404}
    
    """
    pass


def test_number_requester_keeps_log_of_requests():
    """Test that a NumberRequester instance keeps a log of its own requests.

    Given:
        A NumberRequester is instantiated.
        The NumberRequester.request method is called 5 times at known times.

    Result:
        The NumberRequester.log attribute returns a array of five valid results. Each result
        is a serialisable dict in the form:
        {'request_number': 1, 'call_time': '2022-11-09T16:38:23.417667', 'end_point': 'http://numbersapi.com/random/math',
        'result': 'SUCCESS', 'number': 49}
    Ensure that you test that each dict is exactly correct - including the 'call_time'.
    """
    pass
