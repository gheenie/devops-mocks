# Mocking and Patching

Some awful code here... The `numbers.py` file contains two classes, `NumberRequester` and `NumberCruncher`. The `NumberRequester` gets a random number fact from the `numbersapi` endpoint. It makes a careful note of the results of each request in a log and returns a dictionary with the number and its associated fact.

The `NumberCruncher` eats number facts, although it only has a limited capacity. When it is started you have to specify the size of its tummy (ie how many number facts it can store). It has a `NumberRequester` built in. To `crunch` a number, it gets the `NumberRequester` to get a number fact. It then does one of three things:
1. It hates odd numbers, so if the numebr is odd, it just rejects it with a "Yuk!" message.
1. If the number is even, and its tummy is not full, it happily eats the number fact and returns a "Yum!" message.
1. If the number is even an its tummy is full, it expels one number fact at random from its tummy to make room for the new one. It returns a "Burp!" message.

If we start a REPL, we should be able to do something like this:
```python
>>> from numbers import NumberCruncher
>>> nc = NumberCruncher(3) # a NumberCruncher that can store 3 facts
>>> nc.crunch()
'Yum! 8100'   # stored
>>> nc.crunch()
'Yuk! 5335'
>>> nc.crunch()
'Yuk! 5565'
>>> nc.crunch()
'Yum! 730'  # stored
>>> nc.tummy
[{'number': 8100, 'fact': '8100 is divisible by its reverse.'}, {'number': 730, 'fact': '730 is the number of connected bipartite graphs with 9 vertices.'}]
>>> nc.crunch()
'Yuk! 9267'
>>> nc.crunch()
'Yum! 436'  # stored - tummy full
>>> nc.crunch()
'Burp! 436' # 436 burped out to make room for the new fact
>>> nc.tummy
[{'number': 8100, 'fact': '8100 is divisible by its reverse.'}, {'number': 730, 'fact': '730 is the number of connected bipartite graphs with 9 vertices.'}, {'number': 5624, 'fact': '5624 is the number of binary 5×5 matrices up to permutations of rows and columns.'}]
>>> nc.requester.log
[{'request_number': 1, 'call_time': '2022-11-09T16:38:23.417667', 'end_point': 'http://numbersapi.com/random/math', 'result': 'SUCCESS', 'number': 8100}, {'request_number': 2, 'call_time': '2022-11-09T16:38:26.111704', 'end_point': 'http://numbersapi.com/random/math', 'result': 'SUCCESS', 'number': 5335}, {'request_number': 3, 'call_time': '2022-11-09T16:38:31.689280', 'end_point': 'http://numbersapi.com/random/math', 'result': 'SUCCESS', 'number': 5565}, {'request_number': 4, 'call_time': '2022-11-09T16:38:37.810081', 'end_point': 'http://numbersapi.com/random/math', 'result': 'SUCCESS', 'number': 730}, {'request_number': 5, 'call_time': '2022-11-09T16:38:52.720854', 'end_point': 'http://numbersapi.com/random/math', 'result': 'SUCCESS', 'number': 9267}, {'request_number': 6, 'call_time': '2022-11-09T16:38:55.040040', 'end_point': 'http://numbersapi.com/random/math', 'result': 'SUCCESS', 'number': 436}, {'request_number': 7, 'call_time': '2022-11-09T16:39:07.712827', 'end_point': 'http://numbersapi.com/random/math', 'result': 'SUCCESS', 'number': 5624}]
```

So this works but - shock!!! - it has no unit tests!!! This is, of course, unacceptable. Your task is to write some. A test suite has been prepared with some specifications for behaviour we want to test for. However, they have not been implemented. You should implement these tests, making use of Mocks and patches where necessary. The code as written should pass the required tests. But if you complete those tests, feel free to write new ones making more rigorous checks on `NumberCruncher` and `NumberRequester` behaviour.