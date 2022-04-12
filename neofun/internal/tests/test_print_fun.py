from neofun.internal.gogo import print_gogo


def test_importing():
    assert (print_gogo() == 'gogo gadget')
