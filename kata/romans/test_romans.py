import romans

def test_to_romans():
    assert romans.to_romans(0) == ""
    assert romans.to_romans(18) == "XVIII"
    assert romans.to_romans(1939) == "MCMXXXIX"