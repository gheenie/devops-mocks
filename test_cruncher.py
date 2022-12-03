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


def test_number_cruncher_discards_oldest_item_when_tummy_full():
    """Test that the crunch method maintains a maximum number of facts.
    
    Given:
         A Number cruncher instance with tummy size 3 having 3 items in tummy getting 
         an even result for its "crunch" method, eg 24.

    Result:
        Method deletes oldest result from tummy (eg 42)
        Method returns "Burp! 42"
        The tummy attribute contains 24 but not 42.
    
    """
    pass

def test_number_cruncher_raises_runtime_error_if_invalid_number_request():
    """Test that there is a runtime error if NumberRequester response is
        invalid

        Given:
            A NumberCruncher instance, receiving an invalid NumberRequester
            response (eg an AttributeError)

        Result: 
            Raises RuntimeError
    """
    pass