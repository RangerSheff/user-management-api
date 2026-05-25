#!/bin/bash

echo "=================================="
echo "Running Ruff..."
echo "=================================="
ruff check .

if [ $? -ne 0 ]; then
  echo "Ruff validation failed"
  exit 1
fi

echo ""
echo "=================================="
echo "Running Bandit..."
echo "=================================="
bandit -r app

if [ $? -ne 0 ]; then
  echo "Bandit validation failed"
  exit 1
fi

echo ""
echo "=================================="
echo "Running pip-audit..."
echo "=================================="
pip-audit

if [ $? -ne 0 ]; then
  echo "Dependency vulnerability scan failed"
  exit 1
fi

echo ""
echo "=================================="
echo "Running tests..."
echo "=================================="
pytest --cov=app

if [ $? -ne 0 ]; then
  echo "Tests failed"
  exit 1
fi

echo ""
echo "=================================="
echo "All validations passed successfully"
echo "=================================="
