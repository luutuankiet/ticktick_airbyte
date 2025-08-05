# Product Context

This file provides a high-level overview of the project and the expected product that will be created. Initially it is based upon projectBrief.md (if provided) and all other available project-related information in the working directory. This file is intended to be updated as the project evolves, and should be used to inform all other modes of the project's goals and context.
2025-08-04 23:23:40 - Log of updates made will be appended as footnotes to the end of this file.

*

## Project Goal

*   Building and Deploying a Custom Airbyte Connector for TickTick on GCP

## Key Features

*   Building a custom Airbyte source connector for TickTick using the Python CDK.
*   Interacting with the TickTick API using the `dida365` library.
*   Implementing core connector methods: `spec`, `check`, `discover`, `read`.
*   Building and packaging the connector as a Docker image.
*   Deploying the connector on a free-tier Google Cloud Platform (GCP) instance.

## Overall Architecture

*   The connector will be built using the Airbyte Python CDK.
*   It will use the `dida365` library for asynchronous interaction with the TickTick API, utilizing OAuth2 authentication.
*   The connector will be packaged as a Docker image and pushed to a Docker registry for deployment on GCP.