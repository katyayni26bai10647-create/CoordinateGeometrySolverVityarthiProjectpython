import math
import cmath
print("\n======================================")
print(".    COORDINATE GEOMETRY.               ")
print("========================================")
print("1. Distance Between two points")
print("2. Midpoint of two points")
print("3. Slope of a line")
print("4. Exit")
choice = input("\n Enter your choice: ")
if choice == "1":
   print("\n---DISTANCE BETWEEN TWO POINTS---")
   x1 = float(input("Enter x1: "))
   y1 = float(input("Enter y1: "))
   x2 = float(input("Enter x2: "))
   y2 = float(input("Enter y2: "))
   k = ((x2 - x1)**2 + (y2-y1)**2)**0.5
   print("The distance between two points is" , k)
elif choice == "2":
   print("\n---MIDPOINT OF TWO POINTS---")
   x1 = float(input("Enter x1: "))
   y1 = float(input("Enter y1: "))
   x2 = float(input("Enter x2: "))
   y2 = float(input("Enter y2: "))
   e = (x2 - x1)/2
   n = (y2 - y1)/2
   print("MIDPOINT:", "(" , e , "," , n , ")")
elif choice == "3":
   print("\n---SLOPE OF A LINE---")
   a = float(input("Enter coefficient of x: "))
   b = float(input("Enter coefficient of y: "))
   c = (-1 * a)/ b
   print("Slope of line:" , c)   

   
            