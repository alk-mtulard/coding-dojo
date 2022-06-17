from simple_music_encoder import __version__, compress


def test_version():
    assert __version__ == "0.1.0"


def test_no_compression_with_one_bit():
    uncompressed = [2]
    result = compress(uncompressed)
    assert result == "2"


def test_no_compression_with_multiple_bit():
    uncompressed = [2, 3]
    result = compress(uncompressed)
    assert result == "2,3"


def test_sequence_of_identical():
    uncompressed = [1, 1, 1]
    result = compress(uncompressed)
    assert result == "1*3"


def test_sequence_of_identical_without_first():
    uncompressed = [2, 1, 1, 1]
    result = compress(uncompressed)
    assert result == "2,1*3"


def test_sequence_of_identical_without_last():
    uncompressed = [1, 1, 1, 2]
    result = compress(uncompressed)
    assert result == "1*3,2"


def test_sequence_of_consecutive():
    uncompressed = [1, 3, 5]
    result = compress(uncompressed)
    assert result == "1-5/2"


def test_sequence_of_consecutive_without_first():
    uncompressed = [1, 2, 4, 6]
    result = compress(uncompressed)
    assert result == "1,2-6/2"


def test_sequence_of_consecutive_without_last():
    uncompressed = [2, 4, 6, 1]
    result = compress(uncompressed)
    assert result == "2-6/2,1"


def test_firework():
    uncompressed = [0, 2, 4, 5, 7, 6, 5, 5, 5, 5, 5]
    result = compress(uncompressed)
    assert result == "0-4/2,5,7-5,5*4"
