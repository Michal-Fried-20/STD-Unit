# michal frid
# 28/04/2020
# test suite

#########################################################################

import ClassTestGMLValidUserAndPassword
import ClassTestGMLInvalidUser
import ClassTestGMLInvalidPassword


# Needed if you would like to run this plan within this file


ClassTestGMLValidUserAndPassword.ClassesGML().enterEmailUserName()

ClassTestGMLInvalidUser.ClassesGML().enterEmailUserName()

ClassTestGMLInvalidPassword.ClassesGML().enterEmailUserName()
