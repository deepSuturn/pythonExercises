# The objective of this exercise is to display the ranking of multiple soccer teams around the world.
# The parameters is all the teams, the first five, the last four and the last.
teams = ('Manchester City', 'Real Madrid', 'Inter Milan', 'Bayern Munchen', 'Liverpool FC',
         'Bayer Leverkusen', 'Arsenal', 'RB Leipzig')


print('-='*20)
print(f'List of Soccer Clubs Ranking of World Football: {teams}')
print('-='*20)
print(f'The first five teams are: {teams[0:4]}')
print('-='*20)
print(f'The last four teams are: {teams[4:]}')
print('-='*20)
print(f'{teams[7]} is on the 8th position.')
print('-='*20)
print(f'teams in alphabetic order: {sorted(teams)}')
