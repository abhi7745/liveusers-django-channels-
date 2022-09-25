from accounts.models import User_Account

def global_dict(request):
    mydata = User_Account.objects.all()
    return {'mydata': mydata}