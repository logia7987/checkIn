from django.db import models

# Create your model
class MyEvent(models.Model):
    LATE = 'LA'
    EARLY = 'EA'
    ABSEN = 'AB'
    OUT = 'OU'
    ATTEND_CHOICE = (
        (LATE, '지각'),
        (EARLY, '조퇴'),
        (ABSEN, '결석'),
        (OUT, '외출')
    )
    attend = models.CharField(
        max_length=2,
        choices=ATTEND_CHOICE,
    )
    usr = models.ForeignKey('auth.User')
    event_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        get_latest_by = 'event_date'


class Group(models.Model):
    CLASS202 = '202'
    CLASS203 = '203'
    CLASS_CHOICE = (
        (CLASS202, '202반'),
        (CLASS203, '203반')
    )
    group = models.CharField(
        max_length=3,
        choices=CLASS_CHOICE,
    )
    usr = models.ForeignKey('auth.User')
    unit = models.PositiveIntegerField()
    limit = models.PositiveIntegerField(default=20)