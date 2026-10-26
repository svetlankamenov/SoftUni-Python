def rectangle(length, width):
    def area():
        rect_area = length * width
        return rect_area

    def perimeter():
        rect_perimeter = 2 * (length + width)
        return rect_perimeter

    if type(length) != int or type(width) != int:
        return "Enter valid values!"
    else:
        return f"Rectangle area: {area()}" + "\n" + f"Rectangle perimeter: {perimeter()}"

print(rectangle(2, 10))
print(rectangle('2', 10))