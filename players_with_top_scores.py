# Author: Apache X692 Attack Helicopter
# Created on: 29/06/2024
players_with_score = {
    "Homelander": 120,
    "Starlight": 50,
    "Butcher": 85,
    "A-Train": 100,
    "Black Noir": 90,
    "Queen Maeve": 95,
    "Stormfront": 110,
    "Kimiko": 80,
    "Frenchie": 70,
    "Hughie": 60,
    "Deep": 75,
    "Ashley": 65,
    "Stan Edgar": 105,
    "Victoria Neuman": 115,
    "Lamplighter": 55
}

high_scores = sorted(players_with_score.items(), key=lambda x: x[1],
reverse=True)
top_scorers = []

for player, score in high_scores[:10]:
    top_scorers.append((player, score))

print(top_scorers)
