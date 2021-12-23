import os
import sys

dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)

from reports.report_example import get_data_dict # noqa


def test_get_data_dict():
    dd = get_data_dict()
    for k in dd:
        assert isinstance(dd[k], str)
