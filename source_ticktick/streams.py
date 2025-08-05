#
# Copyright (c) 2023 Airbyte, Inc., all rights reserved.
#

from typing import Any, Iterable, Mapping, Optional, List

import requests
from airbyte_cdk.sources.streams.http import HttpStream
from airbyte_cdk.sources.streams.http.auth import Oauth2Authenticator
from dida365 import Dida365Client, ServiceType


class Projects(HttpStream):
    url_base = "https://api.ticktick.com/api/v2/"

    def __init__(self, authenticator: Oauth2Authenticator, config: Mapping[str, Any]):
        super().__init__(authenticator=authenticator)
        self.authenticator = authenticator
        self.config = config
        self.client = Dida365Client(
            client_id=config["client_id"],
            client_secret=config["client_secret"],
            service_type=ServiceType.TICKTICK,
        )
        # Manually set the token for POC
        self.client.http.set_token(config["access_token"])


    def next_page_token(self, response: requests.Response) -> Optional[Mapping[str, Any]]:
        return None

    def parse_response(self, response: requests.Response, **kwargs) -> Iterable[Mapping]:
        yield from response.json()

    def path(self, **kwargs) -> str:
        return "projects"

    def primary_key(self, stream_slice: Mapping[str, Any], replica_state: Mapping[str, Any]) -> Optional[List[str]]:
        return ["id"]