
from isso import config
from isso.db import SQLite3
from isso.migrate import Generic
from pathlib import Path

dbpath = "/Users/zrong/works/mysite/test.db"
conf = config.new({
    "general": {
        "dbpath": dbpath,
        "max-age": "1h"
    }
})

def test_generic():
    print(Path(__file__).resolve())
    # filepath = Path(__file__).parent.joinpath('isso', 'tests', 'generic.json')
    filepath = Path(__file__).parent.joinpath('generic.json')

    db = SQLite3(dbpath, conf)
    Generic(db, filepath).migrate()

if __name__ == "__main__":
    test_generic()