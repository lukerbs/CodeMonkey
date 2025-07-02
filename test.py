#!/usr/bin/env python3
"""
Simple test script for ScriptMonkey 2.0
Tests the basic file copying functionality.
"""

import scriptmonkey

# Legacy function call (does nothing now, but maintains compatibility)
scriptmonkey.run()


def calculate_total(price, quantity):
    return price * quantity


def add_tax(total, tax_rate):
    return total + (total * tax_rate)


# Sample calculation
total = calculate_total(100, 2)
tax_rate = 0.08
final_total = add_tax(total, tax_rate)

print(f"Final total with tax: ${final_total:.2f}")
print("\nTo test ScriptMonkey 2.0, try:")
print("  scriptmonkey --files test.py")
print("  scriptmonkey --tree")
print("  scriptmonkey --files test.py --tree")
