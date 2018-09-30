from fabric.api import local


def all():
  merge()
  prod()


def prod():
  local('ng build --prod')
  local('gcloud app deploy --project=sabya-co-za -q --account=choeysnax@gmail.com --verbosity=info')


def merge():
  local('git push')
