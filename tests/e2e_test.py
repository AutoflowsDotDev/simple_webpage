"""
End-to-end tests for SimpleWeb using Playwright
"""

import os
import sys
import pytest
from playwright.sync_api import Page, expect

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Base URL for tests
BASE_URL = "http://localhost:8000"

def test_homepage_loads(page: Page):
    """Test that the homepage loads correctly"""
    # Navigate to the homepage
    page.goto(BASE_URL)
    
    # Check that the page title is correct
    expect(page).to_have_title("Simple Web Page")
    
    # Check that the main heading is visible
    heading = page.locator("h2:has-text('Welcome to SimpleWeb')")
    expect(heading).to_be_visible()
    
    # Check that the navigation links are present
    nav_links = page.locator(".main-nav a")
    expect(nav_links).to_have_count(4)  # Home, Features, About, Contact
    
    # Check that the hero section is visible
    hero = page.locator(".hero")
    expect(hero).to_be_visible()
    
    # Check that the features section is visible
    features = page.locator(".features")
    expect(features).to_be_visible()
    
    # Take a screenshot for visual verification
    page.screenshot(path="homepage.png")

def test_navigation(page: Page):
    """Test that navigation links work correctly"""
    # Navigate to the homepage
    page.goto(BASE_URL)
    
    # Click on the Features link
    page.click("text=Features")
    
    # Check that the Features section is visible and in viewport
    features_section = page.locator("#features")
    expect(features_section).to_be_visible()
    expect(features_section).to_be_in_viewport()
    
    # Click on the About link
    page.click("text=About")
    
    # Check that the About section is visible and in viewport
    about_section = page.locator("#about")
    expect(about_section).to_be_visible()
    expect(about_section).to_be_in_viewport()
    
    # Click on the Contact link
    page.click("text=Contact")
    
    # Check that the Contact section is visible and in viewport
    contact_section = page.locator("#contact")
    expect(contact_section).to_be_visible()
    expect(contact_section).to_be_in_viewport()

def test_contact_form(page: Page):
    """Test that the contact form works correctly"""
    # Navigate to the homepage
    page.goto(BASE_URL)
    
    # Scroll to the contact section
    page.click("text=Contact")
    
    # Fill out the contact form
    page.fill("#name", "Test User")
    page.fill("#email", "test@example.com")
    page.fill("#message", "This is a test message from the end-to-end test.")
    
    # Submit the form
    page.click(".contact-form button[type=submit]")
    
    # In our implementation, JavaScript shows a success message
    # Wait for the success message to appear
    success_message = page.locator(".success-message")
    expect(success_message).to_be_visible()
    expect(success_message).to_contain_text("Thank you for your message")

def test_responsive_design(page: Page):
    """Test that the design is responsive"""
    # Test on mobile viewport
    page.set_viewport_size({"width": 375, "height": 667})  # iPhone SE size
    page.goto(BASE_URL)
    
    # Check that the mobile layout is applied
    # In mobile view, the hero content and image should be stacked
    hero_container = page.locator(".hero .container")
    expect(hero_container).to_have_css("flex-direction", "column")
    
    # Take a screenshot of mobile view
    page.screenshot(path="mobile_view.png")
    
    # Test on tablet viewport
    page.set_viewport_size({"width": 768, "height": 1024})  # iPad size
    page.goto(BASE_URL)
    
    # Take a screenshot of tablet view
    page.screenshot(path="tablet_view.png")
    
    # Test on desktop viewport
    page.set_viewport_size({"width": 1280, "height": 800})  # Desktop size
    page.goto(BASE_URL)
    
    # Check that the desktop layout is applied
    # In desktop view, the hero content and image should be side by side
    hero_container = page.locator(".hero .container")
    expect(hero_container).not_to_have_css("flex-direction", "column")
    
    # Take a screenshot of desktop view
    page.screenshot(path="desktop_view.png")

if __name__ == "__main__":
    # This allows running the tests directly with python
    # You would normally run with pytest
    pytest.main(["-v", __file__])