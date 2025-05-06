#!/usr/bin/env python3
"""
SimpleWeb CLI - Command Line Interface for SimpleWeb
Provides commands for running, testing, and managing the application
"""

import argparse
import os
import subprocess
import sys
import webbrowser
from typing import List, Optional, Dict, Any, Union

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

def run_server(host: str = "0.0.0.0", port: int = 8000, reload: bool = True) -> None:
    """
    Run the FastAPI server
    
    Args:
        host: The host to bind to
        port: The port to bind to
        reload: Whether to enable auto-reload
    """
    print(f"Starting server on http://{host}:{port}")
    
    if reload:
        print("Auto-reload enabled. Press Ctrl+C to stop.")
    
    # Import here to avoid circular imports
    from app import app
    import uvicorn
    
    uvicorn.run(app, host=host, port=port, reload=reload)

def run_tests(test_path: Optional[str] = None, coverage: bool = False) -> None:
    """
    Run the test suite
    
    Args:
        test_path: Path to specific tests to run
        coverage: Whether to generate coverage report
    """
    print("Running tests...")
    
    cmd = ["pytest", "-v"]
    
    if coverage:
        cmd.extend(["--cov=src", "--cov-report=term", "--cov-report=html"])
    
    if test_path:
        cmd.append(test_path)
    
    subprocess.run(cmd)
    
    if coverage:
        print("\nCoverage report generated in htmlcov/index.html")

def run_lint() -> None:
    """Run linting checks"""
    print("Running linting checks...")
    
    print("\n1. Running black...")
    subprocess.run(["black", "--check", "src", "tests"])
    
    print("\n2. Running isort...")
    subprocess.run(["isort", "--check-only", "--profile", "black", "src", "tests"])
    
    print("\n3. Running flake8...")
    subprocess.run(["flake8", "src", "tests"])
    
    print("\n4. Running mypy...")
    subprocess.run(["mypy", "src"])

def format_code() -> None:
    """Format code with black and isort"""
    print("Formatting code...")
    
    print("\n1. Running black...")
    subprocess.run(["black", "src", "tests"])
    
    print("\n2. Running isort...")
    subprocess.run(["isort", "--profile", "black", "src", "tests"])
    
    print("\nCode formatting complete.")

def open_docs() -> None:
    """Open API documentation in browser"""
    url = "http://localhost:8000/docs"
    print(f"Opening API documentation in browser: {url}")
    webbrowser.open(url)

def create_docker_image(tag: str = "latest") -> None:
    """
    Build Docker image
    
    Args:
        tag: Tag for the Docker image
    """
    print(f"Building Docker image with tag: {tag}")
    subprocess.run(["docker", "build", "-t", f"simpleweb:{tag}", "."])

def run_docker_container(tag: str = "latest", port: int = 8000) -> None:
    """
    Run Docker container
    
    Args:
        tag: Tag of the Docker image to run
        port: Port to expose
    """
    print(f"Running Docker container on port {port}")
    subprocess.run([
        "docker", "run", "-p", f"{port}:8000", 
        "--name", "simpleweb", 
        "-d", f"simpleweb:{tag}"
    ])
    
    print(f"Container running at http://localhost:{port}")

def main() -> None:
    """Main CLI entrypoint"""
    parser = argparse.ArgumentParser(
        description="SimpleWeb CLI - Command Line Interface for SimpleWeb",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Command to run")
    
    # Run server command
    run_parser = subparsers.add_parser("run", help="Run the FastAPI server")
    run_parser.add_argument("--host", default="0.0.0.0", help="Host to bind to")
    run_parser.add_argument("--port", type=int, default=8000, help="Port to bind to")
    run_parser.add_argument("--no-reload", action="store_true", help="Disable auto-reload")
    
    # Test command
    test_parser = subparsers.add_parser("test", help="Run tests")
    test_parser.add_argument("path", nargs="?", help="Path to specific tests to run")
    test_parser.add_argument("--coverage", action="store_true", help="Generate coverage report")
    
    # Lint command
    subparsers.add_parser("lint", help="Run linting checks")
    
    # Format command
    subparsers.add_parser("format", help="Format code with black and isort")
    
    # Docs command
    subparsers.add_parser("docs", help="Open API documentation in browser")
    
    # Docker commands
    docker_parser = subparsers.add_parser("docker", help="Docker commands")
    docker_subparsers = docker_parser.add_subparsers(dest="docker_command", help="Docker command to run")
    
    # Docker build command
    docker_build_parser = docker_subparsers.add_parser("build", help="Build Docker image")
    docker_build_parser.add_argument("--tag", default="latest", help="Tag for the Docker image")
    
    # Docker run command
    docker_run_parser = docker_subparsers.add_parser("run", help="Run Docker container")
    docker_run_parser.add_argument("--tag", default="latest", help="Tag of the Docker image to run")
    docker_run_parser.add_argument("--port", type=int, default=8000, help="Port to expose")
    
    args = parser.parse_args()
    
    # Handle commands
    if args.command == "run":
        run_server(args.host, args.port, not args.no_reload)
    elif args.command == "test":
        run_tests(args.path, args.coverage)
    elif args.command == "lint":
        run_lint()
    elif args.command == "format":
        format_code()
    elif args.command == "docs":
        open_docs()
    elif args.command == "docker":
        if args.docker_command == "build":
            create_docker_image(args.tag)
        elif args.docker_command == "run":
            run_docker_container(args.tag, args.port)
        else:
            docker_parser.print_help()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()