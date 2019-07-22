from import_export import resources
from .models import TransLog
from .models import TransSurvey

class TransLogResource(resources.ModelResource):
    class Meta:
        model = TransLog
        fields = ('id', 'person_id', 'Date', 'pick_up_loc', 'drop_off_loc', 'Reason', 'first_time')
        export_order = ('id', 'person_id', 'Date', 'pick_up_loc', 'drop_off_loc', 'Reason', 'first_time')

class TransSurveyResource(resources.ModelResource):
    class Meta:
        model = TransSurvey
        fields = ('id', 'person_id', 'Date', 'Question_1', 'Question_2', 'Question_3', 'Question_4')
        export_order = ('id', 'person_id', 'Date', 'Question_1', 'Question_2', 'Question_3', 'Question_4')
