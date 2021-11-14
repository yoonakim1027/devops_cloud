from . import reverse_string

def test_reverse_string():
    assert reverse_string.check_available("거꾸로: 안녕")
    assert reverse_string.make_response("거꾸로: 안녕") == "녕안"
