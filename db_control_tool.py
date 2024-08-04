def create_delayed_post(date, media):
    import sqlite3
    from pickle import dumps

    db = sqlite3.connect("../database/delayed_posts.sqlite3")
    c = db.cursor()

    serialized_date = dumps(date)
    serialized_media = dumps(media)

    c.execute("INSERT INTO delayed_posts (date, media) VALUES (?, ?)", (serialized_date, serialized_media))

    db.commit()
    db.close()

    return "status code [200]"


def get_delayed_post(date):
    import sqlite3
    from pickle import dumps

    db = sqlite3.connect("../database/delayed_posts.sqlite3")
    c = db.cursor()

    c.execute("SELECT * FROM users WHERE date = ?", (dumps(date)))
    result = c.fetchone()

    return result
