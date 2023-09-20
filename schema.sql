DROP TABLE IF EXISTS records;

create table records (
    id integer primary key autoincrement,
    character_1 text not null, 
    character_2 text not null, 
    character_1_votes int not null,
    character_2_votes int not null,
    user_who_uploaded email not null,
    uploaded_timestamp TIMESTAMP  DEFAULT CURRENT_TIMESTAMP NOT NULL
);



DROP TABLE IF EXISTS user_vote;
create table user_vote (
    id integer primary key autoincrement,
    user_email email not null,
    uploaded_timestamp TIMESTAMP  DEFAULT CURRENT_TIMESTAMP NOT NULL,
    record_id int,
    FOREIGN KEY (record_id) REFERENCES records(id)
);