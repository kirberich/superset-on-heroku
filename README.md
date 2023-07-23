# [superset](https://github.com/airbnb/superset) on [Heroku](http://heroku.com)

Superset is a data exploration platform designed to be visual, intuitive, and interactive. Visit the project's website at <http://airbnb.io/superset>

This fork is set up with poetry for dependency management along with a few other niceties for running on heroku

## Deployment

Instead of deploying with a button, this repository assumes deployment to heroku via the git workflow.

* Set up a heroku app
* Add a postgres database
* Set a SECRET_KEY environment variable
* Specify your git repo as a source for auto deployment