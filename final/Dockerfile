# FROM alpine


# LABEL maintainer="shbhat@pdx.edu"

# # Install pip
# RUN apk add --no-cache python3-dev \
#   && python3 -m ensurepip \
#   && pip3 install --upgrade pip setuptools \
#   && rm -r /usr/lib/python*/ensurepip \
#   && rm -r /root/.cache

# # Copy the contents of the current directory into the container directory /app
# COPY . /app

# # Set the working directory of the container to /app
# WORKDIR /app

# # Install the Python packages specified by requirements.txt into the container

# RUN pip install --no-cache -r requirements.txt

# # Set the program that is invoked upon container instantiation
# ENTRYPOINT ["python3"]

# # Set the parameters to the program
# CMD ["app.py"]


# Use Google Cloud SDK's container as the base image
FROM google/cloud-sdk

# Specify your e-mail address as the maintainer of the container image
LABEL maintainer="shbhat@pdx.edu"

# Copy the contents of the current directory into the container directory /app
COPY . /app

# Set the working directory of the container to /app
WORKDIR /app

# Install the Python packages specified by requirements.txt into the container
RUN curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - && apt update --allow-releaseinfo-change -y && apt install -y python3-pip && pip3 install -r requirements.txt

# Set the parameters to the program
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app
