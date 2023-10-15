
def validate_cv_fields(request):

    data_cv = dict(request.json)
    data_cv.get('basicInfo', None)
    return 0, []