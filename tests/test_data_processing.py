# Contoh sebuah unit test sederhana
def a_simple_data_processing_function(x):
    return x + 1

def test_processing_function():
    assert a_simple_data_processing_function(3) == 4
    print("\nUnit test passed!")