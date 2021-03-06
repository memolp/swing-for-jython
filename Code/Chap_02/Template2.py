#-------------------------------------------------------------------------------
#    Name: Template2.py
#    From: Swing for Jython
#      By: Robert A. (Bob) Gibson [rag]
# ISBN-13: 978-1-4824-0818-2 (paperback)
# ISBN-13: 978-1-4824-0817-5 (electronic)
# website: http://www.apress.com/978148420818
#    Role: Provide a sample / example Jython script template that may be used
#          to build Swing applications.  This example has the Template2 class
#          based upon the java.lang.Runnable class.
#   Usage: wsadmin -f Template2.py
#            or
#          jython Template2.py
# History:
#   date    who  ver   Comment
# --------  ---  ---  ----------
# 14/10/21  rag  0.0  New - ...
#-------------------------------------------------------------------------------

import java
import sys
from   java.awt    import EventQueue
from   javax.swing import JFrame

#-------------------------------------------------------------------------------
# Name: Template2()
# Role: Used to demonstrate how to create, and display a JFrame instance
# Note: This class should be instantiated on the Swing Event Dispatch Thread
#-------------------------------------------------------------------------------
class Template2( java.lang.Runnable ) :

    #---------------------------------------------------------------------------
    # Name: run()
    # Role: Instantiate the user class
    # Note: Invoked by the Swing Event Dispatch Thread
    #---------------------------------------------------------------------------
    def run( self ) :
        frame = JFrame( 'Title' )
        frame.setDefaultCloseOperation( JFrame.EXIT_ON_CLOSE )
        frame.pack()
        frame.setVisible( 1 )

#-------------------------------------------------------------------------------
#  Name: anonymous
#  Role: Verify that the script was executed, and not imported and instantiate
#        the user application class on the Swing Event Dispatch Thread
#-------------------------------------------------------------------------------
if __name__ in [ '__main__', 'main' ] :
    EventQueue.invokeLater( Template2() )
    if 'AdminConfig' in dir() :
        raw_input( '\nPress <Enter> to terminate the application: ' )
else :
    print '\nError: This script should be executed, not imported.\n'
    if 'JYTHON_JAR' in dir( sys ) :
        print 'jython %s.py' % __name__
    else :
        print 'Usage: wsadmin -f %s.py' % __name__
    sys.exit()