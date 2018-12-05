# loadtest-TDC-POA2018

## Execução exemplos

* Primeiro Exemplo (requests a um serviço externo)

```sh
$ locust -f example1.py
```
Então abra o navegador na url [localhost:8089](localhost:8089).

* Segundo Exemplo (adição de pesos as requests)

```sh
$ locust -f example2.py -H https://fakerestapi.azurewebsites.net
```

Então abra o navegador na url [localhost:8089](localhost:8089).

* Terceiro exemplo (adição de uma variável de ambiente para controlar o tempo para sucesso)

```sh
$ MAX_TIME=2000 locust --no-web --print-stats --logfile=logfile.txt -c 500 -r 50 -t 10m -L debug -f example3.py
```
