from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

from website import create_app, db
from website.models import Pitcher

app = create_app()

with app.app_context():
    db.create_all()