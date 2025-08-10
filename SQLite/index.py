import json
from pathlib import Path
movies = [
    {"id": 1, "title": "terminator", "ratings": 9},

]
# data = json.dumps(movies)
data = Path("SQLite/movies.json").read_text()
movies = json.loads(data)
print(movies[0])


