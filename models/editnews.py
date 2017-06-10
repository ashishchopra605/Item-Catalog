from models.login import *
from models.shownews import *
from models.db import *


# Edit a news
@app.route('/category/<int:Category_id>/news/<int:news_id>/edit',
           methods=['GET', 'POST'])
def editNews(Category_id, news_id):
    if 'username' not in login_session:
        return redirect('/login')
    editedNews = session.query(News).filter_by(id=news_id).one()
    category = session.query(Category).filter_by(id=Category_id).one()
    if request.method == 'POST':
        if request.form['news-heading']:
            editedNews.heading = request.form['news-heading']
        if request.form['news-description']:
            editedNews.description = request.form['news-description']
        if request.form['news-img']:
            editedNews.imgurl = request.form['news-img']

        session.add(editedNews)
        session.commit()
        flash('News Successfully Edited')
        return redirect(url_for('showNews', Category_id=Category_id))
    else:
        return render_template('editnews.html', editedNews=editedNews,
                               category=category)
