# Discord Bot

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

## Build and Install with Docker

Prerequisite:

* Docker

```bash
docker build --tag=discordbot .
```

```bash
export TOKEN="Discord API token"
docker run --env TOKEN=$TOKEN discordbot:latest
```