# Dates of significant public transport events:

- 2009 - 2011 Circle line begins development
  - large uptick in MRT ridership from 2009 - 2010

- 2012 Bus Service Enhancement Program
  - large uptick in Bus usage between 2012 to 2020

- 2013 - 2017 Downtown line opens in 3 stages

- 2016 LTA takes more control over bus planning and contracts
  - minor changes in usage from 2016 to 2017, growth happens in 2017 through 2020

- 2017 Tuas west MRT extension
  - not much growth in 2016 to 2017 as compared to 2017-2018, suggesting that the completion in

- 2020 Thomson-East Coast Line opens in stages
  - any uptick in usage overshadowed by COVID

- 2024 Thomson-East Cost Line stages
  - not very much growth in MRT usuage compared to years before COVID
  - connects east coast of Singapore to Central (Orchard) and West/North West Singapore (Woodlands), with central Singapore being a large tourist location

- 2026 Circle Line gets completed


# Linear Regression notes:

- While there is an upward trend for most ridership charts, they are all slightly inaccurate due to Covid-19 completely stopping tourist arrivals and keeping Singapore in lockdown
- While not reflected in the linear regression by year model, the MRT saw a significant bounce back in usage after covid.
- small bumps in usage around the third to fourth quarter of the year in MRT and bus usage, which is in line with the F1 race in Singapore, suggesting that the amount of arrivals coming into Singapore do affect the usage and efficiency of the MRT system.
	- Interesting to note: from the daily MRT usage, there are small dips in the graph in the December period of each year, going from ~3.5 million riders in mid 2023 to 3 million in December 2023 before shooting back up to 3.5 million come January. This suggests that the amount of departures in Singapore has significant effect on the public transport usage in the same way that arrivals affect ridership. This effect is also seen on the bus daily usage graph.

# Taxi Availability notes:
- significant differences in amount of Taxis available on national day compared to one week after
	- throughout National Day, there were a minimum of 1300 taxis available throughout the day compared to August 15th, which didn't break 500 until evening.

# Tasks to be completed:

- set up tracker to get data on taxi availability for F1 2026 (October 9 - 12)
- create linear regression/Time series models for Taxi availability CSV files (DONE)
- search for data on Singapore departures

# Inspiration:

Working in the Public Transport Security division of the SPF, I had always heard stories from other officers about the increased demands and stress that came with patrolling during public holidays or international events such as Singapore National Day or the F1 races that are held in Singapore.

My first deployment was the 2025 F1 race held in October, and I was directly involved with allocating the manpower needs for the 3 days of patrol; helping out with the planning of such a large deployment and seeing the efficiency of not only the officers but Singapore's public transport infrastructure inspired me to use one of my hobbies, math, to study the relationship between the public transport system and external factors such as these big events.

Through this trial, I learned a lot about different quantitative analysis methods, such as time series analysis and using linear regression models in real data, and also how to use python to convert csv files into readable graphs and pull data from API endpoints, allowing for analysis on datasets that aren't already published.

I also was able to get some insights into how Singapore is able to self optimize its public transport system, also while seeing the how the improvements Singapore made to its infrastructure affected its usage over time.
