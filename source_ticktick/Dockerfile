FROM python:3.12-slim

# to build : run this from the root directory 
#  docker build -t tickbyte -f source_ticktick/Dockerfile . 


# install curl 
RUN apt-get update && apt-get install -y curl


# Install uv
RUN curl -LsSf https://astral.sh/uv/install.sh | UV_INSTALL_DIR="/usr/local/bin" sh

WORKDIR /airbyte/integration_code
COPY ../pyproject.toml ./
RUN /usr/local/bin/uv sync

COPY . ./source_ticktick/

ENV AIRBYTE_ENTRYPOINT "python /airbyte/integration_code/source_ticktick/main.py"
ENTRYPOINT ["/bin/bash", "-c", "$AIRBYTE_ENTRYPOINT"]