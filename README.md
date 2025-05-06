# SimpleWeb

A clean, modern web page template built with best practices. This project provides a responsive landing page with a FastAPI backend.

![SimpleWeb Screenshot](https://via.placeholder.com/800x400?text=SimpleWeb+Screenshot)

## Features

- ✨ Clean, modern design
- 📱 Fully responsive layout
- 🚀 Fast loading and performance optimized
- ♿ Accessible design following WCAG guidelines
- 🔒 Secure contact form handling
- 🛠️ Easy setup with installation script
- 📊 FastAPI backend with OpenAPI documentation

## Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/simple-webpage.git
   cd simple-webpage
   ```

2. Run the installation script:
   ```bash
   chmod +x install.sh
   ./install.sh
   ```

3. Start the server:
   ```bash
   source venv/bin/activate
   python src/app.py
   ```

4. Open your browser and navigate to:
   ```
   http://localhost:8000
   ```

## Project Structure

```
simple-webpage/
├── docs/                  # Documentation files
├── src/                   # Source code
│   └── app.py             # FastAPI application
├── static/                # Static assets
│   ├── css/               # CSS stylesheets
│   │   └── styles.css     # Main stylesheet
│   ├── js/                # JavaScript files
│   │   └── main.js        # Main JavaScript file
│   └── images/            # Image assets
│       └── hero-image.svg # Hero section illustration
├── templates/             # HTML templates
│   └── index.html         # Main page template
├── tests/                 # Test files
├── .gitignore             # Git ignore file
├── install.sh             # Installation script
├── README.md              # Project documentation
└── requirements.txt       # Python dependencies
```

## Development

### Local Development

1. Activate the virtual environment:
   ```bash
   source venv/bin/activate
   ```

2. Start the server with auto-reload:
   ```bash
   python src/app.py
   ```

### API Documentation

FastAPI automatically generates OpenAPI documentation for the API endpoints. You can access it at:

```
http://localhost:8000/docs
```

## Customization

### Styling

The main stylesheet is located at `static/css/styles.css`. It uses CSS variables for easy theming:

```css
:root {
    --primary-color: #4a6cf7;
    --primary-dark: #3a56d4;
    /* Other color variables */
}
```

### Content

Edit the `templates/index.html` file to change the content of the page.

### Backend

The FastAPI application is defined in `src/app.py`. You can add new routes and functionality there.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) - The web framework used
- [Font Awesome](https://fontawesome.com/) - Icons used in the UI