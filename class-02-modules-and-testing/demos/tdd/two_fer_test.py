from two_fer_module import two_fer

def test_no_name_given():
    actual = two_fer()
    expected = 'One for you, one for me.'
    assert expected == actual


def test_no_Alice_given():
    actual = two_fer('Alice')
    expected = 'One for Alice, one for me.'
    assert expected == actual

def test_no_Bob_given():
    actual = two_fer('Bob')
    expected = 'One for Bob, one for me.'
    assert expected == actual
