from unittest import mock


@mock.patch("httpx.Client.get")
def test_rankings(d_m, dg_client):
    dg_client.model.rankings()
    d_m.assert_called_once()
    assert (
        "https://feeds.datagolf.com/preds/get-dg-rankings?" in d_m.call_args[1]["url"]
    )

    assert "key=test_key" in d_m.call_args[1]["url"]


@mock.patch("httpx.Client.get")
def test_pre_tournament_pred(d_m, dg_client):
    dg_client.model.pre_tournament_pred()
    d_m.assert_called_once()
    assert "https://feeds.datagolf.com/preds/pre-tournament?" in d_m.call_args[1]["url"]

    assert "key=test_key" in d_m.call_args[1]["url"]
    assert "tour=pga" in d_m.call_args[1]["url"]
    assert "odds_format=percent" in d_m.call_args[1]["url"]
    assert "dead_heat=yes" in d_m.call_args[1]["url"]


@mock.patch("httpx.Client.get")
def test_pre_tournament_with_params(d_m, dg_client):
    dg_client.model.pre_tournament_pred(
        tour="euro", add_position="1,2,3", dead_heat=False, odds_format="american"
    )
    d_m.assert_called_once()
    assert "https://feeds.datagolf.com/preds/pre-tournament?" in d_m.call_args[1]["url"]

    assert "key=test_key" in d_m.call_args[1]["url"]
    assert "tour=euro" in d_m.call_args[1]["url"]
    assert "add_position=1,2,3" in d_m.call_args[1]["url"]
    assert "dead_heat=no" in d_m.call_args[1]["url"]
    assert "odds_format=american" in d_m.call_args[1]["url"]


@mock.patch("httpx.Client.get")
def test_pre_tournament_pred_archive(d_m, dg_client):
    dg_client.model.pre_tournament_pred_archive(event_id="100")
    d_m.assert_called_once()
    assert (
        "https://feeds.datagolf.com/preds/pre-tournament-archive?"
        in d_m.call_args[1]["url"]
    )

    assert "key=test_key" in d_m.call_args[1]["url"]
    assert "odds_format=percent" in d_m.call_args[1]["url"]
    assert "event_id=100" in d_m.call_args[1]["url"]


@mock.patch("httpx.Client.get")
def test_player_skill_decomp(d_m, dg_client):
    dg_client.model.player_skill_decompositions(tour="alt")
    d_m.assert_called_once()
    assert (
        "https://feeds.datagolf.com/preds/player-decompositions?"
        in d_m.call_args[1]["url"]
    )

    assert "key=test_key" in d_m.call_args[1]["url"]
    assert "tour=alt" in d_m.call_args[1]["url"]


@mock.patch("httpx.Client.get")
def test_player_skill_ratings(d_m, dg_client):
    dg_client.model.player_skill_ratings()
    d_m.assert_called_once()
    assert (
        "https://feeds.datagolf.com/preds/skill-ratings?"
        in d_m.call_args[1]["url"]
    )

    assert "key=test_key" in d_m.call_args[1]["url"]
    assert "display=value" in d_m.call_args[1]["url"]


@mock.patch("httpx.Client.get")
def test_detailed_approach_skill(d_m, dg_client):
    dg_client.model.detailed_approach_skill()
    d_m.assert_called_once()
    assert "https://feeds.datagolf.com/preds/approach-skill?" in d_m.call_args[1]["url"]

    assert "key=test_key" in d_m.call_args[1]["url"]
    assert "period=l24" in d_m.call_args[1]["url"]
