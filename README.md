# TBGDBFill

## Overview
TBGDBFill is a program intended for adding cards to the MySQL database "tbgcalc". The purpose of the "tbgcalc" database
is for use with the TBGCalc program which will be completed at a later date.

### Database and Tables
As of this point the "tbgcalc" database only has one table "card" which stores all card information regardless of tier.
If processing of information becomes a burden at any point due to the size of the database, the "card" table may be
split into separate tables for each tier.

## Instructions
TBGDBFill has two functions:
1. Check if a card already exists in the "tbgcalc" database
2. If a card doesn't exist in the "tbgcalc" database, add the card to the database

These functions are performed based on which information is given in the form.

### Check if Card Exists
To check if a card already exists in the "tbgcalc" database, only the TIER and NAME fields need to be filled in.
Performing this function isn't required to add a new card because this function is also run simultaneously to the adding
function. The purpose of only requiring the TIER and NAME fields to be filled in is to save the user time from filling
in POW/TGH/SPD/CHA numbers only to find out the card already exists. When performing this function, a window will appear
notifying the user of the result of the database check.

### Add Card
To add a card to the "tbgcalc" database, all information must be filled in. If any information is missing, an
appropriate warning message will notify the user of the error. When all information is filled in, TBGDBFill will check
if the card already exists and, if it does not, will add the card to the database. Unlike when this check is performed
as described above, if the card doesn't exist already there will be no notification to the user.

### Regarding Card Level & Matches Played

All records are explicitly level 100 base stats for Power (POW), Toughness (TGH), Speed (SPD), and Charisma (CHA). Fewer
than 25 matches can be played on the card for the base stats to remain intact.

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