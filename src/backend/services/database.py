<<<<<<< HEAD
from sqlalchemy import create_engine, and_
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from utils.config import get_config

db_params = f"mysql+pymysql://{get_config('db.user')}:{get_config('db.password')}\
    @{get_config('db.host')}:{get_config('db.port')}/crowdlabel?charset=utf8"

engine = create_engine(db_params)
def init_db():
    Base.metadata.create_all(engine)


def drop_db():
    Base.metadata.drop_all(engine)


if __name__ == '__main__':
    drop_db()
    init_db()
=======
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from models.basicbase import Base
from models.child_results import ChildResults
from models.email import Email
from models.question import Question
from models.results import Results
from models.task import Task
from models.user import User
import asyncio
#from utils.config import get_config

db_params = f"sqlite+aiosqlite:///crowdlabel.db"

engine = create_async_engine(db_params)
async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


if __name__ == '__main__':
    asyncio.run(init_models())

>>>>>>> dev
