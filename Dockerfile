FROM ubuntu:18.04

# Update repository databases
RUN apt-get update

# Install necessary packages to install
RUN apt-get install -y apt-utils software-properties-common
RUN apt-get install -y wget ca-certificates

# Add PostgreSQL repository key to machine
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -

# Add PostgreSQL repository to machine
RUN apt-add-repository 'deb http://apt.postgresql.org/pub/repos/apt/ bionic-pgdg main'

# Update repository databases
RUN apt-get update

#  There are some warnings (in red) that show up during the build. You can hide
#  them by prefixing each apt-get statement with DEBIAN_FRONTEND=noninteractive
RUN apt-get install -y postgresql-11

# Run the rest of the commands as the ``postgres`` user
USER postgres

# Create a PostgreSQL role named ``itucs`` with ``itucspw`` as the password and
# then create a database `itucsdb` owned by the ``itucs`` role.
RUN    /etc/init.d/postgresql start &&\
    psql --command "CREATE USER itucs WITH SUPERUSER PASSWORD 'itucspw';" &&\
    createdb -O itucs itucsdb

# Adjust PostgreSQL configuration so that remote connections to the
# database are possible.
RUN echo "host all  all    0.0.0.0/0  md5" >> /etc/postgresql/11/main/pg_hba.conf

# And add ``listen_addresses`` to ``/etc/postgresql/11/main/postgresql.conf``
RUN echo "listen_addresses='*'" >> /etc/postgresql/11/main/postgresql.conf

# Expose the PostgreSQL port
EXPOSE 5432

# Add VOLUMEs to allow backup of config, logs and databases
VOLUME  ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]

# Set the default command to run when starting the container
CMD ["/usr/lib/postgresql/11/bin/postgres", "-D", "/var/lib/postgresql/11/main", "-c", "config_file=/etc/postgresql/11/main/postgresql.conf"]
