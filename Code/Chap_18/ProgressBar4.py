#-------------------------------------------------------------------------------
#    Name: ProgressBar4.py
#    From: Swing for Jython
#      By: Robert A. (Bob) Gibson [rag]
# ISBN-13: 978-1-4824-0818-2 (paperback)
# ISBN-13: 978-1-4824-0817-5 (electronic)
# website: http://www.apress.com/978148420818
#    Role: Simple Jython Swing script showing how to use a JProgressBar
#    Note: This example verifies that the progressTask constructor has been
#          provided with a changeHandler value before passing it to the
#          SwingWorker constructor.  Additionally, the JProgressBar constructor
#          has the stringPainted keyword argument specified.
#   Usage: wsadmin -f ProgressBar4.py
#            or
#          jython ProgressBar4.py
# History:
#   date    who  ver   Comment
# --------  ---  ---  ----------
# 14/10/30  rag  0.0  New - ...
#-------------------------------------------------------------------------------

import java
import sys

from   time        import sleep

from   java.awt    import BorderLayout
from   java.awt    import EventQueue
from   java.awt    import Insets

from   java.util   import Random

from   javax.swing import BorderFactory
from   javax.swing import JButton
from   javax.swing import JFrame
from   javax.swing import JPanel
from   javax.swing import JProgressBar
from   javax.swing import SwingWorker

#-------------------------------------------------------------------------------
# Name: progressTask
# Role: Background processing of task that takes a long time...
# Note: Instances of SwingWorker are not reusuable, new ones must be created.
#-------------------------------------------------------------------------------
class progressTask( SwingWorker ) :

    #---------------------------------------------------------------------------
    # Name: __init__()
    # Role: constructor
    #---------------------------------------------------------------------------
    def __init__( self, changeHandler = None ) :
        if changeHandler :
            SwingWorker.__init__( self, propertyChange = changeHandler )
        else :
            SwingWorker.__init__( self )

    #---------------------------------------------------------------------------
    # Name: doInBackground()
    # Role: Call the AdminConfig scripting object in the background
    #---------------------------------------------------------------------------
    def doInBackground( self ) :
        #-----------------------------------------------------------------------
        # Use a (pseudo) random number generator to simulate progress
        #-----------------------------------------------------------------------
        try :
            random   = Random()
            progress = 0
            self.super__setProgress( progress )
            while progress < 100 :
                sleep( ( random.nextInt( 1400 ) + 100 ) / 1000.0 )
                progress = min(
                    progress + random.nextInt( 10 ) + 1, 100
                )
                self.super__setProgress( progress )
        except :
            Type, value = sys.exc_info()[ :2 ]
            print 'Error:', str( Type )
            print 'value:', str( value )
            sys.exit()

    #---------------------------------------------------------------------------
    # Name: done()
    # Role: Called when the background processing completes
    #---------------------------------------------------------------------------
    def done( self ) :
        pass

#-------------------------------------------------------------------------------
# Name: ProgressBar4()
# Role: Used to demonstrate how to create, and display a JFrame instance
# Note: This class should be instantiated on the Swing Event Dispatch Thread
#-------------------------------------------------------------------------------
class ProgressBar4( java.lang.Runnable ) :

    #---------------------------------------------------------------------------
    # Name: run()
    # Role: Instantiate the user class
    # Note: Invoked by the Swing Event Dispatch Thread
    #---------------------------------------------------------------------------
    def run( self ) :
        frame = JFrame(
            'ProgressBar4',
            size = ( 280, 125 ),
            locationRelativeTo = None,
            defaultCloseOperation = JFrame.EXIT_ON_CLOSE
        )
        frame.getContentPane().setBorder(
            BorderFactory.createEmptyBorder( 20, 20, 20, 20 )
        )

        panel = JPanel()
        self.button = panel.add(
            JButton(
                'Start',
                actionPerformed = self.start
            )
        )
        self.progressBar = panel.add(
            JProgressBar( stringPainted = 1 )
        )
        frame.add(
            panel,
            BorderLayout.NORTH
        )
        frame.setVisible( 1 )

    #---------------------------------------------------------------------------
    # Name: start()
    # Role: ActionListener event handler for "start" button
    #---------------------------------------------------------------------------
    def start( self, event ) :
        self.button.setEnabled( 0 )
        task = progressTask( self.propertyUpdate )
        task.execute()

    #---------------------------------------------------------------------------
    # Name: propertyUpdate()
    # Role: PropertyChangeListener event handler for progressTask instance
    #---------------------------------------------------------------------------
    def propertyUpdate( self, event ) :
        if event.getPropertyName() == 'progress' :
            progress = event.getNewValue()
            self.progressBar.setValue( progress )
            if progress == 100 :
                self.button.setEnabled( 1 )

#-------------------------------------------------------------------------------
#  Name: anonymous
#  Role: Verify that the script was executed, and not imported and instantiate
#        the user application class on the Swing Event Dispatch Thread
#-------------------------------------------------------------------------------
if __name__ in [ '__main__', 'main' ] :
    EventQueue.invokeLater( ProgressBar4() )
    if 'AdminConfig' in dir() :
        raw_input( '\nPress <Enter> to terminate the application:\n' )
else :
    print '\nError: This script should be executed, not imported.\n'
    which = [ 'wsadmin -f', 'jython' ][ 'JYTHON_JAR' in dir( sys ) ]
    print 'Usage: %s %s.py' % ( which, __name__ )
    sys.exit()
