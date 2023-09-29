# fictional-character-battles

## Purpose
Add in fictional character matchups in your favorite animes. Vote on who you think will win and add in your votes. 

## How to run commands

### Docker
Touch Dockerfile
Turn on Docker Desktop --> Daemon
Build: docker image build -t character_clash .
Run: docker run -p 10000:10000 -v $(pwd)/output:/app/output character_clash




## Postgres
sudo -u postgres psql



# Tech
Flask, Jinja
Ajax --> update data 