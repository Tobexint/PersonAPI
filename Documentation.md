## Online Setup

-WEBSITE LINK: https://txyzv.onrender.com/api

## Sample Usages

## POST

- curl -sX POST https://txyzv.onrender.com/api -H 'Content-Type:application/json' -d '{"first_name":"Mark", "last_name":"Whyte"}'
- 
- {
  "message": "Person created successfully"
  }

## GET

- curl https://txyzv.onrender.com/api

[
  {
    "first_name": "Tony",
    "last_name": "Wilson"
  },
  
  {
    "first_name": "Mark",
    "last_name": "Essien"
  },
  
  {
    "first_name": "Mark",
    "last_name": "Whyte"
  }
]

- curl https://txyzv.onrender.com/api/1

{
  "first_name": "Tony",
  "id": 1,
  "last_name": "Wilson"
}

## Standard formats for requests

- GET: curl -sL http://127.0.0.1:5000

- GET: curl -sL http://127.0.0.1:5000/api

- POST: curl -sX POST http://127.0.0.1:5000/persons -H 'Content-Type:application/json' -d '{"first_name":"u", "last_name":"o"}'

- PUT:
       curl -X PUT \
                  -H 'Content-Type:application/json' \
                  -d '{"first_name":"Sarah", "last_name":"Ahmed"}' \
                  http://127.0.0.1:5000/api/5

- DELETE: curl -sX DELETE http://127.0.0.1:5000/api/2

## Standard format for responses

-GET:     {
            "first_name": "",
            "last_name": ""
          }

-POST:    {
           "message": "Person created successfully"
          }

-PUT:     {
            "message": "Person updated successfully"
          }

-DELETE:  {
            "message": "Person deleted successfully"
          }

## Sample API Usage including example requests and responses

-GET REQUEST: curl http://127.0.0.1:5000/persons

-GET RESPONSE:  
[
  {
    "first_name": "Mark",
    "last_name": "Essien"
  },
  
  {
    "first_name": "Emmanuel",
    "last_name": "Essien"
  },
  {
    "first_name": "Emmanuel",
    "last_name": "White"
  },
  {
    "first_name": "Mark",
    "last_name": "Wilson"
  },
  {
    "first_name": "Sarah",
    "last_name": "Antwi"
  }
]

-POST REQUEST:  $ curl -sX POST http://127.0.0.1:5000/persons -H 'Content-Type:application/json' -d '{"first_name":"Emmanuel", "last_name":"White"}'

-POST RESPONSE:  
{
  "message": "Person created successfully"
}

-PUT REQUEST:   
>            $ curl -X PUT \
>           -H 'Content-Type: application/json' \
>           -d '{"first_name":"Sarah", "last_name":"Ahmed"}' \
>           http://127.0.0.1:5000/persons/5

-PUT RESPONSE:   
{
  "message": "Person updated successfully"
}

-DELETE REQUEST: $ curl -sX DELETE  http://127.0.0.1:5000/persons/5

-DELETE RESPONSE: {
                     "message": "Person deleted successfully"
                  }

## Setup on local terminal
- Python app.py

## Limitations
- I was unable to host my initial database of choice(sqlite) and had to switch to postgresql.
