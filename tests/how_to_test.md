# Unittest and Unit testing

## Notes on tests

With the completion of the max-move branch tests in the test_menu.py associated
with menu.py are failing to import the function being tested.<br>

Testing in the test_pgn_parsers file are failing with the error importing
pgn_parser as pgnp dealing with the set max moves variable in the regex_dict['max_move']
key value pair.<br>

Check testing with VsCode and PyCharm.<br>

## Ways to Run Tests

```
$ python3 -m unittest
```

or<br>

```
$ python3 -m unittest discover -v
```

or<br>

```
$ python3 -m unittest tests.test_parser -v
```

or<br>

```
$ python3 -m unittest tests.test_parser.TestGamesLists -v
```

or<br>

```
$ python3 -m unittest tests.test_parser.TestGamesLists.test_get_only_games -v
```
