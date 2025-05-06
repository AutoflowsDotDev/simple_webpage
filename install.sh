#!/bin/bash
# SimpleWeb - Installation Script
# This script sets up the environment and installs dependencies

set -e  # Exit immediately if a command exits with a non-zero status

# Print colored output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${YELLOW}=== SimpleWeb Installation ===${NC}"

# Check if Python 3 is installed
if command -v python3 &>/dev/null; then
    echo -e "${GREEN}Python 3 is installed${NC}"
    PYTHON_CMD="python3"
elif command -v python &>/dev/null; then
    # Check if python is Python 3
    PYTHON_VERSION=$(python --version 2>&1)
    if [[ $PYTHON_VERSION == *"Python 3"* ]]; then
        echo -e "${GREEN}Python 3 is installed${NC}"
        PYTHON_CMD="python"
    else
        echo -e "${RED}Python 3 is required but not installed. Please install Python 3 and try again.${NC}"
        exit 1
    fi
else
    echo -e "${RED}Python 3 is required but not installed. Please install Python 3 and try again.${NC}"
    exit 1
fi

# Check if pip is installed
if ! command -v pip3 &>/dev/null && ! command -v pip &>/dev/null; then
    echo -e "${RED}pip is required but not installed. Please install pip and try again.${NC}"
    exit 1
fi

# Determine pip command
if command -v pip3 &>/dev/null; then
    PIP_CMD="pip3"
else
    PIP_CMD="pip"
fi

# Create virtual environment
echo -e "${YELLOW}Creating virtual environment...${NC}"
$PYTHON_CMD -m venv venv
echo -e "${GREEN}Virtual environment created${NC}"

# Activate virtual environment
echo -e "${YELLOW}Activating virtual environment...${NC}"
source venv/bin/activate

# Install dependencies
echo -e "${YELLOW}Installing dependencies...${NC}"
$PIP_CMD install --upgrade pip
$PIP_CMD install -r requirements.txt

echo -e "${GREEN}Dependencies installed successfully${NC}"

# Create necessary directories if they don't exist
echo -e "${YELLOW}Checking directory structure...${NC}"
mkdir -p static/css static/js static/images templates src

echo -e "${GREEN}Installation completed successfully!${NC}"
echo -e "${YELLOW}To run the application:${NC}"
echo -e "1. Activate the virtual environment: ${GREEN}source venv/bin/activate${NC}"
echo -e "2. Start the server: ${GREEN}python src/app.py${NC}"
echo -e "3. Open your browser and navigate to: ${GREEN}http://localhost:8000${NC}"