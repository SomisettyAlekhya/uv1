from mcp.server.fastmcp import FastMCP

mcp = FastMCP("atm-server")

balance = 1000


@mcp.tool()
def check_balance():
    return f"Your balance is ₹{balance}"


@mcp.tool()
def deposit(amount: float):
    global balance
    balance += amount
    return f"Deposited ₹{amount}. New balance: ₹{balance}"


@mcp.tool()
def withdraw(amount: float):
    global balance
    if amount > balance:
        return "Insufficient balance"
    balance -= amount
    return f"Withdrawn ₹{amount}. Remaining balance: ₹{balance}"


if __name__ == "__main__":
    print("ATM MCP Server starting...")
    print("Available tools: check_balance, deposit, withdraw")
    mcp.run()