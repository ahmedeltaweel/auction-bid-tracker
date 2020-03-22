Auction Bid Tracker
======

API derived Flask app that tracks Auction Bids on items.

This simple projects exposes 4 APIs to do the following:
- record a user’s bid on an item.
- get the current winning bid for an item.
- get all the bids for an item.
- get all the items on which a user has bid.

Currently, it's a very naive solution.

Downsides to tackle:
- Concurrent realtime bid tracking for all users
    - Suggested solution using [WebSocket Protocol](https://en.wikipedia.org/wiki/WebSocket) and broadcast the changes in realtime.
- DBMS to handle structured data [PostgreSQL](http://postgresql.org)
    - Table for users.
    - Table to items.
    - Table for bids with foreign key to user and item.
- Performance Cautions:
    - Handle N+1 queries for Bids by using DB JOINS.

## TODO
-----------

- Use actual DB engine instead of current on memory one.
- Write unit tests to each component.
- Write integration tests for APIs.
- Secure APIs.
- Enhance matching, adding and comparing bids, currently it's very naive.
- Add [Pre-commit](https://github.com/pre-commit/pre-commit) to the application repo to maintain the structure and code style.
- If needed containerizing the application using [Docker](https://docker.com).


## Development
-----------

Development is running using on bar metal.

The following details how to run this application (locally).

To build:

```sh
$ virtualenv -p python3 venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python3 main.py
```

You can now access on <http://0.0.0.0:8989/>
