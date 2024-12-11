import romans

def test_to_romans_keys():
    assert romans.to_romans_from(0) == ""
    assert romans.to_romans_from(18) == "XVIII"
    assert romans.to_romans_from(1939) == "MCMXXXIX"

def test_to_romans():
    assert romans.to_romans_from([1]) == "I"
    assert romans.to_romans_from([10,5,1,1,1]) == "XVIII"
    assert romans.to_romans_from([1000,900,10,10,10,9]) == "MCMXXXIX"