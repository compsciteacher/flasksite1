from flask import Flask, render_template, url_for
application=Flask(__name__)

posts=[
    {
        'author':'Howard Davis',
        'title':'Post 1',
        'content':'First post'
    },
    {
        'author' : 'Billy Bob',
        'title' : 'Post 2',
        'content':'First post'
    }
]

@application.route("/")
@application.route("/index")
def home():
    return render_template('home.html',posts=posts)
@application.route("/about")
def about():
    return render_template('about.html',title="About")
# run the application.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production application.
    application.debug = True
    application.run()