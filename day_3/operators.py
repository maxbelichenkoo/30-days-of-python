#task 1-3
age = int(18)
height = float(177)
complexnum = complex(1 + 1j)

#task 4
base = input("Enter base: ")
height = input("Enter height: ")
area = 0.5 * int(base) * int(height)
print("The area of the triangle is ", area)

#task 5
side_a = input("Enter side a: ")
side_b = input("Enter side b: ")
side_c = input("Enter side c: ")
perim = int(side_a) + int(side_b) + int(side_c)
print("The perimeter of the triangle is ", perim)

#task 6
rect_length = input("Enter length: ")
rect_width = input("Enter width: ")
area = int(rect_length) * int(rect_width)
perimeter = 2 * (int(rect_length) + int(rect_width))
print("The area of the triangle is ", area)
print("The perimeter of the triangle is ", perimeter)

#task 7
circle_radius = input("Enter radius: ")
pi = float(3.14)
area = float(pi) ** int(circle_radius)
circumference = 2 * (float(pi) * int(circle_radius))
print("The area of the circle is ", area)
print("The circumference of the triangle is ", circumference)

#task 8
m = 2
y_intercept = -2
x_intercept = -y_intercept / m


print(f"Slope: {m}")
print(f"Y-intercept: (0, {y_intercept})")
print(f"X-intercept: ({x_intercept}, 0)")

#task 9
x1, y1 = 2, 2
x2, y2 = 6, 10

slope = (y2 - y1) / (x2 - x1)

euclidean_distance = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

#task 10
 
slope_8 = 2
slope_9 = 2
print(slope_8 == slope_9)

#task 11

x = -3
y = x**2 + 6 * x + 9
print(f"When x = {x}, y = {y}")

#task 12
python = len("python")
dragon = len("dragon")
print(python > dragon)

#task 13
print("on" in "python" and "on" in "dragon")

#task 14
print("jargon" in "I hope this course is not full of jargon")

#task 15
print("on" not in "python" and "on" not in "dragon")

#task 16
leng = len("python")
print(float(leng))

#task 17
number = int(input("Enter a number: "))
print(number % 2 == 0)

#task 18
print(7 // 3 == int(2.7))

#task 19
print(type("10") == type(10))

#task 20
print(int(float("9.8")) == 10)

#task 21
hours = input("Enter hours: ")
rate = input("Enter rate per hour: ")
print(int(hours) * int(rate))

#task 22
years = input("Enter number of years you have lived: ")
sec = int(years) * 365 * 24 * 60 * 60
print(f"You have lived for {sec} seconds")

#task 23
print(f"1 1 1 {1 ** 2} {1 ** 3}")
print(f"2 1 2 {2 ** 2} {2 ** 3}")
print(f"3 1 3 {3 ** 2} {3 ** 3}")
print(f"4 1 4 {4 ** 2} {4 ** 3}")
print(f"5 1 5 {5 ** 2} {5 ** 3}")