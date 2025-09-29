from src.ap_donnes_des_sous.banque import ap_donnes_des_sous

def test_donnes_des_sous(): 
    result = ap_donnes_des_sous(12, 11)
    assert result == 23

def test_donnes_beaucoup_des_sous():
    result = ap_donnes_des_sous(212, 11)
    assert result == 23