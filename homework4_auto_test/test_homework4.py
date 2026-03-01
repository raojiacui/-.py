# -*- coding: utf-8 -*-
# Homework 4 Auto Test File
# Contains test cases for all 14 homework assignments

import importlib
import sys
import os

# Add parent directory to path to import homework file
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Test results counter
test_results = {
    'passed': 0,
    'failed': 0,
    'errors': []
}


def ensure(condition, message):
    """Test assertion function"""
    if not condition:
        test_results['failed'] += 1
        test_results['errors'].append(message)
        print(f"  [FAIL] {message}")
        return False
    else:
        test_results['passed'] += 1
        return True


def reload_homework():
    """Reload homework module"""
    import 作业四
    importlib.reload(作业四)
    return 作业四


# ==================== Homework 1 Test ====================
def test_find(hw):
    print("\n[TEST] HW1 - find function:")
    try:
        ensure(hw.find('hello', 'e') == 1, "find('hello', 'e') should return 1")
        ensure(hw.find('hello', 'l') == 2, "find('hello', 'l') should return 2")
        ensure(hw.find('world', 'o') == 1, "find('world', 'o') should return 1")
        ensure(hw.find('abc', 'a') == 0, "find('abc', 'a') should return 0")
        ensure(hw.find('abc', 'c') == 2, "find('abc', 'c') should return 2")
        ensure(hw.find('hello', 'x') == -1, "find('hello', 'x') should return -1")
        ensure(hw.find('world', 'z') == -1, "find('world', 'z') should return -1")
    except Exception as e:
        ensure(False, f"find function error: {e}")


# ==================== Homework 2 Test ====================
def test_uppercase(hw):
    print("\n[TEST] HW2 - uppercase function:")
    try:
        ensure(hw.uppercase('abc') == 'ABC', "uppercase('abc') should return 'ABC'")
        ensure(hw.uppercase('hello') == 'HELLO', "uppercase('hello') should return 'HELLO'")
        ensure(hw.uppercase('world') == 'WORLD', "uppercase('world') should return 'WORLD'")
        ensure(hw.uppercase('xyz') == 'XYZ', "uppercase('xyz') should return 'XYZ'")
    except Exception as e:
        ensure(False, f"uppercase function error: {e}")


# ==================== Homework 3 Test ====================
def test_lowercase1(hw):
    print("\n[TEST] HW3 - lowercase1 function:")
    try:
        ensure(hw.lowercase1('Hello') == 'hello', "lowercase1('Hello') should return 'hello'")
        ensure(hw.lowercase1('HELLO') == 'hello', "lowercase1('HELLO') should return 'hello'")
        ensure(hw.lowercase1('Hello World') == 'hello world', "lowercase1('Hello World') should return 'hello world'")
        ensure(hw.lowercase1('ABC123') == 'abc123', "lowercase1('ABC123') should return 'abc123'")
    except Exception as e:
        ensure(False, f"lowercase1 function error: {e}")


# ==================== Homework 4 Test ====================
def test_uppercase1(hw):
    print("\n[TEST] HW4 - uppercase1/uppercase function:")
    try:
        # Note: The function might be named uppercase1 or uppercase
        if hasattr(hw, 'uppercase1'):
            func = hw.uppercase1
            func_name = 'uppercase1'
        else:
            func = hw.uppercase
            func_name = 'uppercase'

        ensure(func('Hello') == 'HELLO', f"{func_name}('Hello') should return 'HELLO'")
        ensure(func('hello') == 'HELLO', f"{func_name}('hello') should return 'HELLO'")
        ensure(func('Hello World') == 'HELLO WORLD', f"{func_name}('Hello World') should return 'HELLO WORLD'")
        ensure(func('abc123') == 'ABC123', f"{func_name}('abc123') should return 'ABC123'")
    except Exception as e:
        ensure(False, f"uppercase1 function error: {e}")


# ==================== Homework 5 Test ====================
def test_encode1(hw):
    print("\n[TEST] HW5 - encode1 function:")
    try:
        ensure(hw.encode1('abc') == 'bcd', "encode1('abc') should return 'bcd'")
        ensure(hw.encode1('xyz') == 'yza', "encode1('xyz') should return 'yza'")
        ensure(hw.encode1('afz') == 'bga', "encode1('afz') should return 'bga'")
        ensure(hw.encode1('hello') == 'ifmmp', "encode1('hello') should return 'ifmmp'")
    except Exception as e:
        ensure(False, f"encode1 function error: {e}")


# ==================== Homework 6 Test ====================
def test_decode1(hw):
    print("\n[TEST] HW6 - decode1 function:")
    try:
        ensure(hw.decode1('bcd') == 'abc', "decode1('bcd') should return 'abc'")
        ensure(hw.decode1('yza') == 'xyz', "decode1('yza') should return 'xyz'")
        ensure(hw.decode1('bga') == 'afz', "decode1('bga') should return 'afz'")
        ensure(hw.decode1('ifmmp') == 'hello', "decode1('ifmmp') should return 'hello'")
        ensure(hw.decode1(hw.encode1('hello')) == 'hello', "decode1(encode1('hello')) should return 'hello'")
    except Exception as e:
        ensure(False, f"decode1 function error: {e}")


# ==================== Homework 7 Test ====================
def test_encode2(hw):
    print("\n[TEST] HW7 - encode2 function:")
    try:
        ensure(hw.encode2('abc', 1) == 'bcd', "encode2('abc', 1) should return 'bcd'")
        ensure(hw.encode2('abc', 2) == 'cde', "encode2('abc', 2) should return 'cde'")
        ensure(hw.encode2('xyz', 3) == 'abc', "encode2('xyz', 3) should return 'abc'")
        ensure(hw.encode2('hello', 5) == 'mjqqt', "encode2('hello', 5) should return 'mjqqt'")
        ensure(hw.encode2('a', 26) == 'a', "encode2('a', 26) should return 'a'")
        ensure(hw.encode2('a', 27) == 'b', "encode2('a', 27) should return 'b'")
    except Exception as e:
        ensure(False, f"encode2 function error: {e}")


# ==================== Homework 8 Test ====================
def test_decode2(hw):
    print("\n[TEST] HW8 - decode2 function:")
    try:
        ensure(hw.decode2('bcd', 1) == 'abc', "decode2('bcd', 1) should return 'abc'")
        ensure(hw.decode2('cde', 2) == 'abc', "decode2('cde', 2) should return 'abc'")
        ensure(hw.decode2('abc', 3) == 'xyz', "decode2('abc', 3) should return 'xyz'")
        ensure(hw.decode2('mjqqt', 5) == 'hello', "decode2('mjqqt', 5) should return 'hello'")
        ensure(hw.decode2(hw.encode2('hello', 7), 7) == 'hello', "decode2(encode2('hello', 7), 7) should return 'hello'")
    except Exception as e:
        ensure(False, f"decode2 function error: {e}")


# ==================== Homework 9 Test ====================
def test_encode3(hw):
    print("\n[TEST] HW9 - encode3 function:")
    try:
        ensure(hw.encode3('a-b-c', 1) == 'b-c-d', "encode3('a-b-c', 1) should return 'b-c-d'")
        ensure(hw.encode3('hello world', 1) == 'ifmmp xpsme', "encode3('hello world', 1) should return 'ifmmp xpsme'")
        ensure(hw.encode3('abc xyz!', 3) == 'def abc!', "encode3('abc xyz!', 3) should return 'def abc!'")
        ensure(hw.encode3('test-123', 2) == 'vguv-123', "encode3('test-123', 2) should return 'vguv-123'")
    except Exception as e:
        ensure(False, f"encode3 function error: {e}")


# ==================== Homework 10 Test ====================
def test_decode3(hw):
    print("\n[TEST] HW10 - decode3 function:")
    try:
        ensure(hw.decode3('b-c-d', 1) == 'a-b-c', "decode3('b-c-d', 1) should return 'a-b-c'")
        ensure(hw.decode3('ifmmp xpsme', 1) == 'hello world', "decode3('ifmmp xpsme', 1) should return 'hello world'")
        ensure(hw.decode3('def abc!', 3) == 'abc xyz!', "decode3('def abc!', 3) should return 'abc xyz!'")
        ensure(hw.decode3(hw.encode3('hello world!', 5), 5) == 'hello world!', "decode3(encode3('hello world!', 5), 5) should return 'hello world!'")
    except Exception as e:
        ensure(False, f"decode3 function error: {e}")


# ==================== Homework 11 Test ====================
def test_decode4(hw):
    print("\n[TEST] HW11 - decode4 function (Zhihu cipher):")
    try:
        # decode4 should decrypt the Zhihu cipher
        # Correct answer shift=3: "sometimes i want to chat with you,but i have no reason to chat with you"
        print("  (decode4 function defined, check output manually)")
        ensure(hasattr(hw, 'decode4'), "decode4 function should exist")
    except Exception as e:
        ensure(False, f"decode4 function error: {e}")


# ==================== Homework 12 Test ====================
def test_find2(hw):
    print("\n[TEST] HW12 - find2 function:")
    try:
        ensure(hw.find2('hello world', 'world') == 6, "find2('hello world', 'world') should return 6")
        ensure(hw.find2('hello world', 'hello') == 0, "find2('hello world', 'hello') should return 0")
        ensure(hw.find2('aaa', 'aa') == 0, "find2('aaa', 'aa') should return 0")
        ensure(hw.find2('hello world', 'xyz') == -1, "find2('hello world', 'xyz') should return -1")
        ensure(hw.find2('abc', 'abcd') == -1, "find2('abc', 'abcd') should return -1")
        ensure(hw.find2('abc', 'abc') == 0, "find2('abc', 'abc') should return 0")
    except Exception as e:
        ensure(False, f"find2 function error: {e}")


# ==================== Homework 13 Test ====================
def test_find_between(hw):
    print("\n[TEST] HW13 - find_between function:")
    try:
        s1 = 'meet #<gua># halfway'
        s2 = 'meet #<gua># #<high>#way'
        left = '#<'
        right = '>#'

        ensure(hw.find_between(s1, left, right) == 'gua', "find_between(s1, left, right) should return 'gua'")
        ensure(hw.find_between(s2, left, right) == 'gua', "find_between(s2, left, right) should return 'gua'")
        ensure(hw.find_between('<hello>world<test>', '<', '>') == 'hello', "find_between('<hello>world<test>', '<', '>') should return 'hello'")
        ensure(hw.find_between('hello world', '#<', '>#') == -1, "find_between('hello world', '#<', '>#') should return -1")
    except Exception as e:
        ensure(False, f"find_between function error: {e}")


# ==================== Homework 14 Test ====================
def test_openurl(hw):
    print("\n[TEST] HW14 - openurl function (crawler):")
    try:
        ensure(hasattr(hw, 'openurl'), "openurl function should exist")
        print("  (Network test skipped, call openurl() manually)")
    except Exception as e:
        ensure(False, f"openurl function error: {e}")


# ==================== Run All Tests ====================
def run_all_tests():
    """Run all tests"""
    global test_results
    test_results = {'passed': 0, 'failed': 0, 'errors': []}

    print("=" * 60)
    print("[START] Running Homework 4 Tests")
    print("=" * 60)

    try:
        hw = reload_homework()
    except Exception as e:
        print(f"[ERROR] Cannot load homework file: {e}")
        return test_results

    # Run all tests
    test_find(hw)
    test_uppercase(hw)
    test_lowercase1(hw)
    test_uppercase1(hw)
    test_encode1(hw)
    test_decode1(hw)
    test_encode2(hw)
    test_decode2(hw)
    test_encode3(hw)
    test_decode3(hw)
    test_decode4(hw)
    test_find2(hw)
    test_find_between(hw)
    test_openurl(hw)

    # Print summary
    print("\n" + "=" * 60)
    print("[SUMMARY] Test Results")
    print("=" * 60)
    print(f"[PASS] Passed: {test_results['passed']}")
    print(f"[FAIL] Failed: {test_results['failed']}")

    if test_results['failed'] == 0:
        print("\n[SUCCESS] All tests passed!")
    else:
        print(f"\n[WARNING] {test_results['failed']} test(s) failed")

    print("=" * 60)

    return test_results


if __name__ == '__main__':
    run_all_tests()
