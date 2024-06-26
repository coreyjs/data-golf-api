class Betting:
    def __init__(self, client):
        self._client = client
        self._path = "/betting-tools"

    def outright_odds(
        self,
        market: str,
        tour: str = "pga",
        odds_format: str = "decimal",
        f_format: str = "json",
    ) -> dict:
        """
        Returns the most recent win, top 5, top 10, top 20, make/miss cut, and
         first round leader odds offered at 11 sportsbooks alongside the corresponding
          predictions from the DG model.
        :param market: (str, required). Specifies the match-up market. Supports values: win, top_5, top_10,
        top_20, mc, make_cut, frl
        :param tour: (str, optional).  pga (default), euro, kft, opp (opposite field PGA TOUR event), alt
        :param odds_format: (str, optional)  Specifies the odds format. Supports values: percent, american, decimal
            (default), fraction
        :param f_format: (str, optional) json (default)
        :return: dict
        """
        query_p = {"tour": tour, "odds_format": odds_format, "market": market}

        return self._client.get(
            resource=f"{self._path}/outrights", params=query_p, format=f_format
        )

    def matchup_odds(
        self,
        market: str,
        tour: str = "pga",
        odds_format: str = "decimal",
        f_format: str = "json",
    ) -> dict:
        """
        Returns the most recent tournament match-up, round match-up, and 3-ball odds offered at 8
            sportsbooks alongside the corresponding prediction from our model.
        :param market: (str, required). Specifies the match-up market. Supports values: tournament_matchups,
        round_matchups, 3_balls
        :param tour: (str, optional).  pga (default), euro, kft, opp (opposite field PGA TOUR event), alt
        :param odds_format: (str, optional)  Specifies the odds format. Supports values: percent, american, decimal (default), fraction
        :param f_format: (str, optional) json (default)
        :return:
        """
        query_p = {"tour": tour, "odds_format": odds_format, "market": market}
        return self._client.get(
            resource=f"{self._path}/matchups", params=query_p, format=f_format
        )

    def matchup_odds_all_pairings(
        self, tour: str = "pga", odds_format: str = "decimal", f_format: str = "json"
    ) -> dict:
        """
        Returns Data Golf matchup / 3-ball odds for every pairing in the next round of
            current PGA Tour and European Tour events.
        :param tour: (str, optional).  pga (default), euro, opp, alt
        :param odds_format: (str, optional)  Specifies the odds format. Supports values: percent, american, decimal (default), fraction
        :param f_format: (str, optional) json (default)
        :return:
        """
        query_p = {"tour": tour, "odds_format": odds_format}
        return self._client.get(
            resource=f"{self._path}/matchups-all-pairings",
            params=query_p,
            format=f_format,
        )
