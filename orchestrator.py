import subprocess
import os

def run_command(command, cwd=None):
    result = subprocess.run(command, shell=True, cwd=cwd, text=True, capture_output=True)
    if result.returncode != 0:
        print(f"Command failed with error: {result.stderr}")
    else:
        print(f"Command succeeded: {result.stdout}")
    return result

# Example for JavaScript (Node.js)
def process_nodejs_project():
    # Install dependencies
    run_command("npm install")
    # Generate SBOM (using CycloneDX or Syft)
    run_command("npx @cyclonedx/cyclonedx-npm --output-format json --output-file /app/sbom-nodejs.json")
    # Run vulnerability scan
    run_command("npm audit")

# Example for Python
def process_python_project():
    # Install dependencies
    run_command("pip install -r requirements.txt")


    # Generate SBOM (using CycloneDX for requirements.txt)
    run_command("cyclonedx-py requirements -i requirements.txt -o sbom-python.json")
    # Run vulnerability scan
    # run_command("pip-audit -r ./requirements.txt")
    run_command("pip-audit --desc")

# Example for PHP (Composer)
def process_php_project():
    # Install dependencies
    run_command("composer install")
    # Generate SBOM
    run_command("composer sbom")
    # Run vulnerability scan
    run_command("composer audit")



# Example for Java (Maven)
def process_java_project():
    # Install dependencies
    run_command("mvn clean install")
    # Generate SBOM (using CycloneDX plugin)
    run_command("mvn org.cyclonedx:cyclonedx-maven-plugin:makeAggregateBom")
    # Run vulnerability scan (using OWASP Dependency Check)
    run_command("mvn org.owasp:dependency-check-maven:check")

# Example for C# (Dotnet)
def process_csharp_project():
    # Install dependencies
    run_command("dotnet restore")
    # Generate SBOM (using Syft or CycloneDX)
    run_command("syft dotnet -o sbom.json")
    # Run vulnerability scan
    run_command("dotnet list package --vulnerable")


def process_cocoapods_project():
    # Install dependencies
    run_command("pod install")
    # Generate SBOM (using Syft or another tool if supported for Swift/Objective-C)
    # run_command("syft /app/Podfile.lock -o cyclonedx-json=/app/sbom-cocoapods.json")
    # (Optional) Run vulnerability scan (CocoaPods does not have a built-in audit tool)
    # You might use a custom script or a third-party tool here
        # Install dependencies
    run_command("pod install")
    # Generate SBOM (using Syft for the local directory)
    run_command("syft dir:/app -o cyclonedx-json=/app/sbom-cocoapods.json")
    # (Optional) Run vulnerability scan (CocoaPods does not have a built-in audit tool)
    # You might use a custom script or a third-party tool here
    # Run Snyk vulnerability scan
    run_command("snyk test --file=Podfile.lock")

# Example dispatcher based on file type
def process_project(file_path):
    if os.path.exists(file_path):
        if file_path.endswith("package.json"):
            process_nodejs_project()
        elif file_path.endswith("requirements.txt"):
            process_python_project()
        elif file_path.endswith("composer.json"):
            process_php_project()
        elif file_path.endswith("Podfile"):
            process_cocoapods_project()
        else:
            print("Unsupported file type")
    else:
        print("File not found")

# Example usage
# process_project("package.json")
# process_project("Podfile")
process_project("requirements.txt")