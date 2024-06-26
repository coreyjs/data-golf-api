class LivePrediction:
    def __init__(self, client):
        self.client = client
        self._path = "/preds"

    def live_in_play(
        self,
        tour: str = "pga",
        dead_heat: bool = False,
        odds_format: str = "percent",
        f_format: str = "json",
    ) -> dict:
        """
        Returns live (updating at 5 minute intervals) finish probabilities for ongoing PGA and European Tour tournaments.
        :param tour: pga (default), euro, opp (opposite field PGA TOUR event), kft, alt
        :param dead_heat: False (default), True
        :param odds_format: percent (default), american, decimal, fraction
        :param f_format: Defaults to JSON.
        :return: dict
        """
        query_p = {
            "odds_format": odds_format,
            "dead_heat": "yes" if dead_heat else "no",
            "tour": tour,
        }

        return self.client.get(
            resource=f"{self._path}/in-play", params=query_p, format=f_format
        )

    def live_tournament_stats(
        self,
        stats: str = None,
        round: str = None,
        display: str = "value",
        f_format: str = "json",
    ) -> dict:
        """
        Returns live strokes-gained and traditional stats for every player during
        PGA Tour tournaments
        :param stats: Comma-seperated list of statistics to be returned.  Accepts:
        [sg_putt, sg_arg, sg_app, sg_ott, sg_t2g, sg_bs, sg_total, distance,
        accuracy, gir, prox_fw, prox_rgh, scrambling]
        :param round: Specifies the round: Accepts: (event_avg, 1, 2, 3, 4)
        :param display: Specifies how stats are displayed. Accepts values: value (default), rank
        :param f_format:
        :return: dict
        """
        query_p = {
            "display": display,
        }

        if stats:
            query_p["stats"] = stats
        if round:
            query_p["round"] = round
        return self.client.get(
            resource=f"{self._path}/live-tournament-stats",
            params=query_p,
            format=f_format,
        )

    def live_hole_stats(self, tour: str = "pga", f_format: str = "json"):
        """
        Returns live hole scoring averages and distrubutions (birdies, pars, bogeys, etc.) broken down by tee time wave.
        :param tour: pga (default), euro, kft, opp, alt
        :param f_format: Defaults to JSON.
        :return:
        """
        return self.client.get(
            resource=f"{self._path}/live-hole-stats",
            params={"tour": tour},
            format=f_format,
        )
