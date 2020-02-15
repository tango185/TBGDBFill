# TBGDBFill

## Overview
TBGDBFill is a standalone program intended for adding cards to the MySQL database "tbgcalc". The purpose of the
"tbgcalc" database is for use with the TBGCalc program. There are tables setup for the Royal Rumble, Vanguard, Primal,
and Nightmare tiers.

## Card Input

### POW/TGH/SPD/CHA

All records are explicitly level 100 base stats for Power (POW), Toughness (TGH), Speed (SPD), and Charisma (CHA). Fewer
than 25 matches can be played on the card for the base stats to remain intact.

### Abilities

While the specific ability stats (POW, TGH, SPD, CHA) need to be selected upon input, the base amount that those stats
are increased when the ability activates is based on the tier of the card, not its level. Therefore, TBGDBFill will only
update the "tbgcalc" database with which stats are affected, not the amount. Fewer than 25 matches can be played on the
card in order to not impact the ability increase.

### Required Inputs

All inputs are required for successful addition into "tbgcalc" database. Required inputs are:
1. Tier
2. Name
3. Gender
4. POW
5. TGH
6. SPD
7. CHA
8. First and second Ability stats
9. Arrow

#### Naming Convention

Normal tier card names should include only the name on the card (i.e. AJ Styles). If the card name includes quotation
marks, use single quotes (i.e. Bret 'Hit Man' Hart). If the card is an special event card, include the event in
parentheses following the name (i.e. AJ Styles (Extreme)).

#### Numerical Inputs

Stat amounts must include numerical values only. Do not include commas to separate values in groups of three.