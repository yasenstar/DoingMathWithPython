 Doing Math with Python

Sample solutions of program challenges:https://nostarch.com/doingmathwithpython


# 00 Introduction

## Tip: how to clear screen

### Terminal in VS Code

#### import os
# Clearing the Screen
os.system('cls')

### Python IDLE (tricky way)

#### def cls(): print("\n" * 40)
cls()

# 01 Working with Numbers

Within this chapter:

- you learn to write programs that recognize integers, floating point numbers, fractional numbers (expressed as a fraction or a floating point number), and complex numbers.
- you write programs that generate multiplication tables, perform unit conversions, and find the roots of a quadratic equation


## 01-01 Basic Mathematical Operations

### addition (+)

### subtraction (-)

### multiplication (*)

### division (/)

#### floor division (//)

#### modulo (%)

### exponential (**)

#### square root: x ** (1/2)

#### cube root: x ** (1/3)

### Python will evaluate the expression following the standard PEMDAS rule for the order of calculations

#### PEMDAS: Parentheses, Exponents, Multiplications, division, addition, subtraction

## 01-02 Labels: Attaching Names to Numbers

## 01-03 Different Kinds of Numbers

### Data Type

#### Use type() to check the kind of number (or variable)

#### int(), float(), etc.. used to convert the data type

### 01-03-01 Working with Fractions

#### from fractions import Fraction

#### <class 'fractions.Fraction'>

#### Fraction(a,b) or Fraction(a/b) ==>
Fraction(numerator, denominator)

### 01-03-02 Complex Numbers

#### <class 'complex'>: a+bj

#### .real and .imag: get real and imaginary part separately

#### .conjugate(): same real part but an imaginary part with an equal magnitude and an opposite sign

#### magnitude of a complex number:
(z.real ** 2 + z.imag ** 2) ** 0.5  <--> abs(z)

## 01-04 Getting User Input

### 01-04-01 Handling Exceptions and Invalid Input

#### try:
    STATEMENT
except ErrorType:
    print("customized error message")

### 01-04-02 Fractions and Complex Numbers as Input

#### a = Fraction(input('Enter a fraction: '))

#### z = complex(input('Enter a complex number: '))

## 01-05 Writing Programs that Do the Math for you

### 01-05-01 Calculating the Factors of an Integer

#### 01-01_is_factor_checking.py

#### 01-02_factors-finder.py

### 01-05-02 Generating Multiplication Tables

#### 01-03_linear-multiplication-table.py

#### 01-04_Chinese-multiplication-table.py

#### 01-05_Chinese-multiplication-table-new.py

### 01-05-03 Converting Units of Measurement

#### 01-06_mile-km-converter.py

#### 01-07_temperature-converter.py

### 01-05-04 Finding the Roots of a Quadratic Equation

#### 01-08_quadratic-equation-roots-calculator.py

## 01-06 Programming Challenges

### 1. Even-Odd Vending Machine

#### 01-09_even-odd-vending-machine.py

### 2. Enhanced Multiplication Table Generator

#### 01-10_enhanced-multiplication-table.py
 (see:01-05-02 Generating Multiplication Tables)
### 3. Enhanced Unit Converter

#### 01-11_enhanced-unit-converter.py
 (see:01-05-03 Converting Units of Measurement)
### 4. Fraction Calculator

#### 01-12_fraction-calculator.py
 (see:01-03-01 Working with Fractions)
### 5. Give Exit Power to the User

#### 01-13_run-until-exit.py

#### 01-14_enhanced-unit-converter-with-exit.py
 (see:3. Enhanced Unit Converter)
# 02 Visualizing Data with Graphs

## 02-01 Understanding the Cartesian Coordinate Plane

## 02-02 Working with Lists and Tuples

### 02-02-01 Iterating over a List or Tuple

## 02-03 Creating Graphs with Matplotlib

### 02-03-01 Marking Points on Your Graph

### 02-03-02 Graphing the Average Annual Temperature

### 02-03-03 Comparing the Monthly Temperature Trends

### 02-03-04 Customizing Graphs

### 02-03-05 Saving the Plots

## 02-04 Plotting with Formulas

### 02-04-01 Newton's Law of Universal Gravitation

### 02-04-02 Projectile Motion

## 02-05 Programming Challenges

### 1. How Does the Temperature Vary

### 2. Explorting a Quadratic Function Visually

### 3. Enhanced Projectile Trajectory Comparison

### 4. Visualizing Your Expenses

### 5. Exploring the Relationship

# 03 Describing Data with Statistics

## 03-01 Finding the Mean

## 03-02 Finding the Median

## 03-03 Finding the Mode and Creating a Frequency Table

### 03-03-01 Finding the Most Common Elements

### 03-03-02 Finding the Mode

### 03-03-03 Creating a Frequency Table

## 03-04 Measuring the Dispersion

### 03-04-01 Finding the Range of a Set of Numbers

### 03-04-20 Finding the Variance and Standard Deviation

## 03-05 Calculating the Correlation Between Two Data Sets

### 03-05-01 Calculating the Correlation Coefficient

### 03-05-02 High School Grades and Performance on College

## 03-06 Scatter Plots

## 03-07 Reading Data from Files

### 03-07-01 Reading Data from a Text File

### 03-07-02 Reading Data from a CSV File

## 03-08 Programming Clallenges

### 1. Better Correlation Coefficient

### 2. Statistics Calculator

### 3. Experiment with other CSV Data

### 4. Finding the Percentile

### 5. Creating a Grouped Frequency Table

# 04 Algebra and Symbolic Math with Sympy

## 04-01 Defining Symbols and Symbolic Operations

## 04-02 Working with Expressions

### 04-02-01 Fractorizing and Expanding Expressions

### 04-02-02 Pretty Printing

### 04-02-03 Substituting in Values

### 04-02-04 Converting Strings to Mathematical Expressions

## 04-03 Solving Equations

### 04-03-01 Solving Quadratic Equations

### 04-03-02 Solving for One Variable in Terms of Others

### 04-03-03 Solving a System of Linear Equations

## 04-04 Plotting Using Sympy

### 04-04-01 Plotting Expressions Input by the User

### 04-04-02 Plotting Multiple Functions

## 04-05 Programming Challenges

### 1. Factor Finder

### 2. Graphical Equation Solver

### 3. Summing a Series

### 4. Solving Single-Variable Inequalities

# 05 Playing with Sets and Probability

## 05-01 What's a Set?

### 05-01-01 Set Construction

### 05-01-02 Subsets, Supersets, and Power Sets

### 05-01-03 Set Operations

## 05-02 Probability

### 05-02-01 Probability of Event A or Event B

### 05-02-02 Probability of Event A and Event B

### 05-02-03 Generating Random Numbers

### 05-02-04 Nonuniform Random Numbers

## 05-03 Programming Challenges

### 1. Using Venn Diagrams to Visualize Relations

### 2. Law of Large Numbers

### 3. How Many Tosses Before you Run Out

### 4. Shuffling a Deck of Cards

### 5. Estimating the Area of a Circle

# 06 Drawing Geometric Shapes and Fractals

## 06-01 Drawing Geometric Shapes with Matplotlib's Patches

### 06-01-01 Drawing a Circle

### 06-01-02 Creating Animated Figures

### 06-10-03 Animating a Projectile's Trajectory

## 06-02 Drawing Fractals

### 06-02-01 Transformations of Points in a Plane

### 06-02-02 Drawing the Barnsley Fern

## 06-03 Programming Challenges

### 1. Packing Circles into a Square

### 2. Drawing the Sierpinski Triangle

### 3. Exploring Henon's Function

### 4. Drawing the Mandelbrot Set

# 07 Solving Calculus Problems

## 07-01 What is a Function?

### 07-01-01 Domain and Range of a Function

### 07-01-02 An Overview of Common Mathematical Functions

## 07-02 Assumptions in SymPy

## 07-03 Finding the Limit of Functions

### 07-03-01 Continuous Compound Interest

### 07-03-02 Instantaneous Rate of Change

## 07-04 Finding the Derivative of Functions

### 07-04-01 A Derivative Calculator

### 07-04-02 Calculating Partial Derivatives

## 07-05 Higher-Order Derivatives and Finding the Maxima

## 07-06 Finding the Global Maximum Using Gradient Ascent

### 07-06-01 A Generic Program for Gradient Ascent

### 07-06-02 A Word of Warning About the Initial Value

### 07-06-03 The Role of the Step Size and Epsilon

## 07-07 Finding the Integrals of Functions

## 07-08 Probability Density Functions

## 07-09 Programming Challenges

### 1. Verify the Continuity of the Function

### 2. Implement the Gradient Descent

### 3. Area Between Two Curves

### 4. Finding the Length of a Curve
