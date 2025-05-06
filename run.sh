#!/bin/bash
# SimpleWeb - Run Script
# This script provides a simple way to run the application

set -e  # Exit immediately if a command exits with a non-zero status

# Print colored output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo -e "${YELLOW}Virtual environment not found. Running installation script...${NC}"
    chmod +x install.sh
    ./install.sh
fi

# Activate virtual environment
echo -e "${YELLOW}Activating virtual environment...${NC}"
source venv/bin/activate

# Run the application
echo -e "${GREEN}Starting SimpleWeb application...${NC}"
python src/app.py

# Deactivate virtual environment on exit
trap "echo -e '${YELLOW}Deactivating virtual environment...${NC}'; deactivate" EXIT