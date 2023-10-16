# ABC Jobs

## CI/CD
Se usa el github workflow y para cada microservicio
y en cada uno se propone los siguientes trabajos

### Test

Se crea un trabajo para  revisar los test unitarios y el coverage del codigo
si este trabajo no pasa, no se haran los siguientes trabajos
### Build

Si pasan los test unitarios se creara la imagen y se subira a
artifact registry

### Deploy

Una vez se suba la nueva imagen se desplegara a travez de kubernetes engine de GCP

### Merge a Develop

A su vez se hara un merge de lo nuevo en develop para sus pruebas de
integracion y posterior a esto se hara el merge a main.

## Documentacion y coverage

se uso Open Api y Swagger [Open Api Flask](https://luolingchun.github.io/flask-openapi3/v2.x/)

para acceder a la documentacion de plantea lo siguiente

### documentcion api metodos
/url-proyecto/docs para la docuemntacion de la api. ejemplo candidate/docs/

### docuemntacion coverage
/url-proyecto/coverage para los test de la api. ejemplo candidate/coverage/


## Hipotesis 1

En la carpeta app_candidate se encuentra el codigo para la primera hipotesis.
En la carpeta deployment se encuntre los archivos de k8s para desplegar el ingress y el pod
de candidate.


## docker

```shell
 docker build -t test-python-2 . 
```
cuando se construya la imagen 


```shell
docker run -p 3000:3000 test-python-2 
```

cambiar el puerto dependiendo de la aplicacion

## Tecnologias utilizadas
1. Postman
2. Python
3. Docker
4. Posgres
5. Flask
6. Kubernetes
7. GCP
8. gcloud SDK
9. kubectl
10. Git
