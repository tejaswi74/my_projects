from django.shortcuts import render
def student_list(request):
    students = [
        {'name': 'Teja', 'marks': 95},
        {'name': 'Hema', 'marks': 39},
        {'name': 'Harshitha', 'marks': 85},
        {'name': 'Sri', 'marks': 30},
    ]
    passing_marks = 50 
    return render(request, 'studentapp/student_list.html', {'students': students, 'passing_marks': passing_marks})

