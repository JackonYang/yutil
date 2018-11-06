# -*- coding: utf-8 -*-
from yutil.dataci import (
    use_json_data,
)

from yutil.text_cleaning.html_text import (
    convert_html_to_text,
)


@use_json_data('html-to-text.json')
def test_clean_spaces(input_obj, expect):
    assert convert_html_to_text(input_obj) == expect
