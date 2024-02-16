def test_installation_from_src_layout():
    import dlp
    from dlp import dummy
    assert dummy() == 42
