from typing import List


class General:
    def __init__(self, client):
        self.client = client

    def player_list(self, format: str = "json") -> List[dict]:
        """

        :return:
        """
        return self.client.get(resource="/get-player-list", format=format)

    def tour_schedule(self, format: str = "json") -> List[dict]:
        """

        :return:
        """
        return self.client.get(resource="/get-schedule", format=format)
