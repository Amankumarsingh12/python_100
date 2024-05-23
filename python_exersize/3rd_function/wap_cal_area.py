def paint(height,width,coverage):
    return (height * width) / coverage



h=int(input("height of wall:" ))
w=int(input("width of wall: "))
coverage=5

nu_can = round(paint(h,w,coverage)+0.5)

print(f"you need {nu_can}")
