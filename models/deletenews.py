from models.login import *
from models.shownews import *
from models.db import *
from models.userhelper import *


# Delete a news
@app.route('/category/<int:Category_id>/news/<int:news_id>/delete',
           methods=['GET', 'POST'])
@login_required
def deleteNews(Category_id, news_id):
    NewsToDelete = session.query(News).filter_by(id=news_id).one()
    category = session.query(Category).filter_by(id=Category_id).one()

    if request.method == 'POST':
        if NewsToDelete.user_id != login_session['user_id']:
            return redirect(url_for('showNews', Category_id=Category_id))

        session.delete(NewsToDelete)
        session.commit()
        flash('News Successfully Deleted')
        return redirect(url_for('showNews', Category_id=Category_id))
    else:
        return render_template('deletenews.html', NewsToDelete=NewsToDelete)
