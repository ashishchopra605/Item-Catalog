from models.login import *
from models.showcategory import *
from models.db import *


# Create a new Category
@app.route('/category/new/', methods=['GET', 'POST'])
def newCategory():
    if 'username' not in login_session:
        return redirect('/login')
    if request.method == 'POST':
        newCategory = Category(
            name=request.form['category-name'],
            description=request.form['category-description'],
            imgurl=request.form['category-img'],
            user_id=login_session.get('user_id')
        )
        session.add(newCategory)
        flash('New Category %s Successfully Created' % newCategory.name)
        session.commit()
        return redirect(url_for('shownewscategory'))
    else:
        return render_template('addcategory.html')
