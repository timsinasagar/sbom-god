# Use an Ubuntu base image
FROM ubuntu:22.04

# Set the environment variables to non-interactive
ENV DEBIAN_FRONTEND=noninteractive

# Update the package list and install basic tools
RUN apt-get update && \
    apt-get install -y \
    curl \
    wget \
    git \
    unzip \
    build-essential \
    apt-transport-https \
    ca-certificates \
    gnupg \
    software-properties-common

# Install Node.js (with npm)
RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y nodejs

# Install Python (with pip)
RUN apt-get install -y python3 python3-pip

# Install PHP (with Composer)
RUN apt-get install -y php-cli unzip && \
    curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# Install Java (OpenJDK 17)
RUN apt-get install -y openjdk-17-jdk

# Install Maven for Java
RUN apt-get install -y maven

# Install .NET SDK
RUN wget https://packages.microsoft.com/config/ubuntu/22.04/packages-microsoft-prod.deb -O packages-microsoft-prod.deb && \
    dpkg -i packages-microsoft-prod.deb && \
    apt-get update && \
    apt-get install -y dotnet-sdk-7.0

# Install CycloneDX for Node.js
RUN npm install -g @cyclonedx/cyclonedx-npm

# Install CycloneDX for Python
RUN pip3 install cyclonedx-bom

# Install Syft (for SBOM generation across multiple languages)
RUN curl -sSfL https://raw.githubusercontent.com/anchore/syft/main/install.sh | sh -s -- -b /usr/local/bin

# Install OWASP Dependency Check for Java
RUN mkdir /dependency-check && \
    curl -L https://github.com/jeremylong/DependencyCheck/releases/download/v8.4.0/dependency-check-8.4.0-release.zip -o dependency-check.zip && \
    unzip dependency-check.zip -d /dependency-check && \
    rm dependency-check.zip

# Install pip-audit for Python vulnerability scanning
RUN pip3 install pip-audit

# Install Ruby (required for CocoaPods)
RUN apt-get install -y ruby-full

# Install CocoaPods
RUN gem install cocoapods

# Set up working directory
WORKDIR /app

# Default command to keep the container running
CMD ["python3", "orchestrator.py"]

# docker build -t sbom-scanner:latest .
# docker run -it --rm -v $(pwd):/app sbom-scanner:latest