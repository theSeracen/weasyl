from sqlalchemy.orm import relationship

from libweasyl import staff
from libweasyl.models.meta import Base
from libweasyl.models.users import Login
from libweasyl.models import tables


class SiteUpdate(Base):
    __table__ = tables.siteupdate

    owner = relationship(Login, backref='siteupdate')

    def get_display_owner(self):
        if self.wesley and staff.WESLEY is not None:
            wesley = Login.query.get(staff.WESLEY)
            if wesley is not None:
                return wesley

        return self.owner


class SavedNotification(Base):
    __table__ = tables.welcome

    owner = relationship(Login, backref='saved_notifications')
