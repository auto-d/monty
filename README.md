# Monty

[Monty](https://github.com/auto-d/monty) is a command-line gardening assistant tool. It was created to provide a introduction to language-model-based agent patterns. Monty is built on top of [AutoGen](https://microsoft.github.io/autogen/) and leverages a handful of free open APIs to perform some up-front enrichment. 

## Setup

The application requires Python 3 and has been tested on MacOS 13.5.2. No filesystem dependencies exist and cross-platform deployment should work (my story). Dependencies are included in the repo and should be installed prior to running the tool. 

1. Set up a virtual environment to contain dependencies: `python -m venv .venv`
2. Activate your virtual environment: `source .venv/bin/activate`
2. Install dependencies: `pip install -r requirements.txt`
3. Check usage: `python monty.py --help`

ℹ️ To validate this CLI tool, an openAI API key is currently required. Acknowledging that's not ideal, here's a functioning key that can be used for testing and validation: 

>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

## Usage

*Backstory*: Monty is a curmudgeonly and notoriously terse assistant. His time is valuable and he knows it. His gatekeeper is a weather bot, who manages the weather history and forecast to ensure Monty makes sound recommendations for your garden. 

```
% python monty.py --help
usage: monty.py [-h] --backend {open-ai,ollama,internal} [--key KEY] [--uri URI] [--max-turns MAX_TURNS]

CLI for instantiating and interacting with the gardening agent.

options:
  -h, --help            show this help message and exit
  --backend {open-ai,ollama,internal}
                        backend LLM to use for the agent
  --key KEY             API key to use for LLM backend
  --uri URI             URI (ip:port/path) of LLM API
  --max-turns MAX_TURNS
                        Maximum number of turns to interact with monty
```

⛔️ The internal and Ollama-based backends have been removed due to performance issues on desktop hardware. 

### Examples

1. Start a chat session of no more than 3 turns with an OpenAI-driven Monty: `python monty.py --max-turns=3 --backend=open-ai --key=<openAI API key>`
2. Start a chat session with a locally hosted phi3 model: `python monty.py --backend=internal`

## Testing

A Pytest-compatible test regimen is included and can be run across the repo with a call to pytest, e.g. 

```
(venv) % pytest                                                                                                                                                                                                                      
================================================================================================================================================ test session starts ================================================================================================================================================
platform darwin -- Python 3.12.4, pytest-8.3.2, pluggy-1.5.0
plugins: anyio-4.4.0
collected 8 items                                                                                                                                                                                                                                                                                                   

test_agent.py ..                                                                                                                                                                                                                                                                                              [ 25%]
test_monty.py ...                                                                                                                                                                                                                                                                                             [ 62%]
test_weather.py ...                                                                                                                                                                                                                                                                                           [100%]

================================================================================================================================================ 8 passed in 17.84s =================================================================================================================================================
```


## Cites

1. [AutoGen Quickstart Documentation](https://microsoft.github.io/autogen/docs/Getting-Started)
1. [PyTest Good Integration Practices](https://docs.pytest.org/en/7.1.x/explanation/goodpractices.html)
1. [datetime API docs](https://docs.python.org/3/library/datetime.html#examples-of-usage-timedelta)
1. [Decoding the NOAA API](https://github.com/partytax/ncei-api-guide/blob/master/README.md)
1. [Open IP Geo API](https://api.techniknews.net/ipgeo)
1. [National Weather Service Forecast API](https://www.ncei.noaa.gov/cdo-web/api/v2/datasets)


