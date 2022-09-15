from django.core import serializers

from units.models import Course
from users.models import CourseStack


def getCourseData(id):
    course = Course.objects.get(id=id)
    classTimesDict = []
    for classtime in course.classTime.all():
        classTimesDict.append({
            'from_hour': classtime.from_hour,
            'to_hour': classtime.to_hour,
            'day': classtime.get_day_display(),
        })
    courseDict = {'name': course.name, 'code': course.code, 'capacity': course.capacity, 'filled': course.filled,
                  'units': course.units, 'master': course.master, 'exam_date': course.exam_date,
                  'exam_hour': course.exam_hour, 'place': course.place, 'coeducational': course.coeducational,
                  'classTimes': classTimesDict}

    return courseDict

