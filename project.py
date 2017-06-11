
from models.db import *


from models.showcategory import *
from models.shownews import *
from models.createnewcategory import *
from models.createnews import *
from models.editnews import *
from models.editcategory import *
from models.deletecategory import *
from models.deletenews import *
from models.login import *
from models.fblogin import *
from models.googlelogin import *
from models.jsonendpoint import *
from models.userhelper import *
from models.disconnect import *


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
