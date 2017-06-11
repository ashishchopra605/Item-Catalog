'''
  this file contains show news category function.
'''

from models.db import *


# Show all news_category
@app.route('/')
@app.route('/category/')
def shownewscategory():
    news_category = session.query(Category).order_by(asc(Category.name))

    if 'username' not in login_session:
        return render_template('publiccategory.html',
                               news_category=news_category)
    else:
        return render_template('category.html', news_category=news_category)
