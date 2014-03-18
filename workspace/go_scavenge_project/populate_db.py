import os

def populate():

    user_test1 = add_user(name='scotty', email='scotty@hotmail.com', password='test')
    user_test2 = add_user(name='sarah', email='sarah@hotmail.com', password='test')
    user_test3 = add_user(name='steph', email='steph@hotmail.com', password='test')
    user_test4 = add_user(name='johnny', email='johnny@hotmail.com', password='test')
    user_test5 = add_user(name='clive', email='clive@hotmail.com', password='test')

    add_profile(user=user_test1, picture='', about="I'm Scott")
    add_profile(user=user_test2, picture='', about="I'm Sarah")
    add_profile(user=user_test3, picture='', about="I'm Steph")
    add_profile(user=user_test4, picture='', about="I'm Johnny")
    add_profile(user=user_test5, picture='', about="I'm Clive")

    add_stats(name=user_test1, longest_session=14, max_survivors=22, supplies=112)
    add_stats(name=user_test2, longest_session=2, max_survivors=8, supplies=20)
    add_stats(name=user_test3, longest_session=5, max_survivors=14, supplies=43)
    add_stats(name=user_test4, longest_session=1, max_survivors=5, supplies=10)
    add_stats(name=user_test5, longest_session=0, max_survivors=3, supplies=0)

    #Print whats just been added
        
    for t in Stat.objects.all():
        print "- {0} -".format(str(t))

def add_user(name, email, password):
        u = User.objects.get_or_create(username=name, email=email, password=password)[0]
        return u

def add_profile(user, picture, about):
        p = UserProfile.objects.get_or_create(user=user, picture=picture, about=about)[0]
        return p


def add_stats(name, longest_session, max_survivors, supplies):
        s = Stat.objects.get_or_create(user=name, longest_session=longest_session, max_survivors=max_survivors, supplies=supplies)[0]
        return s

if __name__ == '__main__':
    print "Starting game population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'go_scavenge_project.settings')
    from game.models import UserProfile, Stat
    from django.contrib.auth.models import User
    populate()
