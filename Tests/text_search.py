import pytest
import text_search as Text_Search

def test_text_search():
    txt = 'dog'
    all_files = Text_Search.search(txt)
    expected_files = [
        '895502702_5170ada2ee.jpg',
        '925491651_57df3a5b36.jpg',
        '967719295_3257695095.jpg',
        '977856234_0d9caee7b2.jpg',
        '1009434119_febe49276a.jpg',
        '1129704496_4a61441f2c.jpg'
    ]
    for file in all_files:
        assert file in expected_files
