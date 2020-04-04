__all__ = ['Ignition']

__productname__ = 'Ignition'
# Expecting trailing "-rcN" or "" for stable releases.
__version__     = "0.0.3"
__copyright__   = "Copyright 2020 Josh L & contributors"
__author__      = "Josh L"
__author_email__= "sillynoodle36@gmail.com"
__description__ = "Hit the ground running on your fresh Ubuntu installation."
__license__  = "Licensed under the GNU GPL v3 or any later version"

#from offlineimap.error import OfflineImapError
# put this last, so we don't run into circular dependencies using
# e.g. offlineimap.__version__.
from ignition.init import Igntition
