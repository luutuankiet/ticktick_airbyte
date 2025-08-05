#
# Copyright (c) 2023 Airbyte, Inc., all rights reserved.
#


from airbyte_cdk.sources.source import Source
from airbyte_cdk.sources.streams.stream import Stream
from airbyte_cdk.sources.streams.http.auth import Oauth2Authenticator

from typing import Any, Dict, List, Mapping, Optional, Tuple, Iterable

from .streams import Projects


class SourceTicktick(Source):
    def check(self, logger, config: Mapping[str, Any]) -> Tuple[bool, Optional[str]]:
        """
        Tests if the input configuration can be used to successfully connect to the external resource

        :param logger:
        :param config:  The user-provided configuration as specified by the connector's spec.yaml.
        :return: Tuple of (boolean, error message). If boolean is true, then the connection check is successful.
        If false, then the connection check is unsuccessful and the second element of the tuple should be a human-readable
        message explaining why the connection check failed.
        """
        try:
            # TODO: Implement actual connection check using the dida365 library
            # For now, a placeholder check
            client_id = config["client_id"]
            client_secret = config["client_secret"]
            username = config["username"]
            password = config["password"]

            if not all([client_id, client_secret, username, password]):
                return False, "Client ID, Client Secret, Username, and Password must be provided."

            # In a real scenario, you would attempt to authenticate with the TickTick API here
            # using the dida365 library and the provided credentials.
            # For example:
            # auth = Oauth2Authenticator(
            #     token_refresh_endpoint="https://api.ticktick.com/api/v2/oauth/token",
            #     client_id=client_id,
            #     client_secret=client_secret,
            #     refresh_token=None, # You'd get this after initial auth
            #     oauth_request_body={
            #         "grant_type": "password",
            #         "username": username,
            #         "password": password,
            #     }
            # )
            # access_token = auth.get_access_token()
            # if not access_token:
            #     return False, "Authentication failed. Please check your credentials."

            return True, None
        except Exception as e:
            return False, f"An exception occurred: {str(e)}"

    def streams(self, config: Mapping[str, Any]) -> List[Stream]:
        """
        :param config: The user-provided configuration as specified by the connector's spec.yaml.
        :return: List of the connector's streams.
        """
        # TODO: Instantiate and return actual stream instances
        # For now, returning placeholder streams
        authenticator = Oauth2Authenticator(
            token_refresh_endpoint="https://api.ticktick.com/api/v2/oauth/token",
            client_id=config["client_id"],
            client_secret=config["client_secret"],
            refresh_token=config["access_token"], # Use access_token from config
            oauth_request_body={
                "grant_type": "password", # This will be ignored if refresh_token is present
                "username": "", # Not used for access_token auth
                "password": "", # Not used for access_token auth
            },
        )
        return [
            Projects(authenticator=authenticator),
        ]