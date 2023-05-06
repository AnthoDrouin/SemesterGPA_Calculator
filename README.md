# SemesterGPA_Calculator

This small code was originally created for my friend who wanted a better way to optimize their GPA and to know which courses should have a pass mention or should be kept. Please note that this is a small project made for fun. It should not be taken seriously.

## How to use it ?

First, define an object </code> Semester() </code>. After that, you can simply add your GPA for each semester and their respective credits. For instance, one might do :



```
my_semester = Semester()
my_semester.append((4, 15))
my_semester.append((4.33, 12))
```

At any point, one can :

```
my_semester.get_gpa()
```
This function should return your current GPA. After that, you can definie a dictionary for your current semester that you want to optimize. To do so, you create a dict where the key is the name of your course and the item is a tuple containing your GPA for this course and the credit of this course :
```
current_semester = {
'PHY1' : (4.33, 3)
'PHY2' : (3.67, 1)
}
```
Your GPA can then be easily optimize :
```
my_semester.optimize_gpa(current_semester)
```
#### Enjoy!
