import pytest

from data_golf import DataGolfClient
from data_golf.api.general import General
from data_golf.client import DGCInvalidApiKey


def test_client_responds_to_general():
    dgc = DataGolfClient(api_key="test_key")
    assert isinstance(dgc.general, General)


def test_client_will_err_on_invalid_api_key():
    with pytest.raises(DGCInvalidApiKey):
        DataGolfClient(api_key=1234)
