## Objectives

- Build a simple REST API capable of CRUD operations on a "person" resource, interfacing with any database of your choice.

- API should dynamically handle parameters such as adding or retrieving a person by name.

- Host your entire project on GitHub, provide a well-structured documentation in the repository that outlines request/response formats, setup instructions, and sample API usage.

## REST API Development: Develop an API with endpoints for:

- CREATE: Adding a new person. => /api

- READ: Fetching details of a person. => /api/user_id

- UPDATE: Modifying details of an existing person => /api/user_id

- DELETE: Removing a person => /api/user_id

- Ensure all interactions with the database are secure and free from common vulnerabilities (e.g., SQL Injections).

## Database Modelling:(Bonus)

- UML Diagram: Design and present a UML(Unified Modeling Language) diagram that represents the structure and relationships of your API's classes and models.

##  Testing

- Using tools like Postman or (scripts written in Python using the requests library) that tests each CRUD operation in your API.

- This should:

- Add a new person (e.g., "Mark Essien").

- Fetch details of a person

- Modify the details of an existing person

- Remove a person

## Dynamic Parameter Handling:

- Your API should be flexible enough to handle dynamic input. If we provide a name( or other details), your backend should be able to process operations using that name.

- Example: If we pass "Mark Essien", we should be able to perform all CRUD operations on "Mark Essien"

- Add validation- field should only be strings; integers or any other data type should not be allowed.
