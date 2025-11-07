
FROM python:3.9-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    perl git && apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /github/workspace
COPY . /github/workspace

RUN chmod +x .github/scripts/*.sh

ENTRYPOINT ["/github/workspace/.github/scripts/entrypoint.sh"]
