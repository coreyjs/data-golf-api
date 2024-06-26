[![Data-Golf-API](https://github.com/coreyjs/data-golf-api/actions/workflows/python-app.yml/badge.svg)](https://github.com/coreyjs/data-golf-api/actions/workflows/python-app.yml)
[![PyPI version](https://badge.fury.io/py/data_golf.svg)](https://badge.fury.io/py/data_golf)


# Data Golf API (Unofficial)

### An Unofficial API Library for DataGolf.com APIs

This is a Python library for interacting with the DataGolf APIs. DataGolf is a golf analytics platform that provides a wide range of data and analytics for golf tournaments, players, and courses.

**This is an unofficial API lib, and it is not affiliated with DataGolf in any way.**


This is being built to support some ML projects I am working on.  I will be 
continuing to add more endpoints as I need them.  If you have a specific endpoint you need, please open a ticket for submit a PR.

---
## Developer Note:
This is in development.  Code structure will change as I get
all the endpoints added.  So expect some renaming and convention changes.

### Contact
Im available on [Bluesky](https://bsky.app/profile/coreyjs.dev) for any questions or just general chats about enhancements.

---
# Usage + Installation & Setup
(Currently this only supports JSON formats, CSV is on the roadmap)

```python
pip install data_golf
```

```python
from data_golf import DataGolfClient

client = DataGolfClient(api_key="YOUR_API_KEY")

# For more request logging
client = DataGolfClient(api_key="YOUR_API_KEY", verbose=True)
```

---

# Main Modules

These modules map directly to the [DataGolf API Documentation](https://datagolf.com/api-access) available on their site:

1. General
2. Predictions
3. Live Predictions

The Data Golf API is a paid service via [DataGolf.com](https://datagolf.com/api-access), there they will provide you with an API Key.  This library is
only a helper utility, to make interacting and consuming the API easier.

---

# General APIs

### Player List

<details>
    <summary>API Endpoint Info</summary>

**Endpoint:** `/get-player-list`  
**Method:** GET  
**Formats:** JSON

</details>

```python
players = client.general.player_list()
```


### Current Season Tour Schedule

<details>
    <summary>API Endpoint Info</summary>

**Endpoint:** `/get-schedule`  
**Method:** GET  
**Formats:** JSON

| Param | Type   | Ex                                                                        |
|-------|--------|---------------------------------------------------------------------------|
| tour  | str    | all, pga, euro, kft, alt, liv |

</details>

```python
# Can use optinal parameter 'tour' to filter by tour: pga, euro, kft, alt, liv
tour_schedule = client.general.tour_schedule()
tour_schedule = client.general.tour_schedule(tour="pga")
tour_schedule = client.general.tour_schedule(tour="liv")
```

### Field Updates

<details>
    <summary>API Endpoint Info</summary>

**Endpoint:** `/field-updates`  
**Method:** GET  
**Formats:** JSON

| Param | Type   | Ex                                                                        |
|-------|--------|---------------------------------------------------------------------------|
| tour  | str    | all, pga, euro, kft, alt, liv |

</details>

```python
# tour = pga (default), euro, kft, opp, alt
rsp = client.general.field_updates() # defaults to pga
rsp = client.general.field_updates(tour="kft")
```

---

# Model Prediction APIs

## Rankings

<details>
    <summary>API Endpoint Info</summary>


**Endpoint:** `/preds/get-dg-rankings`  
**Method:** GET  
**Formats:** JSON

</details>

```python
rankings = client.predictions.rankings()
```

## Pre Tournament Predictions

<details>
    <summary>API Endpoint Info</summary>

**Endpoint:** `/preds/pre-tournament`  
**Method:** GET  
**Formats:** JSON

</details>

```python
rsp = client.predictions.pre_tournament()

rsp = client.predictions.pre_tournament(
    tour='pga',
    dead_heat=True,
    odds_format='american'
)
```

## Pre Tournament Prediction Archive

<details>
    <summary>API Endpoint Info</summary>

**Endpoint:** `/preds/pre-tournament-archive`  
**Method:** GET  
**Formats:** JSON

</details>

```python
# Supports optional parameters event_id:, year:, odds_format:
rsp = client.predictions.pre_tournament_pred_archive()

rsp = client.predictions.pre_tournament_pred_archive(
    year=2021,
)
```

## Player Skill Decomposition

<details>
    <summary>API Endpoint Info</summary>

**Endpoint:** `/preds/player-decompositions`  
**Method:** GET  
**Formats:** JSON

</details>

```python
# Supports optional parameters tour:
rsp = client.predictions.player_skill_decompositions()
rsp = client.predictions.player_skill_decompositions(tour='alt')
```

## Player Skill Ratings

<details>
    <summary>API Endpoint Info</summary>

**Endpoint:** `/preds/skill-ratings`  
**Method:** GET  
**Formats:** JSON

</details>

```python
# Supports optional param display: (value, rank)
rsp = client.predictions.player_skill_ratings()
rsp = client.predictions.player_skill_ratings(display="rank")
```

## Detailed Approach Skill

<details>
    <summary>API Endpoint Info</summary>

**Endpoint:** `/preds/approach-skill`  
**Method:** GET  
**Formats:** JSON

| Param  | Type   | Ex                                                                        |
|--------|--------|---------------------------------------------------------------------------|
| period | str    | l24 (last 24 months) (default), <br/> l12 (last 12 months), ytd (year to date) |

</details>

```python
rsp = client.predictions.detailed_approach_skill()
rsp = client.predictions.detailed_approach_skill(period='ytd')
```

## Fantasy Projections
<details>
    <summary>API Endpoint Info</summary>


**Endpoint:** `/preds/fantasy-projection-defaults`  
**Method:** GET  
**Formats:** JSON

| Param | Type | Ex                                                            |
|-------|-----|---------------------------------------------------------------|
| tour  | str | pga (default), euro, opp (opposite field PGA TOUR event), alt |
| site  | str |  draftkings (default), fanduel, yahoo  |
| slate | str | main (default), showdown, showdown_late, weekend, captain |

</details>

```python
rsp = client.predictions.fantasy_projection()
rsp = client.predictions.fantasy_projection(tour='pga', site='fanduel', slate='showdown')
```

---

# Live Predictions


### Live Model Predictions

<details>
    <summary>API Endpoint Info</summary>


**Endpoint:** `/preds/in-play`  
**Method:** GET  
**Formats:** JSON

| Param       | Type | Ex                                                            |
|-------------|------|---------------------------------------------------------------|
| tour        | str  | pga (default), euro, opp (opposite field PGA TOUR event), alt |
| dead_head   | bool | False (default), True                                         |
| odds_format | str  | percent (default), american, decimal, fraction                                                             |

</details>

```python
data = dg.live_predictions.live_in_play()
data = dg.live_predictions.live_in_play(tour='kft', odds_format='american')
```


### Live Tournament Stats

Returns live strokes-gained and traditional stats for every player during PGA Tour tournaments.


<details>
    <summary>API Endpoint Info</summary>


**Endpoint:** `/preds/live-tournament-stats`  
**Method:** GET  
**Formats:** JSON

| Param   | Type    | Ex                                                            |
|---------|---------|---------------------------------------------------------------|
| stats   | csv str | Comma-separated list of statistics to be returned. Supports: sg_putt, sg_arg, sg_app, sg_ott, sg_t2g, sg_bs, sg_total, <br/>distance, accuracy, gir, prox_fw, prox_rgh, scrambling |
| round   | str     | event_avg, 1, 2, 3, 4                                       |
| display | str     | value (default), rank                |

</details>

```python
data = dg.live_predictions.live_tournament_stats()
data = dg.live_predictions.live_tournament_stats(stats="sq_arg, sg_bs", disppaly="rank")
```


### Live Hole Scoring Distruibution

Returns live hole scoring averages and distrubutions (birdies, pars, bogeys, etc.) broken down by tee time wave.


<details>
    <summary>API Endpoint Info</summary>


**Endpoint:** `/preds/live-hole-stats`  
**Method:** GET  
**Formats:** JSON

| Param   | Type | Ex                                                           |
|---------|------|--------------------------------------------------------------|
| tour    | str  |  pga (default), euro, opp (opposite field PGA TOUR event), kft, alt |
| round   | str  | event_avg, 1, 2, 3, 4                                      |
| display | str  | value (default), rank               |

</details>

```python
data = dg.live_predictions.live_hole_stats()
data = dg.live_predictions.live_hole_stats(tour='kft')
```


---

# Betting

### Outright Odds

Returns the most recent win, top 5, top 10, top 20, make/miss cut, and
         first round leader odds offered at 11 sportsbooks alongside the corresponding
          predictions from the DG model.

<details>
    <summary>API Endpoint Info</summary>


**Endpoint:** `/betting-tools/outrights`  
**Method:** GET  
**Formats:** JSON

| Param   | Type | Ex                                                           |
|---------|------|--------------------------------------------------------------|
| tour    | (str, optional)  |  pga (default), euro, opp (opposite field PGA TOUR event), kft, alt |
| market  | (str, required)  | Specifies the match-up market. Supports values: win, top_5, top_10, top_20, mc, make_cut, frl                                     |
| odds_format | (str, optional)   |  Specifies the odds format. Supports values: percent, american, decimal (default), fraction               |

</details>

```python
data = dg.betting.outright_odds(market='win')
data = dg.betting.outright_odds(market='top_5', tour='euro')
```


### Matchup Odds


Returns the most recent tournament match-up, round match-up, and 3-ball odds offered at 8
            sportsbooks alongside the corresponding prediction from our model.

<details>
    <summary>API Endpoint Info</summary>


**Endpoint:** `/betting-tools/matchups`  
**Method:** GET  
**Formats:** JSON

| Param   | Type | Ex                                                           |
|---------|------|--------------------------------------------------------------|
| tour    | (str, optional)  |  pga (default), euro, opp (opposite field PGA TOUR event), kft, alt |
| market  | (str, required)  | Specifies the match-up market. Supports values: tournament_matchups, round_matchups, 3_balls                                     |
| odds_format | (str, optional)   |  Specifies the odds format. Supports values: percent, american, decimal (default), fraction               |

</details>

```python
data = dg.betting.matchup_odds(market='tournament_matchups')
data = dg.betting.matchup_odds(market='3_balls', tour='euro')
```

### Matchup Odds - All Pairings


Returns Data Golf matchup / 3-ball odds for every pairing in the next round of
            current PGA Tour and European Tour events.

<details>
    <summary>API Endpoint Info</summary>


**Endpoint:** `/betting-tools/matchups-all-pairings`  
**Method:** GET  
**Formats:** JSON

| Param   | Type | Ex                                                           |
|---------|------|--------------------------------------------------------------|
| tour    | (str, optional)  |  pga (default), euro, opp (opposite field PGA TOUR event), kft, alt |
| odds_format | (str, optional)   |  Specifies the odds format. Supports values: percent, american, decimal (default), fraction               |

</details>

```python
data = dg.betting.matchup_odds_all_pairings(tour='pga')
data = dg.betting.matchup_odds_all_pairings(tour='euro', odds_format='american')
```


