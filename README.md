# sam_api
Please follow the readme file.

Get into the folder <b>sam_api</b>

<h3>Install requirements.txt by the command:</h3>

pip install -r requirements.txt


<h4><b>Run the command: </b></h4>

 uvicorn capitals:app --reload

<i>this will start the local server <i>



<h2>Swagger Docs</h2>
localhost/docs

Hit the GET api, gives you the random country
Guess the capital via the POST api, gives you the result if its correct or returns with the correct capital.


<h2>Via Curl</h2>

Get-> curl -X GET "http://127.0.0.1:8000/randomcountry"
gives the random country to the user


post-> curl -X POST "http://127.0.0.1:8000/country" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"capital\": \"<your_input>\"}"


sample:
![image](https://github.com/user-attachments/assets/bf5105ce-a6e8-4fa3-9b10-6c6c7d5abddb)









