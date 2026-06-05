# Day 4 – Object-Oriented Programming (OOP)

## Objective

Learn the fundamentals of Object-Oriented Programming (OOP) in Python and apply them through practical assignments and a mini Library Management System project.

---

# OOP Concepts Learned

### Class

A blueprint used to create objects.

### Object

An instance of a class that contains its own data and behavior.

### Constructor (`__init__`)

A special method that initializes object data when an object is created.

### Instance Variables

Variables that belong to a specific object.

### Class Variables

Variables shared by all objects of a class.

### Encapsulation

Protecting and controlling access to object data using methods.

### Inheritance

Allows a child class to reuse properties and methods from a parent class.

### Method Overriding

A child class provides its own version of a parent class method.

### Polymorphism

Same method name can perform different actions depending on the object.

### Abstraction

Hides implementation details and forces child classes to implement required methods.

### `super()`

Used to access methods or constructors of a parent class.

### Access Modifiers

* Public → Accessible everywhere
* Protected (`_`) → Intended for internal use
* Private (`__`) → Restricted access

---

# Assignments Completed

## 1. Student Management System

Learned:

* Classes and Objects
* Constructors
* Methods
* Instance Variables

Features:

* Store student details
* Calculate grades
* Display information

---

## 2. Bank Account System

Learned:

* Encapsulation
* Validation

Features:

* Deposit
* Withdraw
* Check Balance

---

## 3. Employee Management

Learned:

* Inheritance

Structure:

```text
Employee
   ↑
Manager
```

---

## 4. Vehicle System

Learned:

* Method Overriding
* Polymorphism

Structure:

```text
Vehicle
├── Car
└── Bike
```

---

## 5. Shape Area Calculator

Learned:

* Abstraction
* Inheritance

Structure:

```text
Shape
├── Rectangle
├── Circle
└── Triangle
```

---

## 6. Library Management System

Classes:

```text
Library
├── Book
└── Member
```

Features:

* Add Books
* Add Members
* Issue Books
* Return Books
* Display Available Books

Concepts Used:

* Classes
* Objects
* Constructors
* Encapsulation
* Composition
* Validation

---

# Key Takeaways

* Every class should have a clear responsibility.
* Protect objects from entering invalid states.
* Use inheritance only when a child **IS-A** parent.
* Use composition when an object **HAS-A** another object.
* Validate data before modifying object state.
* Avoid code duplication through OOP principles.
* Design classes based on responsibilities, not just code organization.

---

# Final Outcome

This assignment helped me understand how to design and build real-world programs using:

* Classes and Objects
* Encapsulation
* Inheritance
* Polymorphism
* Abstraction
* Method Overriding
* Composition
* Validation
* Basic Software Design Principles

These concepts form the foundation of software development, backend systems, web applications, AI systems, and large-scale software projects.
