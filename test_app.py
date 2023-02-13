import pytest
i = 0

_threshold = 3

def test_flaky():
    global i, _threshold
    print("Thresholdd ", _threshold)
    i += 1
    assert i == _threshold


def test_fail_all():
    print("Intentional fail!")
    assert 1 == 3


def test_success():
    assert 1 == 1


@pytest.mark.xfail
def test_xfail():
    assert 1 == 2


@pytest.mark.xfail
def test_xpass():
    assert 1 == 1

def test_error():
    sys.stderr.write("stderr log!\n")
    assert 1/0 == 1


@pytest.mark.skip(reason="no way of currently testing this")
def test_skip():
    return "a"


class TestReport:
    def test_suite_success(self):
        assert 1 == 1

    def test_suite_fail(self):
        assert 1 == 2
