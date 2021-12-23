from report_example import get_data_dict


def test_get_data_dict():
    dd = get_data_dict()
    for k in dd:
        assert isinstance(dd[k], str)
