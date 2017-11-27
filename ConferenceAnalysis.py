import pandas as pd
import matplotlib.pyplot as plt
from collections import namedtuple

Record = namedtuple('Record', ['Wins', 'Losses'])

NBArecords = {
	# Note these are records as of 11/27/17 @ 2:00PM PST
    'Eastern': {
        'BOS': Record(18, 3),
        'DET': Record(12, 6),
        'CLE': Record(12, 7),
        'TOR': Record(12, 7),
	    'PHI': Record(11, 7),
	    'IND': Record(11, 9),
	    'WSH': Record(10, 9),
	    'MIA': Record(10, 9),
	    'NY': Record(10, 9),
	    'MIL': Record(9, 9),
	    'CHA': Record(8, 11),
	    'ORL': Record(8, 12),
	    'BKN': Record(7, 12),
	    'ATL': Record(4, 16),
	    'CHI': Record(3, 15),
    },
    'Western': {
        'HOU': Record(15, 4),
        'GS': Record(15, 5),
        'SA': Record(12, 7),
        'MIN': Record(12, 8),
	    'POR': Record(12, 8),
	    'DEN': Record(11, 8),
	    'NO': Record(11, 9),
	    'UTAH': Record(9, 11),
	    'LAL': Record(8, 11),
	    'OKC': Record(8, 11),
	    'LAC': Record(7, 11),
	    'MEM': Record(7, 12),
	    'PHX': Record(7, 14),
	    'SAC': Record(5, 14),
	    'DAL': Record(5, 15),
    }
}


def dataframe(conferenceStr):
	conferenceDict = NBArecords[conferenceStr]
	conferenceDf = pd.DataFrame.from_dict(conferenceDict, orient='index')
	conferenceDf['PCT'] = round(conferenceDf['Wins'] / conferenceDf.sum(axis=1), 3)

	return conferenceDf


eastdf = dataframe('Eastern')
westdf = dataframe('Western')

# eastdf['PCT'].plot(kind='hist', color='green', bins=20, alpha=0.4, )

# westdf['PCT'].plot(kind='hist', color='red', bins=20, alpha=0.4)

# set up figure & axes
fig, axes = plt.subplots(nrows=1, ncols=1, sharex=True, sharey=True)

# drop sharex, sharey, layout & add ax=axes
eastdf.hist(column='PCT', ax=axes)

# set title and axis labels
plt.suptitle('NBA W/L Distributions by Conference', x=0.5, y=1.5, ha='center', fontsize='xx-large')
fig.text(0.5, 0.04, 'W/L Percentage', ha='center')
fig.text(0.04, 0.5, '# of teams', va='center', rotation='vertical')

plt.show()
