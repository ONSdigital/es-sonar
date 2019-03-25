from . import DemoPythonWithSonar

def test_DemoPythonWithSonar():
    assert DemoPythonWithSonar.apply("Jane") == "hello Jane"
