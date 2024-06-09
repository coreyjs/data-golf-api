from unittest import mock

import pytest


@mock.patch("httpx.Client.get")
def test_request_gets_json_header(d_m, dg_client):
    dg_client.general.player_list()
    d_m.assert_called_once()
    assert d_m.call_args[1]["headers"]["Content-Type"] == "application/json"


@mock.patch("httpx.Client.get")
def test_api_key_appends_to_request(d_m, dg_client):
    dg_client.general.player_list()
    d_m.assert_called_once()
    assert (
        d_m.call_args[1]["url"]
        == "https://feeds.datagolf.com/get-player-list?key=test_key&file_format=json"
    )
    assert "key=test_key" in d_m.call_args[1]["url"]


def test_request_will_err_on_csv_format(dg_client):
    with pytest.raises(ValueError):
        dg_client.general.player_list(format="csv")


@mock.patch("httpx.Client.get")
def test_player_list(d_m, dg_client):
    dg_client.general.player_list()
    d_m.assert_called_once()
    assert (
        d_m.call_args[1]["url"]
        == "https://feeds.datagolf.com/get-player-list?key=test_key&file_format=json"
    )


@mock.patch("httpx.Client.get")
def test_tour_schedule(d_m, dg_client):
    dg_client.general.tour_schedule()
    d_m.assert_called_once()
    assert (
        d_m.call_args[1]["url"]
        == "https://feeds.datagolf.com/get-schedule?tour=all&key=test_key&file_format=json"
    )


@mock.patch("httpx.Client.get")
def test_tour_schedule_for_tour(d_m, dg_client):
    dg_client.general.tour_schedule(tour="kft")
    d_m.assert_called_once()
    assert (
        d_m.call_args[1]["url"]
        == "https://feeds.datagolf.com/get-schedule?tour=kft&key=test_key&file_format=json"
    )


@mock.patch("httpx.Client.get")
def test_field_updates(d_m, dg_client):
    dg_client.general.field_updates()
    d_m.assert_called_once()
    assert (
        d_m.call_args[1]["url"]
        == "https://feeds.datagolf.com/field-updates?key=test_key&file_format=json"
    )


@mock.patch("httpx.Client.get")
def test_field_updates_with_tour_euro(d_m, dg_client):
    dg_client.general.field_updates(tour="euro")
    d_m.assert_called_once()
    assert (
        d_m.call_args[1]["url"]
        == "https://feeds.datagolf.com/field-updates?tour=euro&key=test_key&file_format=json"
    )
