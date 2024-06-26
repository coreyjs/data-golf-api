from typing import List


class Historical:
    def __init__(self, client):
        self._client = client
        self._path = "/historical-raw-data"

    def events(self, f_format: str = "json") -> List[dict]:
        """
        Returns a list of all events in the Data Golf database.
        :param f_format: (str, optional) json (default)
        :return: dict
        """
        return self._client.get(resource=f"{self._path}/event-list", format=f_format)

    def rounds(self, tour: str, event: str, year: str, f_format: str = "json"):
        """
        Returns round-level scoring, traditional stats, strokes-gained, and tee time data across 22 global tours.
        :param tour: (str, required) Specifies the tour. Hover over tour
            codes in table https://datagolf.com/raw-data-archive to see full tour names.
            pga, euro, kft, cha, jpn, anz, alp, champ, kor, ngl, bet, chn, afr, pgt, pgti,
             atvt, atgt, sam, ept, can, liv, mex
        :param event: (str, required) IDs can be found via Historical.events
        :param year: (str, required)
        :param f_format: (str, optional) json (default)
        :return:
        """
        query_p = {"tour": tour, "event": event, "year": year}
        return self._client.get(
            resource=f"{self._path}/rounds", params=query_p, format=f_format
        )
