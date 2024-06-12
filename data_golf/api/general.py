from typing import List


class General:
    def __init__(self, client):
        self.client = client

    def player_list(self, format: str = "json") -> List[dict]:
        """

        :return:
        """
        return self.client.get(resource="/get-player-list", format=format)

    def tour_schedule(self, tour: str = "all", f_format: str = "json") -> dict:
        """
        Current season schedule for PGA Tour, European Tour, Korn Ferry Tour, and LIV.
        :param tour: str optional defaults to 'all', the tour you want the schedule for.  values: all, pga, euro, kft, alt, liv
        :param f_format:
        :return:
        """
        return self.client.get(
            resource="/get-schedule", params={"tour": tour}, format=f_format
        )

    def field_updates(self, tour: str = "pga", f_format: str = "json") -> List[dict]:
        """
        Up-to-the-minute field updates on WDs, Monday Qualifiers, tee times, and fantasy salaries for PGA Tour,
        European Tour, and Korn Ferry Tour events. Includes data golf IDs and tour-specific IDs for
        each player in the field.
        :type tour: str := pga (default), euro, kft, opp, alt
        :return:
        """

        return self.client.get(
            resource="/field-updates", params={"tour": tour}, format=f_format
        )
