from datetime import datetime


def test_create_directory(tmpdir):
    '''Test creating of directory'''

    directory = tmpdir.mkdir(datetime.today().strftime("%Y-%m-%d"))
    assert directory.basename == datetime.today().strftime("%Y-%m-%d")
    assert directory.isdir()
