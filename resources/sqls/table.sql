CREATE TABLE IF NOT EXISTS users (
    id           INTEGER PRIMARY KEY,
    telegram_id  INTEGER NOT     NULL,
    balance      INTEGER DEFAULT 1000,
    bank_balance INTEGER DEFAULT 100,
    level        INTEGER DEFAULT 1,
    exp          INTEGER DEFAULT 0,
    time         INTEGER NOT     NULL,
    bonus_time   INTEGER NOT     NULL
)
