# Task 1 Backend

### 1. Post Request to Register User.
![1](https://github.com/Grg-Sid/FunnelHQ-Task-Backend/assets/106266279/af4c6972-5290-44f3-a315-affc2133a3ea)

### 2. Post Request to Login User.
![2](https://github.com/Grg-Sid/FunnelHQ-Task-Backend/assets/106266279/cb4cf3b6-594b-4a4e-b3ec-21d0d4b8b36b)

## Protected Endpoints

### 3. Get Request to Test Token Validity.
![5](https://github.com/Grg-Sid/FunnelHQ-Task-Backend/assets/106266279/50ddc728-41fb-4d8c-98fa-e6205ee9bb68)

### 4. Post Request to Create User Profile.
  #### UnAuthenticated User
  ![3](https://github.com/Grg-Sid/FunnelHQ-Task-Backend/assets/106266279/42d56423-8211-45bc-9ab1-22d1fc6d005e)

  #### Authenticated User
  ![4](https://github.com/Grg-Sid/FunnelHQ-Task-Backend/assets/106266279/f835f178-d68c-4215-8dea-fdb94d5f10a4)

### 5. Get Request to Recommend Books.
![6](https://github.com/Grg-Sid/FunnelHQ-Task-Backend/assets/106266279/743e86f4-db29-4b5f-8670-46c58382f32c)
## Setting Up

- Clone the repositiory
- Create a python virtual environment and activate it
  <br>
  ```shell
  python3 -m venv .venv
  source .venv/bin/activate
  ```
- Give write access to the setup.sh file
  <br>
  ```shell
  chmod +x setup.sh
  ```
- Run setup.sh to install the required packages and set the appropriate paths
  <br>
  ```shell
  ./setup.sh
  ```

- Run the migrate command
  ```shell
  python manage.py migrate
  ```

- Run the backend server on localhost:

  ```shell
  python manage.py runserver
  ```

You can access the endpoints from your web browser following this url

```url
http://127.0.0.1:8000
```

## Make Sure to create a .env file and provie valid OPENAI API KEY.
