def test_version_author():
    import ctm_python_client

    assert ctm_python_client.__author__ == 'BMC Software'
    assert ctm_python_client.__version__ == '2.1.4'


