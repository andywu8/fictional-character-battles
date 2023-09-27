DROP TABLE IF EXISTS records;

create table records (
    id SERIAL PRIMARY KEY,
    character_1 text not null, 
    character_2 text not null, 
    character_1_votes int not null,
    character_2_votes int not null,
    anime_name text not null, 
    user_who_uploaded text not null,
    uploaded_timestamp TIMESTAMP  DEFAULT CURRENT_TIMESTAMP NOT NULL
);

DROP TABLE IF EXISTS user_vote;
create table user_vote (
    id PRIMARY KEY,
    user_email text not null,
    uploaded_timestamp TIMESTAMP  DEFAULT CURRENT_TIMESTAMP NOT NULL,
    record_id int,
    FOREIGN KEY (record_id) REFERENCES records(id)
);

DROP TABLE IF EXISTS comments;
create table comments (
    comment_id SERIAL PRIMARY KEY,
    user_email text not null,
    comment text not null,
    uploaded_timestamp TIMESTAMP  DEFAULT CURRENT_TIMESTAMP NOT NULL,
    record_id int, 
    FOREIGN KEY (record_id) REFERENCES records(id)
);