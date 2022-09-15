from users.models import CourseStack


def getCourseStackData(stack_id):
    courseStack = CourseStack.objects.get(id=stack_id).courses.all().order_by('-row')
    courseStackData = []
    for course in courseStack:
        courseStackData.append({
            'row': course.row,
            'course': course.course.name,
            'course_code': course.course.code,
            'course_id': course.course.id,
        })

    return courseStackData
