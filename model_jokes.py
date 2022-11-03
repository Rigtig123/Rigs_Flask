import random

jokes_data = []
joke_list = [
    "Atlanta Hawks: Trae Young is entertaining enough to make State Farm Arena a destination in Atlanta, no easy feat in a notoriously fickle town.",
    "Boston Celtics: Jayson Tatum and Jaylen Borwn are both averaging close to 30 and are sharing the ball much better now",
    "Brooklin Nets: There are no injury concerns or relapses for Kevin Durant, and he signed an extension.",
    "Charlotte Hornets: The Warriors had the chance to draft LaMelo Ball but passed. ",
    "Chicago Bulls: Caruso and Ball are playing great and Demar Derozan is looking like an MVP candidate to start the season",
    "Cleveland Cavaliers: While the rest of the league goes small, the Cavs refused to be copycatters and drafted center Evan Mobley after extending center Jarrett Allen. ",
    "Dallas Mavericks: For someone who burns plenty of minutes, Luka Doncic has been spared serious injury.",
    "Denver Nuggets: Nikola Jokic apparently isn’t resting on his MVP laurels, far from it, actually.",
    "Detroit Pistons: As long as the Lions are in town, the Pistons won’t be Detroit’s bottom-feeder.",
    "Golden State Warriors: Steph Curry is currently a better version of Steph Curry.",
    "Houston Rockets: Jalen Green, every once in a while, drops hints of being special.",
    "Indiana Pacers: Seven guards were taken ahead of Chris Duarte in last summer’s Draft; good thing the Pacers were sitting pretty at 13.",
    "LA Clippers: Paul George is raising his game just when the Clippers, without Kawhi Leonard, need him to do so.",
    "LA Lakers: They already won a title with LeBron James; now they’re playing with house money. Also: Anthony Davis is upright.",
    "Memphis Grizzlies: Remind us again who was the prize of the 2019 NBA Draft? Also: For those who live in Memphis, attending a Grizzlies’ game is the best value in the NBA.",
    "Miami Heat: Nobody can find nooks and crannies in the salary cap quite like Heat capologist Andy Elisburg; that’s why Miami, year after year, finds a way to add talent.",
    "Milwaukee Bucks: Giannis didn’t leave town.",
    "Minnesota Timberwolves: Anthony Edwards is playing like an allstar and Rudy Gobert has revitalized his career",
    "New Orleans Pelicans: Number 1 picks don’t refuse rookie max contract extensions from the teams that drafted them, so there’s that regarding Zion Williamson’s future.",
    "New York Knicks: Knicks fans are still passionate about their team and willing to go over-the-top in response to the smallest signs of progress.",
    "Oklahoma City Thunder: Shai Gilgeous-Alexander is a solid building block for the future.",
    "Orlando Magic: Paolo Banchero is playing at an all star caliber level. He is the next big thing.",
    "Philadelphia 76ers: The emergence of Tyrese Maxey is clearly the best, and maybe only good thing, to happen as a result of the Ben Simmons Situation.",
    "Phoenix Suns: The hangover from losing the NBA Finals was short-lived with this team; the focus and cohesiveness seem intact.",
    "Portland Trail Blazers: Even with Damian Lillard hurt, Nurkic, Hart, Grant, and Simons, are leading them to a 5 and 2 record.",
    "Sacremento Kings: Kevin Huerter was a very good pickup and he has quitely put together a very solid start.",
    "San Antonio Spurs: Gregg Popovich is committed to see this through and evidently will leave one day on his own terms.",
    "Toronto Raptors: Those who said the Raptors were reaching when they drafted Scottie Barnes — where y’all at?.",
    "Utah Jazz: Lauri Markkanen is playing how he did during Eurobasket. They are one of the most fun teams to watch in the West.",
    "Washington Wizards: GM Tommy Sheppard dumped John Wall and Russell Westbrook and their poisonous contracts for solid players and cap flexibility.",
    
    
    
    
]

# Initialize jokes
def initJokes():
    # setup jokes into a dictionary with id, joke, haha, boohoo
    item_id = 0
    for item in joke_list:
        jokes_data.append({"id": item_id, "joke": item, "haha": 0, "boohoo": 0})
        item_id += 1
    # prime some haha responses
    for i in range(10):
        id = getRandomJoke()['id']
        addJokeHaHa(id)
    # prime some haha responses
    for i in range(5):
        id = getRandomJoke()['id']
        addJokeBooHoo(id)
        
# Return all jokes from jokes_data
def getJokes():
    return(jokes_data)

# Joke getter
def getJoke(id):
    return(jokes_data[id])

# Return random joke from jokes_data
def getRandomJoke():
    return(random.choice(jokes_data))

# Liked joke
def favoriteJoke():
    best = 0
    bestID = -1
    for joke in getJokes():
        if joke['haha'] > best:
            best = joke['haha']
            bestID = joke['id']
    return jokes_data[bestID]
    
# Jeered joke
def jeeredJoke():
    worst = 0
    worstID = -1
    for joke in getJokes():
        if joke['boohoo'] > worst:
            worst = joke['boohoo']
            worstID = joke['id']
    return jokes_data[worstID]

# Add to haha for requested id
def addJokeHaHa(id):
    jokes_data[id]['haha'] = jokes_data[id]['haha'] + 1
    return jokes_data[id]['haha']

# Add to boohoo for requested id
def addJokeBooHoo(id):
    jokes_data[id]['boohoo'] = jokes_data[id]['boohoo'] + 1
    return jokes_data[id]['boohoo']

# Pretty Print joke
def printJoke(joke):
    print(joke['id'], joke['joke'], "\n", "haha:", joke['haha'], "\n", "boohoo:", joke['boohoo'], "\n")

# Number of jokes
def countJokes():
    return len(jokes_data)

# Test Joke Model
if __name__ == "__main__": 
    initJokes()  # initialize jokes
    
    # Most likes and most jeered
    best = favoriteJoke()
    print("Most liked", best['haha'])
    printJoke(best)
    worst = jeeredJoke()
    print("Most jeered", worst['boohoo'])
    printJoke(worst)
    
    # Random joke
    print("Random joke")
    printJoke(getRandomJoke())
    
    # Count of Jokes
    print("Jokes Count: " + str(countJokes()))
