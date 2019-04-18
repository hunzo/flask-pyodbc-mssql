# Use an official Python runtime as a parent image
FROM python

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

#Install unixodbc

RUN echo "[FreeTDS]\n\
Description = FreeTDS unixODBC Driver\n\
Driver = /usr/lib/x86_64-linux-gnu/odbc/libtdsodbc.so\n\
Setup = /usr/lib/x86_64-linux-gnu/odbc/libtdsS.so" >> /etc/odbcinst.ini

RUN apt-get update
RUN apt-get install -y tdsodbc unixodbc-dev gcc
RUN apt install unixodbc-bin -y
RUN apt-get clean -y



# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Run app.py when the container launches
CMD python app.py