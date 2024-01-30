# Utiliza la imagen oficial de MariaDB
FROM mariadb

# Variables de entorno para configurar la base de datos
ENV MYSQL_ROOT_PASSWORD='37961'
ENV MYSQL_DATABASE='db_citas'
ENV MYSQL_USER='ti_1'
ENV MYSQL_PASSWORD='37961'

# Copia el script SQL que inicializará la base de datos
COPY db_citas.sql /docker-entrypoint-initdb.d/