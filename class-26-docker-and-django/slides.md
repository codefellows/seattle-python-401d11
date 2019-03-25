# Why Docker is a **BIG** deal #

---

## Boss calls you in and says... ##

`We need a web app built ASAP.` 

Here are the requirements

- Ubuntu 18.04
- Python 3.6
- Postgres 9.6
- Django 2.1.7
- Pyscopg 2.7.6

`How soon can you get started?`

---

Well, let's see. 

**Ubuntu 18.0.4**

- Nope. I'm on Mac. I can install a Virtual Machine. I wonder how long that'll take.
- All the dependencies are cross platform, won't they just work the same either way?

---

**Python 3.6**
- I'm on latest, 3.7.2, but I can downgrade system wide I guess. 
- Or learn to use a tool like PyEnv to manage multiple Python installations.

---

**Postgres 9.6**
- I'm way past that version. And do you know how hard it is to uninstall Postgres???
- Won't the ORM take care of that anyway?

---

**Django 2.1.7 and Psycopg 2.7.6**

- No problem. Those are installed into virtual environment. Easy to have whatever version the project needs.

---

Boss interrupts mental math with...

`And by the way you'll have to keep up on your existing projects too and whatever versions of tools they depend upon. That's not a problem is it?`

---

I am so fired.

I can't uninstall/reinstall these tools all the time.

Wouldn't it be dreamy if system wide tools were as easy to swap out as Python packages? 

Heck, why stop there. What if we could swap entire OS? 

But that'll never happen...

---

## Interlude : Docker & Postgres ##

- Create volume to persist data

    ```mkdir -p $HOME/docker/volumes/postgres```

- Run the Postgres container

    ```docker run --rm   --name pg-docker -e POSTGRES_PASSWORD=docker -d -p 5432:5432 -v $HOME/docker/volumes/postgres:/var/lib/postgresql/data  postgres```

- Connect to Postgres

    ```psql -h localhost -p 5432 -U postgres -d postgres```

    Note: you may have port conflicts here with local Postgres installation. In that case change the first 5432 to something unused e.g. 5433. That would be the first 5432 in ```docker run``` as well as the `-p` flag to `psql`

- When done

    ```docker stop pg-docker``` 



---

Pretty awesome to get Postgres so easily. I hear it's as easy for Python and even Ubuntu.

But what if they need to all work together?

---

## Docker Compose ##

Let's 'containerize' an application with docker-compose. 

There's not *THAT* much to it. https://docs.docker.com/compose/reference/

Hmm, what application should we try out?

---

## Django - The Undisputed Heavyweight Champ ##

Just a tiny bite today. Let's get a skeleton app and poke at it