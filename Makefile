run-dev:
	export FLASK_APP=manage.py && export FLASK_ENV=development && export APP_SETTINGS='projects.config.DevelopmentConfig' && flask run