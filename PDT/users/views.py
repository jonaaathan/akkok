from django.shortcuts import render
from users.forms import UserForm, UserProfileForm
from django.http import HttpResponse
from django.template import RequestContext, loader
from users.models import UserProfile

def index(request):
    
    manager_list = UserProfile.objects.all()[:5]
    context = {'manager_list': manager_list}
    return render(request, 'users/index.html', context)
    
def register(request):
	#get request's context
	#context = RequestContext(request)
	#return HttpResponse("hello , looking for register ?")
	# A book for telling whether the registrtoin was successgul
	registered = False
	'''
	#if it is a HTTP POST, we are interested in processing form data
	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()

			#hash password
			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit=False) # becoz we need to set user attibutes ourselves
			profile.user = user

			profile.save()

			registered = True
		else:
			print user_form.errors, profile_form.errors	
	else: # not HTTP POST, but render tow ModelForms for user Input
	'''
	user_form = UserForm()
	profile_form = UserProfileForm()
	context = {'user_form' : user_form, 'profile_form': profile_form, 'registered': registered}
	return render(request, 'users/register.html', context)
	#return render_to_response('users/register.html', {'user_form' : user_form, 'profile_form': profile_file, 'registered': registered}, context)
	#give context in the last argument of render_to_request
# Create your views here.
'''
def login(request):
	loginname = Manager.objects.all()
	context={'loginname' : loginname}
	return render(request, 'users/login.html', context)
	'''