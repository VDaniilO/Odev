# Odev

# djnago_transfer_money

## Install all requirements:

  `pip install -r requirements.txt`
  
## Run project:
  
  `python wallets/manage.py runserver`
  
### URLS:
  
  ```
    POST http://localhost:8000/wallets/ -d "name=NameOfWallet&balance=0.00"      | Create wallet with 0 money
    GET  http://localhost:8000/wallets/                                          | Show all wallets
    POST http://localhost:8000/transactions/                                     | Create transaction follow JSON
         example body for transfer = {
                                      "sender": 1,
                                      "receiver": 2,
                                      "amount": 10.0
                                      }
  ```
