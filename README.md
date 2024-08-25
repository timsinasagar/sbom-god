# sbom-god

docker build -t sbom-scanner:latest .

docker run -it --rm -v $(pwd):/app sbom-scanner:latest

             +--------------------------------+
             |            Frontend            |
             | +----------------------------+ |
             | |  Web Interface / API        | |
             | +----------------------------+ |
             +--------------------------------+
                          |
                          v
             +--------------------------------+
             |            Backend             |
             | +----------------------------+ |
             | |  File Ingestion Service     | |
             | +----------------------------+ |
             |                |                |
             |                v                |
             | +----------------------------+ |
             | | SBOM Generation Service     | |
             | +----------------------------+ |
             |                |                |
             |                v                |
             | +----------------------------+ |
             | |  Security Audit Service     | |
             | +----------------------------+ |
             |                |                |
             |                v                |
             | +----------------------------+ |
             | | Results Aggregation Service | |
             | +----------------------------+ |
             +--------------------------------+
                          |
                          v
             +--------------------------------+
             |          Storage Service       |
             |  +--------------------------+  |
             |  |       Database           |  |
             |  +--------------------------+  |
             +--------------------------------+
                          |
                          v
             +--------------------------------+
             |       Notification Service     |
             |  +--------------------------+  |
             |  | Email / Slack / etc.     |  |
             |  +--------------------------+  |
             +--------------------------------+
                          |
                          v
             +--------------------------------+
             |        CI/CD Integration       |
             |  +--------------------------+  |
             |  |      Webhook Service      |  |
             |  +--------------------------+  |
             +--------------------------------+
