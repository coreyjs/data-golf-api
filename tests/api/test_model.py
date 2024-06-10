from unittest import mock


@mock.patch("httpx.Client.get")
def test_rankings(d_m, dg_client):
    dg_client.model.rankings()
    d_m.assert_called_once()
    assert (
        d_m.call_args[1]["url"]
        == "https://feeds.datagolf.com/preds/get-dg-rankings?key=test_key&file_format=json"
    )


@mock.patch("httpx.Client.get")
def test_pre_tournament_pred(d_m, dg_client):
    dg_client.model.pre_tournament_pred()
    d_m.assert_called_once()
    assert (
        d_m.call_args[1]["url"]
        == "https://feeds.datagolf.com/preds/pre-tournament?tour=pga&dead_heat=yes&odds_format=percent&key=test_key&file_format=json"
    )


@mock.patch("httpx.Client.get")
def test_pre_tournament_with_params(d_m, dg_client):
    dg_client.model.pre_tournament_pred(
        tour="euro", add_position="1,2,3", dead_heat=False, odds_format="american"
    )
    d_m.assert_called_once()
    assert (
        d_m.call_args[1]["url"]
        == "https://feeds.datagolf.com/preds/pre-tournament?tour=euro&add_position=1,2,3&dead_heat=no&odds_format=american&key=test_key&file_format=json"
    )
