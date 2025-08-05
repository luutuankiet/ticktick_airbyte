# TickTick Airbyte Connector

This repository contains a custom Airbyte source connector for TickTick, designed to extract data from TickTick accounts into various destinations supported by Airbyte.

## Project Goal

The overarching goal is to build a robust and deployable Airbyte connector for TickTick, with an initial focus on a Proof of Concept (POC) to establish core functionality.

## Current Status: Proof of Concept (POC) Development

We are currently developing a minimal POC for the TickTick connector. The focus of this POC is to:

*   **Authenticate:** Successfully connect to the TickTick API using a pre-generated OAuth2 access token.
*   **Extract Data:** Read data from the simplest available endpoint, which is the "Projects" stream.

### Key Decisions for the POC:

*   **Authentication:** Due to the interactive nature of the `dida365` Python client's OAuth2 flow, the POC will utilize a pre-generated `access_token` provided in the connector's configuration (`spec.yaml`).
*   **Stream Simplification:** For the POC, only the `Projects` stream is being implemented to streamline development and testing.
*   **Dependency Management:** `uv` is used for dependency management, with dependencies defined in the root `pyproject.toml` and installed via the `Dockerfile`.

### Current Progress:

*   Project structure defined (`source_ticktick/` subdirectory with `source.py`, `spec.yaml`, `Dockerfile`, `main.py`, `streams.py`, `unit_tests/`).
*   Development environment setup (Python, Docker, `uv`).
*   Airbyte connector project initialized using the Python CDK.
*   `dida365` API client integrated.
*   `spec` method for connector configuration implemented and revised for POC (using `access_token`).
*   Streams simplified to define only the `Projects` stream.
*   **Currently in progress:** Implementing the `check` method (POC Version) to validate credentials.

For a more detailed architectural design, rationale, and future plans, please refer to the [`handoff.md`](handoff.md) document.