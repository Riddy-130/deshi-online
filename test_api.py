"""
Test script to verify API endpoints are working correctly.
Run this while backend is running.
"""
import requests
import json

BASE_URL = "http://127.0.0.1:8000"

def test_health():
    print("Testing health endpoint...")
    try:
        response = requests.get(f"{BASE_URL}/api/v1/health/")
        print(f"  Status: {response.status_code}")
        print(f"  Response: {response.json()}")
    except Exception as e:
        print(f"  Error: {e}")

def test_signup():
    print("\nTesting signup endpoint...")
    try:
        data = {
            "full_name": "Test User",
            "email": "test@example.com",
            "password": "testpass123"
        }
        response = requests.post(
            f"{BASE_URL}/api/v1/auth/signup/",
            json=data
        )
        print(f"  Status: {response.status_code}")
        print(f"  Response: {response.text[:500]}")
    except Exception as e:
        print(f"  Error: {e}")

def test_signin():
    print("\nTesting signin endpoint...")
    try:
        data = {
            "email": "test@example.com",
            "password": "testpass123"
        }
        response = requests.post(
            f"{BASE_URL}/api/v1/auth/signin/",
            json=data
        )
        print(f"  Status: {response.status_code}")
        if response.status_code == 200:
            result = response.json()
            print(f"  Token: {result.get('token', 'N/A')[:20]}...")
            print(f"  User: {result.get('user', {})}")
    except Exception as e:
        print(f"  Error: {e}")

def test_storefront():
    print("\nTesting storefront endpoint...")
    try:
        response = requests.get(f"{BASE_URL}/api/v1/storefront/")
        print(f"  Status: {response.status_code}")
        data = response.json()
        print(f"  Categories: {len(data.get('categories', []))}")
        print(f"  Products: {len(data.get('products', []))}")
        print(f"  Featured: {len(data.get('featured_products', []))}")
    except Exception as e:
        print(f"  Error: {e}")

if __name__ == "__main__":
    print("="*50)
    print("API Test Script for Deshi Product")
    print("="*50)
    print("\nMake sure backend is running: python manage.py runserver")
    print()
    
    test_health()
    test_storefront()
    test_signup()
    test_signin()