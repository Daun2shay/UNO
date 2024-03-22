#Example sets of team names from 3 of the "Big 4" US sports
baseball_teams = set(['angels', 'cardinals', 'cubs', 'dodgers', 'giants', 'mets', 'rangers', 'royals', 'twins', 'yankees'])
football_teams = set(['buccaneers', 'cardinals', 'colts', 'falcons', 'giants', 'jets', 'lions', 'panthers', 'seahawks', 'vikings'])
hockey_teams = set(['blues', 'canucks', 'ducks', 'jets', 'kings', 'kraken', 'panthers', 'penguins', 'rangers', 'wild'])

#Input the type of report to generate
sport = input('Enter the sport to add a new team to (all lowercase): ')

#Depending on the sport, input the new team name
new_team_name = input('Enter a new {} team name: '.format(sport))

#Add the new team name to the appropriate set
if sport == 'baseball':
    baseball_teams.add(new_team_name)
elif sport == 'football':
    football_teams.add(new_team_name)
elif sport == 'hockey':
    hockey_teams.add(new_team_name)

#Find the common team names through code
common_teams = baseball_teams.intersection(football_teams, hockey_teams)

#Find the team names that are only team names from the selected sport
if sport == 'baseball':
    unique_teams = baseball_teams.difference(football_teams, hockey_teams)
elif sport == 'football':
    unique_teams = football_teams.difference(baseball_teams, hockey_teams)
elif sport == 'hockey':
    unique_teams = hockey_teams.difference(baseball_teams, football_teams)

#Print the results
print('Team names in common between at least two sports:', sorted(common_teams))
print('Only {} teams:'.format(sport), sorted(unique_teams))