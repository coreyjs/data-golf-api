class Prediction:
    def __init__(self, client):
        self.client = client
        self._path = "/preds"

    def rankings(self, f_format: str = "json") -> dict:
        """
        Returns top 500 players according to DG model predictions.
        :return: dict
        """
        return self.client.get(
            resource=f"{self._path}/get-dg-rankings", format=f_format
        )

    def pre_tournament(
        self,
        tour: str = "pga",
        add_position: str = None,
        dead_heat: bool = True,
        odds_format: str = "percent",
        f_format: str = "json",
    ) -> dict:
        """

        :param tour: pga, euro, kft, opp, alt
        :param add_position: 1, 2, 3 (csv separated values)
        :param dead_heat: bool - Adjust odds for dead-heat rules.
        :param odds_format: percent (default), american, decimal, fraction
        :param f_format: json (default)
        :return:
        """
        query_p = {"tour": tour}
        if add_position:
            query_p["add_position"] = add_position

        query_p["dead_heat"] = "yes" if dead_heat else "no"
        query_p["odds_format"] = odds_format

        return self.client.get(
            resource=f"{self._path}/pre-tournament?", params=query_p, format=f_format
        )

    def pre_tournament_pred_archive(
        self,
        event_id: str = None,
        year: str = None,
        odds_format: str = "percent",
        f_format="json",
    ) -> dict:
        """
        Returns pre-tournament predictions for a specific event or year.
        :param event_id: The event id for the tournament.
        :param year: The year for the tournament.
        :param odds_format: percent (default), american, decimal, fraction
        :param f_format: json (default)
        :return: dict
        """

        query_p = {}

        if event_id:
            query_p["event_id"] = event_id
        if year:
            query_p["year"] = year
        query_p["odds_format"] = odds_format
        query_p["file_format"] = f_format

        return self.client.get(
            resource=f"{self._path}/pre-tournament-archive",
            params=query_p,
            format=f_format,
        )

    def player_skill_decompositions(
        self, tour: str = "pga", f_format: str = "json"
    ) -> dict:
        """
        Returns player skill decompositions for a specific tour.
        :param tour: pga, euro, kft, opp, alt
        :param f_format: json (default)
        :return: dict
        """
        query_p = {"tour": tour}
        return self.client.get(
            resource=f"{self._path}/player-decompositions",
            params=query_p,
            format=f_format,
        )

    def player_skill_ratings(
        self, display: str = "value", f_format: str = "json"
    ) -> dict:
        """
        Returns our estimate and rank for each skill for all players with sufficient Shotlink measured rounds (at least 30 rounds in the last year or 50 in the last 2 years).
        :param display: value, rank
        :param f_format: json (default)
        :return: dict
        """
        query_p = {"display": display}
        return self.client.get(
            resource=f"{self._path}/skill-ratings",
            params=query_p,
            format=f_format,
        )

    def detailed_approach_skill(
        self, period: str = "l24", f_format: str = "json"
    ) -> dict:
        """
        Returns detailed player-level approach performance stats (strokes-gained per shot, proximity, GIR, good shot rate, poor shot avoidance rate) across various yardage/lie buckets.
        :param period: l24 (last 24 months) (default), l12 (last 12 months), ytd (year to date)
        :param f_format: json (default)
        :return: dict
        """
        query_p = {"period": period}
        return self.client.get(
            resource=f"{self._path}/approach-skill",
            params=query_p,
            format=f_format,
        )

    def fantasy_projection(
        self,
        tour: str = "pga",
        slate: str = "main",
        site: str = "draftkings",
        f_format: str = "json",
    ) -> dict:
        """
        Returns our fantasy projections for a specific tour and slate.
        :param tour: pga (default), euro, opp (opposite field PGA TOUR event), alt
        :param slate: main (default), showdown, showdown_late, weekend, captain
        :param site: draftkings (default), fanduel, yahoo
        :param f_format: json (default)
        :return: dict
        """
        query_p = {"tour": tour, "slate": slate, "site": site}
        return self.client.get(
            resource=f"{self._path}/fantasy-projection-defaults",
            params=query_p,
            format=f_format,
        )
