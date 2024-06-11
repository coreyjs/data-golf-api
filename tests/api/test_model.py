from unittest import mock


@mock.patch("httpx.Client.get")
def test_rankings(d_m, dg_client):
    dg_client.model.rankings()
    d_m.assert_called_once()
    assert (
        "https://feeds.datagolf.com/preds/get-dg-rankings?" in d_m.call_args[1]["url"]
    )

    assert d_m.call_args[1]["params"]["key"] == "test_key"


@mock.patch("httpx.Client.get")
def test_pre_tournament_pred(d_m, dg_client):
    dg_client.model.pre_tournament_pred()
    d_m.assert_called_once()
    assert "https://feeds.datagolf.com/preds/pre-tournament?" in d_m.call_args[1]["url"]

    assert d_m.call_args[1]["params"]["key"] == "test_key"
    assert d_m.call_args[1]["params"]["tour"] == "pga"
    assert d_m.call_args[1]["params"]["odds_format"] == "percent"
    assert d_m.call_args[1]["params"]["dead_heat"] == "yes"


@mock.patch("httpx.Client.get")
def test_pre_tournament_with_params(d_m, dg_client):
    dg_client.model.pre_tournament_pred(
        tour="euro", add_position="1,2,3", dead_heat=False, odds_format="american"
    )
    d_m.assert_called_once()
    assert "https://feeds.datagolf.com/preds/pre-tournament?" in d_m.call_args[1]["url"]

    assert d_m.call_args[1]["params"]["key"] == "test_key"
    assert d_m.call_args[1]["params"]["tour"] == "euro"
    assert d_m.call_args[1]["params"]["add_position"] == "1,2,3"
    assert d_m.call_args[1]["params"]["dead_heat"] == "no"
    assert d_m.call_args[1]["params"]["odds_format"] == "american"


@mock.patch("httpx.Client.get")
def test_pre_tournament_pred_archive(d_m, dg_client):
    dg_client.model.pre_tournament_pred_archive(event_id="100")
    d_m.assert_called_once()
    assert (
        "https://feeds.datagolf.com/preds/pre-tournament-archive?"
        in d_m.call_args[1]["url"]
    )

    assert d_m.call_args[1]["params"]["key"] == "test_key"
    assert d_m.call_args[1]["params"]["odds_format"] == "percent"
    assert d_m.call_args[1]["params"]["event_id"] == "100"


@mock.patch("httpx.Client.get")
def test_player_skill_decomp(d_m, dg_client):
    dg_client.model.player_skill_decompositions(tour="alt")
    d_m.assert_called_once()
    assert (
        "https://feeds.datagolf.com/preds/player-decompositions?"
        in d_m.call_args[1]["url"]
    )

    assert d_m.call_args[1]["params"]["key"] == "test_key"
    assert d_m.call_args[1]["params"]["tour"] == "alt"


@mock.patch("httpx.Client.get")
def test_player_skill_ratings(d_m, dg_client):
    dg_client.model.player_skill_ratings()
    d_m.assert_called_once()
    assert "https://feeds.datagolf.com/preds/skill-ratings?" in d_m.call_args[1]["url"]

    assert d_m.call_args[1]["params"]["key"] == "test_key"
    assert d_m.call_args[1]["params"]["display"] == "value"


@mock.patch("httpx.Client.get")
def test_detailed_approach_skill(d_m, dg_client):
    dg_client.model.detailed_approach_skill()
    d_m.assert_called_once()
    assert "https://feeds.datagolf.com/preds/approach-skill?" in d_m.call_args[1]["url"]

    assert d_m.call_args[1]["params"]["key"] == "test_key"
    assert d_m.call_args[1]["params"]["period"] == "l24"
