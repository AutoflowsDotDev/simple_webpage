"""
SimpleWeb - FastAPI Server
A simple web server to serve the static website with FastAPI
"""

import os
import logging
from typing import Dict, Any, Optional
from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, EmailStr
import uvicorn

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("app.log")
    ]
)

logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="SimpleWeb",
    description="A simple web page served with FastAPI",
    version="1.0.0"
)

# Get the directory of the current file
current_dir = os.path.dirname(os.path.abspath(__file__))
# Go up one level to the project root
project_root = os.path.dirname(current_dir)

# Mount static files
app.mount("/static", StaticFiles(directory=os.path.join(project_root, "static")), name="static")

# Set up templates
templates = Jinja2Templates(directory=os.path.join(project_root, "templates"))

# Define data models
class ContactForm(BaseModel):
    name: str
    email: EmailStr
    message: str

class ContactResponse(BaseModel):
    success: bool
    message: str

@app.get("/", response_class=HTMLResponse)
async def home(request: Request) -> HTMLResponse:
    """
    Serve the main index.html page
    
    Args:
        request: The incoming request object
        
    Returns:
        HTMLResponse: The rendered HTML template
    """
    logger.info("Home page requested")
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/api/contact", response_model=ContactResponse)
async def contact(form_data: ContactForm) -> Dict[str, Any]:
    """
    Handle contact form submissions
    
    Args:
        form_data: The submitted form data
        
    Returns:
        Dict: JSON response indicating success or failure
    """
    try:
        logger.info(f"Contact form submission from {form_data.email}")
        
        # In a real application, you would process the form data here
        # For example, send an email or store in a database
        
        return {
            "success": True,
            "message": "Thank you for your message! We'll get back to you soon."
        }
    except Exception as e:
        logger.error(f"Error processing contact form: {str(e)}")
        raise HTTPException(status_code=500, detail="An error occurred processing your request")

@app.get("/health")
async def health_check() -> Dict[str, str]:
    """
    Health check endpoint for monitoring
    
    Returns:
        Dict: Status information
    """
    return {"status": "healthy"}

def start() -> None:
    """Start the FastAPI server using uvicorn"""
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)

if __name__ == "__main__":
    start()