from datetime import datetime


def test_create_directory(tmpdir):
    '''Test creating of directory'''

    folder = tmpdir.mkdir(datetime.today().strftime("%Y-%m-%d"))
    print(dir(folder))
    assert str(folder) == str(datetime.today().strftime("%Y-%m-%d"))
