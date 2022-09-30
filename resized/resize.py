from image_resizer import sort, Img_resizer, run_save


path = "../image files/"
print(sort(path))
print(sort.__doc__)



path = "../Elijah.jpg/"
print(Img_resizer.__doc__)
Img_resizer(path, name= "resize.jpg")


path = "../"
print(run_save.__doc__)
run_save(path)


