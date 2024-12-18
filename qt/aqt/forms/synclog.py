from typing import TYPE_CHECKING

from aqt.qt import qtmajor

if qtmajor > 5 or TYPE_CHECKING:
    from _aqt.forms.synclog_qt6 import *
else:
    from _aqt.forms.synclog_qt5 import *  # type: ignore
