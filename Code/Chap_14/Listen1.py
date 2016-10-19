#-------------------------------------------------------------------------------
#    Name: Listen1.py
#    From: Swing for Jython
#      By: Robert A. (Bob) Gibson [rag]
# ISBN-13: 978-1-4824-0818-2 (paperback)
# ISBN-13: 978-1-4824-0817-5 (electronic)
# website: http://www.apress.com/978148420818
#    Role: Simple Jython Swing script showing how to add a mouse listener to a
#          component
#   Usage: wsadmin -f Listen1.py
#            or
#          jython Listen1.py
# History:
#   date    who  ver   Comment
# --------  ---  ---  ----------
# 14/10/27  rag  0.0  New - ...
#-------------------------------------------------------------------------------

import java
import sys

from   java.awt       import EventQueue
from   java.awt       import FlowLayout

from   java.awt.event import MouseListener

from   javax.swing    import JButton
from   javax.swing    import JFrame
from   javax.swing    import JScrollPane
from   javax.swing    import JTextArea

#-------------------------------------------------------------------------------
# Name: listener()
# Role: Used to monitor Mouse events
#-------------------------------------------------------------------------------
class listener( MouseListener ) :

    #---------------------------------------------------------------------------
    # Name: __init__()
    # Role: Instantiate our MouseListener class
    # Note: In order to access the using component, it needs to be provided
    #---------------------------------------------------------------------------
    def __init__( self, textArea ) :
        self.textArea = textArea

    #---------------------------------------------------------------------------
    # Name: mouseClicked()
    # Role: Log the event
    #---------------------------------------------------------------------------
    def mouseClicked( self, me ) :
        self.logEvent( me )

    #---------------------------------------------------------------------------
    # Name: mouseEntered()
    # Role: Log the event
    #---------------------------------------------------------------------------
    def mouseEntered( self, me ) :
        self.logEvent( me )

    #---------------------------------------------------------------------------
    # Name: mouseExited()
    # Role: Log the event
    #---------------------------------------------------------------------------
    def mouseExited( self, me ) :
        self.logEvent( me )

    #---------------------------------------------------------------------------
    # Name: mousePressed()
    # Role: Log the event
    #---------------------------------------------------------------------------
    def mousePressed( self, me ) :
        self.logEvent( me )

    #---------------------------------------------------------------------------
    # Name: mouseReleased()
    # Role: Log the event
    #---------------------------------------------------------------------------
    def mouseReleased( self, me ) :
        self.logEvent( me )

    #---------------------------------------------------------------------------
    # Name: logEvent()
    # Role: Update the user text area with details of the current event
    #---------------------------------------------------------------------------
    def logEvent( self, me ) :
        self.textArea.append( me.toString() + '\n' )

#-------------------------------------------------------------------------------
# Name: Listen1()
# Role: Used to demonstrate how to create, and display a JFrame instance
# Note: This class should be instantiated on the Swing Event Dispatch Thread
#-------------------------------------------------------------------------------
class Listen1( java.lang.Runnable ) :

    #---------------------------------------------------------------------------
    # Name: run()
    # Role: Instantiate the user class
    # Note: Invoked by the Swing Event Dispatch Thread
    #---------------------------------------------------------------------------
    def run( self ) :
        frame = JFrame(
            'Listen1',
            layout = FlowLayout(),
            locationRelativeTo = None,
            size = ( 512, 256 ),
            defaultCloseOperation = JFrame.EXIT_ON_CLOSE
        )
        self.button   = frame.add( JButton( 'Button' ) )
        self.textarea = JTextArea( rows = 10, columns = 40 )
        self.button.addMouseListener( listener( self.textarea ) )
        frame.add( JScrollPane( self.textarea ) )
        frame.setVisible( 1 )

#-------------------------------------------------------------------------------
#  Name: anonymous
#  Role: Verify that the script was executed, and not imported and instantiate
#        the user application class on the Swing Event Dispatch Thread
#-------------------------------------------------------------------------------
if __name__ in [ '__main__', 'main' ] :
    EventQueue.invokeLater( Listen1() )
    if 'AdminConfig' in dir() :
        raw_input( '\nPress <Enter> to terminate the application:\n' )
else :
    print '\nError: This script should be executed, not imported.\n'
    which = [ 'wsadmin -f', 'jython' ][ 'JYTHON_JAR' in dir( sys ) ]
    print 'Usage: %s %s.py' % ( which, __name__ )
    sys.exit()
