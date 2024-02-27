class Borda:
  """
  Classe pour implémenter la méthode de Borda.
  https://fr.wikipedia.org/wiki/M%C3%A9thode_Borda

  Args:
    projects: La liste des projets soumis au vote.
  """

  def __init__(self, projects):
    self.projects = projects
    self.scores = {}

  def calculate_scores(self, votes):
    """
    Calcule le score de Borda pour chaque projet.

    Args:
      votes: Une liste de listes contenant les votes des membres du groupe.

    Returns:
      Un dictionnaire avec les scores de Borda pour chaque projet.
    """

    for vote in votes:
      for i, project in enumerate(vote):
        if project not in self.scores:
          self.scores[project] = 0
        self.scores[project] += len(vote) - i - 1

  def get_winner(self):
    """
    Retourne le projet avec le score de Borda le plus élevé.

    Returns:
      Le projet gagnant.
    """

    winner = None
    max_score = -float("inf")
    for project, score in self.scores.items():
      if score > max_score:
        max_score = score
        winner = project

    return winner

# Place aux votes
projects = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]

projects_name = {
  "A": "Accidents routiers en France",
  "B": "Blood cells classification",
  "C": "Classification de produits e-commerce Rakuten",
  "D": "Emission de CO2 par les véhicules",
  "E": "Prévision météo en Australie",
  "F": "Reconnaissance de champignons",
  "G": "Reconnaissance de plantes",
  "H": "Supply Chain - Satisfaction des clients",
  "I": "Temps de Réponse de la Brigade des Pompiers de Londres",
}

borda = Borda(projects)

votes = [
  ["A", "B", "C", "D", "E", "F", "G", "H", "I"], # Heuzef - @heuzef
  ["A", "B", "C", "D", "E", "F", "G", "H", "I"], # Yvan
  ["A", "B", "C", "D", "E", "F", "G", "H", "I"], # Viktoriia
  ["A", "B", "C", "D", "E", "F", "G", "H", "I"], # Florent - @FConstantMovework
]

borda.calculate_scores(votes)

winner = borda.get_winner()

print(f"""
Rires et roulements de tambour ... Le suspense est à son comble ...
Après un vote palpitant, c'est avec une immense joie que nous vous annonçons le grand gagnant :

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
LE PROJET {winner} : {projects_name[winner]} !!!
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Applaudissements nourris et cris de joie s'il vous plaît !
N'oubliez pas, il n'y a pas de perdants aujourd'hui, seulement des participants formidables !
Merci à tous d'avoir participé à ce vote !
""")