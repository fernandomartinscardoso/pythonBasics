# Basic Concepts

This file contains auxiliary general information to support the reading of the [readme file](readme.md).

## NaN and Nat

In computing and data analysis contexts, NaN stands for "Not a Number" and NaT stands for "Not a Time".

### NaN: Not a Number

- __Definition__: `NaN` is a special value used in computing (especially in floating-point arithmetic following the IEEE 754 standard) to represent an undefined or unrepresentable numerical value.
- __Common Causes__: It typically results from invalid mathematical operations, such as:
  - Dividing zero by zero (\(0/0\)).
  - Taking the square root of a negative number (since the result is an imaginary number, not a real number).
  - Performing arithmetic operations on non-numeric values.
- __Usage__: In data science libraries like `pandas` and `NumPy`, `NaN` is also used as a placeholder for general missing or null numerical data.

### NaT: Not a Time

- __Definition__: `NaT` is the datetime equivalent of `NaN`, specifically designed to represent missing, null, or undefined values in date and time data.
- __Usage__: It is primarily used within the `pandas` library for Python when working with time-series data or columns formatted as `datetime` or `timedelta` objects.
- __Function__: Like `NaN`, `NaT` helps maintain data integrity within a structured dataset, ensuring that missing time values are handled consistently without causing errors in calculations.

## API

An API (Application Programming Interface) is a set of rules and protocols that allows two different software programs to communicate and exchange data with each other. It acts as a messenger or a middleman, enabling applications to access functionality or data from other services without needing to know the internal workings of the other system.

### How an API Works (The Restaurant Analogy)

A common way to understand an API is to think of a restaurant:

- __You (the client application)__: The application that needs information or wants an action performed (e.g., a weather app that needs the current temperature).
- __The kitchen (the server)__: The external system that has the data or can perform the action (e.g., the weather bureau's database).
- __The waiter (the API)__: The intermediary that takes your order (request), delivers it to the kitchen, brings the prepared order (response) back to you, and ensures the communication follows a specific format (the menu and ordering rules).

### Key Concepts

- __Abstraction__: APIs simplify complexity by exposing only the necessary parts for developers to use, hiding the underlying details of how a system works.
- __Request and Response Cycle__: Communication happens through a standardized process where a client sends a request (often using HTTP methods like `GET` to retrieve data or `POST` to send data) to a specific URL (an __endpoint__), and the server sends back a response, usually in a structured format like JSON or XML.
- __Documentation__: An API is accompanied by documentation (like a menu) that explains how developers should format requests, what data can be exchanged, and what responses to expect.
