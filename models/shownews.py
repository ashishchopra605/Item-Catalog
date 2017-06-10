from models.userhelper import *
from models.db import *


# Show news
@app.route('/category/<int:Category_id>/')
@app.route('/category/<int:Category_id>/news/')
def showNews(Category_id):
    category = session.query(Category).filter_by(id=Category_id).one()
    creator = getUserInfo(category.user_id)
    news = session.query(News).filter_by(
        category_id=Category_id).all()
    if 'username' not in login_session or creator.id != login_session['user_id']:
        return render_template(
            'publicnews.html',
            news=news,
            Category=category,
            creator=creator)
    else:
        return render_template(
            'news.html',
            news=news,
            Category=category,
            creator=creator
        )
