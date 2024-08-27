# Monty

[Monty](https://github.com/auto-d/monty) is a command-line gardening assistant tool. It was created to provide a introduction to language-model-based agent patterns. Monty is built on top of [AutoGen](https://microsoft.github.io/autogen/) and leverages a handful of free open APIs to perform some up-front enrichment. 

## Setup

The application requires Python 3 (developed w/ 3.12) and has been tested on MacOS 13.5. No filesystem dependencies exist and cross-platform deployment should work (my story). Dependencies are included in the repo and should be installed prior to running the tool. 

1. Set up a virtual environment to contain dependencies: `python -m venv .venv`
2. Activate your virtual environment: `source .venv/bin/activate`
2. Install dependencies: `pip install -r requirements.txt`
3. Check usage: `python monty.py --help`

ℹ️ To validate this CLI tool, an openAI API key is currently required. I would a limited use key here but apparently OpenAI scans public GitHub repos and disables any keys it finds. :/ 

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

### Example

Start a chat session of no more than 3 turns with an OpenAI-driven Monty: : `python monty.py --max-turns=3 --backend=open-ai --key='<openAI API key>'`

```
(venv) % python monty.py --max-turns=1 --backend=open-ai --key='...'
--------------------------------------------------------------------------------
Doing some background research to furnish to your gardener (monty).
Looking up location by IP...
Resolving weather prediction site...
Retrieving forecast...
Querying for historical precipitation, this might take a bit...
Failed to parse precipitation data response from NOAA API, bailing! 
 This may happen if there are no historicals available for the identified zip code (27605)
Gardener started!
 ! Ignore subsequent API key warning, autogen validation routine is outdated. (╯°□°)╯
[autogen.oai.client: 08-26 22:59:51] {164} WARNING - The API key specified is not a valid OpenAI format; it won't work with the OpenAI-hosted model.
weather-bot (to monty):

Today is 2024-08-26. There is no historical precipitation available. The forecast for next week is:
 - Day 1: Mostly clear, with a low around 66. Southwest wind around 2 mph.
 - Day 2: Sunny, with a high near 94. Southwest wind 2 to 6 mph.
 - Day 3: Mostly clear, with a low around 71. Southwest wind around 5 mph.
 - Day 4: Sunny, with a high near 97. Heat index values as high as 101. Southwest wind around 6 mph.
 - Day 5: Mostly clear, with a low around 75. Southwest wind around 6 mph.
 - Day 6: A slight chance of showers and thunderstorms after 2pm. Sunny, with a high near 97. Chance of precipitation is 20%.
 - Day 7: A chance of showers and thunderstorms before 2am. Partly cloudy, with a low around 74. Chance of precipitation is 30%.

 The client lives in Raleigh, North Carolina. Could use some recommendations on garden chores today!

--------------------------------------------------------------------------------
monty (to weather-bot):

Water deeply today; it’s going to be hot. Mulch to retain moisture. Check for pests and weeds before the rain. Prepare for possible storms later in the week.

--------------------------------------------------------------------------------
Replying as weather-bot. Provide feedback to monty. Press enter to skip and use auto-reply, or type 'exit' to end the conversation: What pests are native to the region? 
weather-bot (to monty):

What pests are native to the region? 

--------------------------------------------------------------------------------
monty (to weather-bot):

In Raleigh, common pests include aphids, spider mites, whiteflies, and Japanese beetles. Check for them regularly, especially in hot weather. 

--------------------------------------------------------------------------------
Replying as weather-bot. Provide feedback to monty. Press enter to skip and use auto-reply, or type 'exit' to end the conversation: exit
```

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


