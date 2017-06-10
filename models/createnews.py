from models.login import *
from models.shownews import *
from models.db import *


# Create a new news
@app.route('/category/<int:Category_id>/news/new/', methods=['GET', 'POST'])
def newNews(Category_id):
    if 'username' not in login_session:
        return redirect('/login')
    category = session.query(Category).filter_by(id=Category_id).one()
    if request.method == 'POST':
        newNews = News(
            heading=request.form['news-heading'],
            description=request.form['news-description'],
            imgurl=request.form['news-img'],
            category_id=Category_id,
            user_id=category.user_id
        )
        session.add(newNews)
        session.commit()
        flash('New News %s Successfully Created' % (newNews.heading))
        return redirect(url_for('showNews', Category_id=Category_id))
    else:
        return render_template('addnews.html', category=category)
