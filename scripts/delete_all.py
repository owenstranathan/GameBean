from GameBean.models import Company, Platform, Game, Review

def deleteAllCompanies():
    for c in Company.objects.all():
        c.delete()

def deleteAllGames():
    for g in Game.objects.all():
        g.delete()

def deleteAllPlatforms():
    for p in Platform.objects.all():
        p.delete()

def deleteAllReviews():
    for r in Review.objects.all():
        r.delete()

def deleteAll():
    deleteAllReviews()
    deleteAllGames()
    deleteAllPlatforms()
    deleteAllCompanies()
