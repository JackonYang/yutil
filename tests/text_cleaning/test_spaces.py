# -*- coding: utf-8 -*-
from yutil.dataci import (
    use_json_data,
)

from yutil.text_cleaning.spaces import (
    remove_continuous_spaces,
)


@use_json_data('continuous-spaces.json')
def test_clean_spaces(input_obj, expect):
    assert remove_continuous_spaces(input_obj) == expect
