import template_check.hello


def test_basic_test() -> None:
    template_check.hello.hello_world()
    assert True
