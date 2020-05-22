# Code Review

Dear candidate, thank you very much for you submission to the 
Backend Developer Co-op Position.

As a sign of respect and appreciation for the time you spent on this task,
I decided to give you a feedback about your code and I hope that this 
experience will be educational for you.

My feedback does should not imply your acceptance or rejection to the internship 
program. All candidates got a feedback like this.


## My comments

### Best practices:

- Use [requirements.txt] for installing Python packages (e.g. Django)

- Use [.gitignore] to exclude files from the source code you commit into git

- Never commit your DB to git. If you need to create initial data for the project,
  like in this project, use Django's [data migration] scripts or [fixtures]. 

- Extend your templates using [base.html]

### Additional comments

- style.css belongs to the static directory: https://docs.djangoproject.com/en/3.0/howto/static-files/

Additional comments can be found in the code with a comment that starts with `CR:` (i.e. CodeReview)


[requirements.txt]: https://pip.pypa.io/en/stable/user_guide/#requirements-files
[.gitignore]: https://git-scm.com/docs/gitignore
[data migration]: https://docs.djangoproject.com/en/3.0/topics/migrations/#data-migrations
[fixtures]: https://docs.djangoproject.com/en/3.0/howto/initial-data/
[base.html]: https://docs.djangoproject.com/en/3.0/ref/templates/language/#template-inheritance