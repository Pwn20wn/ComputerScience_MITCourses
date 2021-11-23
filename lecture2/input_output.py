#if you use a comma, python will insert a space
#if you don't want a space you can use the "+" to concat and it'll do exactly what you tell it
#everything will have to be a string for comment 2

x = 1
print(x)
x_str = str(x)
#will have a space between everything because of comma
print("my fav number is", x, ".", "x=", x)
print("my fav number is", x_str + "." + "x=" + x_str)
#concat everywhere
print("my fav number is" + x_str + "." + "x=" + x_str)

num = input("type a number....:")
print(5*num)

num = int(input("type a number....:"))
print(5*num)