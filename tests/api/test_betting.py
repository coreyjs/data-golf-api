from unittest import mock


@mock.patch("httpx.Client.get")
def test_outright_odds(d_m, dg_client):
    dg_client.betting.outright_odds(market="win")
    d_m.assert_called_once()
    assert (
        "https://feeds.datagolf.com/betting-tools/outright" in d_m.call_args[1]["url"]
    )

    assert d_m.call_args[1]["params"]["key"] == "test_key"
    assert d_m.call_args[1]["params"]["market"] == "win"


@mock.patch("httpx.Client.get")
def test_matchups(d_m, dg_client):
    dg_client.betting.outright_odds(market="3_balls")
    d_m.assert_called_once()
    assert (
        "https://feeds.datagolf.com/betting-tools/outright" in d_m.call_args[1]["url"]
    )

    assert d_m.call_args[1]["params"]["key"] == "test_key"
    assert d_m.call_args[1]["params"]["market"] == "3_balls"
