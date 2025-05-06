#!/bin/bash
set -e

echo "Creating DigitalOcean App Platform app from specification..."

# Verify doctl is authenticated
if ! doctl account get > /dev/null; then
  echo "You need to authenticate with doctl first. Run 'doctl auth init' and try again."
  exit 1
fi

# Path to the app spec file
APP_SPEC="app-spec.yaml"

# Check if app spec file exists
if [ ! -f "$APP_SPEC" ]; then
  echo "Error: App spec file '$APP_SPEC' not found."
  exit 1
fi

# Check if the app already exists
APP_ID=$(doctl apps list --format ID,Spec.Name --no-header | grep "simpleweb" | awk '{print $1}')

if [ -n "$APP_ID" ]; then
  echo "App 'simpleweb' already exists with ID: $APP_ID"
  echo "Updating existing app..."
  doctl apps update "$APP_ID" --spec "$APP_SPEC"
else
  echo "Creating new app..."
  # Create the app from the spec file
  doctl apps create --spec "$APP_SPEC"
fi

echo "Deployment initiated! Your app will be available shortly."
echo "You can check its status with: doctl apps list"
echo "Once deployed, you can get the app URL with: doctl apps list --format DefaultIngress"