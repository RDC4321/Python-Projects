# Python Projects

Hello!  
This repository contains Python projects I’ve built while learning and practicing Python — from beginner fundamentals to intermediate, object-oriented programs.

The goal of this repo is to:
- Strengthen Python fundamentals
- Practice problem-solving and logic
- Build small but complete programs from scratch
- Progress from procedural code to clean OOP design

---

## Beginner Level Projects

### 1. Ordering System
Simulates an online ordering system.  
**Concepts:** if/elif/else, f-strings

### 2. Ticketing System
Online ticketing simulation that produces different outputs based on user input.  
**Concepts:** conditional logic

### 3. Text-Based Adventure Game
Choose-your-own-adventure style game using nested conditionals.  
**Concepts:** nested if/elif

### 4. Lottery Game
Simple lottery simulator.  
**Concepts:** random module

#### 4.1 Random Module (User Input)
User defines the range for random number generation.

### 5. Heads or Tails
Coin toss simulation.  
**Concepts:** random, logical operators

### 6. Rock Paper Scissors (V1)
User vs computer Rock–Paper–Scissors game.  
**Concepts:** lists, conditionals, random

### 6.1 Rock Paper Scissors (V2)
Same game with a different logic structure.

### 7. Basic Roulette
Lottery/roulette simulation.  
**Concepts:** lists, append, random

### 7.1 List Append & Extend Tests
Experiments with list modification.

### 7.2 List Methods & Nested Lists
Further practice with lists and nested lists.

### 8. FizzBuzz
Classic FizzBuzz challenge.  
**Concepts:** for loops, conditionals

### 9. Random Password Generator
Generates passwords based on user preferences.  
**Concepts:** loops, lists, random

### 9.1 Dice Roll Simulator
Simulates dice rolls and tracks how often 6 appears.

### 10. Hangman
Text-based Hangman game.  
**Concepts:** loops, lists, booleans, random

#### 10.1 Hangman (With ASCII Art)
Revised version with ASCII art and external resources.  
**Resource file:** `hangman_resources.py`

### 11. Caesar Cipher
Encrypts/decrypts messages using Caesar Cipher logic.  
**Concepts:** functions, loops, conditionals

### 12. Student Grading Program
Converts numerical grades into descriptive grades.  
**Concepts:** dictionaries

### 13. Secret Auction Program
Simulates a blind auction and determines the highest bidder.  
**Concepts:** dictionaries, loops

### 14. Simple Calculator
Calculator that supports chained operations.  
**Concepts:** functions, dictionaries, loops  
**Resource file:** `calcu_resources.py`

### 15. Blackjack Capstone Project
Blackjack game against a computer dealer.  
**Concepts:** functions with returns, loops, lists, conditionals

### 16. Prime Number Checker
Checks whether a number is prime.  
**Concepts:** scope, functions

### 17. Number Guessing Game (V1)
Guess a number between 1–100 with limited attempts.  
**Concepts:** loops, conditionals  
**Resource file:** `number_guess_resources.py`

### 17.1 Number Guessing Game (V2)
Improved version using multiple functions and constants.

### 18. Higher / Lower Game
Guess which option has more followers.  
**Concepts:** dictionaries, functions, loops, random  
**Resource file:** `higher_lower_data.py`

---

## Intermediate Level Projects

### 19. Coffee Machine (Procedural)
A command-line coffee machine simulation.

**Features:**
- Espresso / Latte / Cappuccino selection
- Resource management (water, milk, coffee)
- Coin processing & change handling
- Profit tracking
- Report & refill commands
- Safe checks for insufficient resources or money

**Concepts Used:**
- Nested dictionaries
- State management
- Control flow
- Input validation
- Debugging logic & indentation

---

### 20. Turtle Graphics (OOP & Loops)
Visual drawing project using Python’s `turtle` module.  
**Concepts:** OOP, loops, angles, randomness, graphics

---

### 21. PrettyTable (OOP & External Package)
Simple table output using the PrettyTable package.  
**Concepts:** third-party packages, classes, object methods

---

### 22. Coffee Machine (Object-Oriented Programming)
A command-line coffee machine simulation rebuilt using Object-Oriented Programming (OOP).

**Features:**
- Espresso / Latte / Cappuccino selection
- Ingredient resource tracking (water, milk, coffee)
- Coin-based payment system
- Change handling
- Profit tracking
- Report & shutdown commands

**OOP Design:**
- **MenuItem** – Represents a single drink
- **Menu** – Manages available drinks
- **CoffeeMaker** – Handles resources & preparation
- **MoneyMachine** – Processes payments
- **main.py** – Controls program flow

**Concepts Used:**
- Object-Oriented Programming (OOP)
- Classes & objects
- State management
- Multi-file project design

---

### 23. Command-Line Quiz Engine (OOP)
A command-line **True/False quiz engine** built using Object-Oriented Programming.

**Features:**
- Dynamic question loading from external data
- Question-by-question progression
- Case-insensitive answer checking
- Real-time score tracking
- Final score summary

**Project Structure:**
- **Question** – Represents a single question
- **QuizBrain** – Manages quiz flow, scoring, and logic
- **main.py** – Controls program execution and looping

**Concepts Used:**
- Object-Oriented Programming (OOP)
- Classes & objects
- Boolean logic
- While loops & state control
- Multi-file Python project architecture

---

### 24. Generative Geometry (Turtle Graphics)
A Python Turtle project that dynamically generates and overlays multiple regular polygons with randomized RGB colors.
This project demonstrates mathematical angle calculation, nested loops, and basic generative art techniques.

**Features**
- Draws polygons from 3 sides (triangle) to 10 sides (decagon)
- Automatically calculates turning angle using:
  angle = 360 / number_of_sides

- Applies a random RGB color to each shape
- Overlays all polygons from the same starting position
- Animates the drawing process using Turtle speed control

**Concepts Used:**
- Nested loops
- Mathematical geometry (360° rule)
- RGB color generation
- Randomization
- Turtle graphics
- Programmatic shape generation

**Core Logic**

Outer loop:
- Controls number of sides (3–10)
  
Inner loop:
- Draws one complete polygon

---

### 24.1 Heatmap Random Walk (Structured Movement)
A structured random walk visualization built using Python Turtle Graphics.
This project expands on turtle movement by introducing directional constraints and dynamic color mapping based on distance from the origin.

**Features**
- Grid-based random walk (0°, 90°, 180°, 270°)
- Prevents immediate 180° reversals (no jitter backtracking)
- Distance-based RGB heatmap scaling
- Smooth gradient from green (center) to red (outer range)
- Distance clamping to control gradient sensitivity
- Modular function design (`color()` and `direct()`)
- Persistent center marker overlay

**Concepts Used**
- Geometry (Pythagorean distance formula)
- Scaling values into RGB range (0–255)
- List filtering & control logic
- Pure functions and modular design
- Separation of simulation logic and UI elements
- Procedural art principles

**Visual Logic**
- 🟢 Green → Near origin  
- 🟡 Yellow → Mid-range  
- 🔴 Red → Far from origin  
The turtle's color dynamically updates after each move based on its distance from the center, creating a heatmap-style procedural visualization.
This project demonstrates progression from basic turtle graphics to structured movement systems and behavior-based visual rendering.
---

## About This Repository
This repository documents my progression from beginner Python fundamentals to intermediate object-oriented programming and structured, multi-file project design.
