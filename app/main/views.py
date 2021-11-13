from flask_login import login_required
from . import main

@main.route('/new/blog/', methods=['GET','POST'])
@login_required
def new_blog():
    
