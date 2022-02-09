from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest



def test_make_full_name():
    assert make_full_name("Karenn", "Teran") == "Teran; Karenn"
    assert make_full_name("Jesus", "Perez-Gonzalez") == "Perez-Gonzalez; Jesus"
    assert make_full_name("Ana", "Abreu") == "Abreu; Ana"



def test_extract_family_name():
    assert extract_family_name("Teran; Karenn") == "Teran"
    assert extract_family_name("Perez-Gonzalez; Jesus") == "Perez-Gonzalez"
    assert extract_family_name("Abreu; Ana") == "Abreu"


def test_extract_given_name():
    assert extract_given_name("Teran; Karenn") == "Karenn"
    assert extract_given_name("Perez-Gonzalez; Jesus") == "Jesus"
    assert extract_given_name("Abreu; Ana") == "Ana"





# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])