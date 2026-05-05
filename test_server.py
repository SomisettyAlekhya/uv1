#!/usr/bin/env python3
"""Test script for ATM MCP Server"""

import subprocess
import json
import sys

def send_request(method, params=None):
    """Send a JSON-RPC request to the MCP server"""
    request = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": method,
        "params": params or {},
    }
    
    print(f"\n📤 Sending: {method}")
    print(f"   Params: {params}")
    print(json.dumps(request, indent=2))


if __name__ == "__main__":
    print("=" * 50)
    print("ATM MCP Server Tester")
    print("=" * 50)
    
    print("\n✅ Available commands to test:")
    print("   1. check_balance")
    print("   2. deposit(amount)")
    print("   3. withdraw(amount)")
    
    print("\n📋 Test Requests Format:")
    
    # Test 1: Check balance
    send_request("check_balance")
    
    # Test 2: Deposit
    send_request("deposit", {"amount": 500})
    
    # Test 3: Check balance again
    send_request("check_balance")
    
    # Test 4: Withdraw
    send_request("withdraw", {"amount": 200})
    
    # Test 5: Withdraw more than balance
    send_request("withdraw", {"amount": 5000})
