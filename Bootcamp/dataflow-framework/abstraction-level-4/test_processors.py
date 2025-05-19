from processors import to_upper, LineCounter, JoinEveryNLines, SplitByDelimiter

def test_line_counter():
    lines = iter(["a", "b", "c"])
    lc = LineCounter()
    result = list(lc(lines))
    assert result == ["1: a", "2: b", "3: c"]

def test_join_every_n():
    lines = iter(["one", "two", "three"])
    joiner = JoinEveryNLines(2)
    result = list(joiner(lines))
    assert result == ["one | two", "three"]

def test_split_by_delim():
    lines = iter(["a|b|c"])
    splitter = SplitByDelimiter("|")
    result = list(splitter(lines))
    assert result == ["a", "b", "c"]

def test_upper():
    lines = iter(["hello", "world"])
    result = list(to_upper(lines))
    assert result == ["HELLO", "WORLD"]

if __name__ == "__main__":
    test_line_counter()
    test_join_every_n()
    test_split_by_delim()
    test_upper()
    print("All tests passed.")
