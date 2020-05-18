import os
from dotenv import load_dotenv
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Shell
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path, override=True)

from app import create_app, models, db

app = create_app()
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


def make_shell_context():
    return dict(app=app, db=db, User=models.User)


manager.add_command("shell", Shell(make_context=make_shell_context))

if __name__ == '__main__':
    manager.run()
