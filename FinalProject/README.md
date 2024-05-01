### README

##### Links to Google Documents:

[Product Backlog](https://docs.google.com/spreadsheets/d/1OMD_KwvRRUKudy6_c_UJ6Se1LZkZbJHrhR9AqtKBD00/edit?usp=sharing)
[User Stories](https://docs.google.com/spreadsheets/d/1GeEQFuDjDG1or4T4HTjFy-LcNVUjlrNnFSAwbUknQPA/edit?usp=sharing)
[Sprint Backlog](https://docs.google.com/spreadsheets/d/1KKYkwmjThF09HjwypnIDUll82e7k1odN/edit?usp=sharing&ouid=100919776270244663037&rtpof=true&sd=true)
[Sprint Review 1](https://docs.google.com/document/d/1KgtY76OANqWbnkkcg8wx1PmfXHfPz8XJ6-g_XKWXylc/edit?usp=sharing)
[Sprint Review 2](https://docs.google.com/document/d/10zXKCqZL4LSVf7gFCuaJWxFdnWYDgPwdC1qXmHhrj08/edit?usp=sharing)


### Essential dependencies

  - pip install fastapi
  - pip install "uvicorn\[standard\]" 
    - if README is showing \ in previous statement, remove them
  - pip install sqlalchemy
  - pip install pymysql
  - pip install pytest 
  - pip install pytest-mock 
  - pip install httpx 
  - pip install cryptography 

### How to run and populate mysql 

  - update config file with local information for mysql 
  - Run the server **from within the FinalProject folder**:
    - $uvicorn api.main:app --reload
  - If running from pycharm:
    - might need to use the following command:
      - $py -m uvicorn api.main:app --reload
- To run pytests:
    - run command $python -m pytest  
    - from FinalProject folder

  - Test API build-in docs:
    - [DOCS](http://127.0.0.1:8000/docs)

### Link to Youtube for Presentation 

[Presentation](https://www.youtube.com/watch?v=LIk1OrDq9Co)
