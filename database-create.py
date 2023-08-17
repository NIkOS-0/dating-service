import sqlite3

# Создание и подключение к базе данных
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Выполнение первого SQL-запроса
cursor.execute('''
CREATE TABLE users (
    users_id              INTEGER         PRIMARY KEY AUTOINCREMENT,
    id_tg                 BIGINT,
    id_vk                 BIGINT,
    phone                 VARCHAR (30),
    lang                  VARCHAR (2)     DEFAULT 'ru',
    lang_code             VARCHAR (2),
    age                   INTEGER,
    male                  VARCHAR (1),
    love                  VARCHAR (1),
    min_age               INTEGER,
    max_age               INTEGER,
    name                  VARCHAR (50),
    description           TEXT,
    photo1                VARCHAR (150),
    photo2                VARCHAR (150),
    photo3                VARCHAR (150),
    video                 VARCHAR (150),
    instagram             VARCHAR (150),
    reg                   BOOLEAN         DEFAULT (0),
    long                  DECIMAL (5, 50),
    lat                   DECIMAL (5, 50),
    ind                   INT             DEFAULT (0) NOT NULL,
    is_search             BOOLEAN         NOT NULL DEFAULT (True),
    count_of_send_message INTEGER         DEFAULT (0)
);
''')

# Выполнение второго SQL-запроса
cursor.execute('''
CREATE TABLE love (
    love_id         INTEGER       PRIMARY KEY,
    from_user       BIGINT,
    to_user         BIGINT,
    from_username   VARCHAR (150),
    from_male       VARCHAR (1),
    from_phone      VARCHAR (20),
    from_first_name VARCHAR (150),
    text            TEXT,
    video           VARCHAR (150),
    photo           VARCHAR (150),
    active          BOOLEAN       DEFAULT (1) NOT NULL
);
''')

# Выполнение третьего SQL-запроса
cursor.execute('''
CREATE TABLE complaint (
    complaint_id INTEGER      PRIMARY KEY,
    from_user    BIGINT,
    to_user      BIGINT,
    type         VARCHAR (50)
);
''')

# Выполнение четвертого SQL-запроса
cursor.execute('''
CREATE TABLE referrals (
    referrals_id INTEGER   PRIMARY KEY AUTOINCREMENT,
    tg_id        BIGINT,
    date_created DATETIME,
    users_id     INTEREGER REFERENCES users (users_id)
);
''')

# Сохранение изменений и закрытие соединения
conn.commit()
conn.close()

print("База данных успешно создана.")
