class Model:
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

    def pre_tournament_pred(
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
        # i think there is a better way to handle building and appending query params.
        q_p = f"tour={tour}"
        q_p += f"&add_position={add_position}" if add_position else ""
        q_p += "&dead_heat=yes" if dead_heat else "&dead_heat=no"
        q_p += f"&odds_format={odds_format}"

        return self.client.get(
            resource=f"{self._path}/pre-tournament?{q_p}", format=f_format
        )
