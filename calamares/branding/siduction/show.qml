/* === This file is part of Calamares - <http://github.com/calamares> ===
 *
 *   Copyright 2015, Teo Mrnjavac <teo@kde.org>
 *
 *   Calamares is free software: you can redistribute it and/or modify
 *   it under the terms of the GNU General Public License as published by
 *   the Free Software Foundation, either version 3 of the License, or
 *   (at your option) any later version.
 *
 *   Calamares is distributed in the hope that it will be useful,
 *   but WITHOUT ANY WARRANTY; without even the implied warranty of
 *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 *   GNU General Public License for more details.
 *
 *   You should have received a copy of the GNU General Public License
 *   along with Calamares. If not, see <http://www.gnu.org/licenses/>.
 */

import QtQuick 2.0;
import calamares.slideshow 1.0;

Presentation
{
    id: presentation

    Timer {
        interval: 20000
        running: true
        repeat: true
        onTriggered: presentation.goToNextSlide()
    }
    
    Slide {

        Image {
            id: background1
            source: "slide1.png"
            width: 467; height: 280
            fillMode: Image.PreserveAspectFit
            anchors.centerIn: parent
        }
        Text {
            anchors.horizontalCenter: background1.horizontalCenter
            anchors.top: background1.bottom
            text: "Welcome to siduction.<br/>"
            wrapMode: Text.WordWrap
            width: 800
            horizontalAlignment: Text.Center
        }
    }

    Slide {

        Image {
            id: background2
            source: "slide2.png"
            width: 467; height: 280
            fillMode: Image.PreserveAspectFit
            anchors.centerIn: parent
        }
        Text {
            anchors.horizontalCenter: background2.horizontalCenter
            anchors.top: background2.bottom
            text: "With this little slideshow we present you some old artwork of the last ten years!<br/>"+
                  "This was our first release, One Step Beyond, great artwork (maybe our best) by se7en.<br/>"+
                  "Our logo which we still use, 'siduction - the community based OS', is made by coruja!<br/>"
            wrapMode: Text.WordWrap
            width: 800
            horizontalAlignment: Text.Center
        }
    }

    Slide {

        Image {
            id: background3
            source: "slide3.png"
            width: 467; height: 280
            fillMode: Image.PreserveAspectFit
            anchors.centerIn: parent
        }
        Text {
            anchors.horizontalCenter: background3.horizontalCenter
            anchors.top: background3.bottom
            text: "This is our second release, Desperado, with the spagetti-western theme by hendrikL and the splash screen by se7en.<br/>"
            wrapMode: Text.WordWrap
            width: 800
            horizontalAlignment: Text.Center
        }
    }

    Slide {

        Image {
            id: background4
            source: "slide4.png"
            width: 467; height: 280
            fillMode: Image.PreserveAspectFit
            anchors.centerIn: parent
        }
        Text {
             anchors.horizontalCenter: background4.horizontalCenter
             anchors.top: background4.bottom
             text: "Our fourth release, Riders On The Storm, artwork by se7en with some modifications for our first christmas-release by hendrikL.<br/>"
             wrapMode: Text.WordWrap
             width: 800
             horizontalAlignment: Text.Center
        }
    }

    Slide {

        Image {
            id: background5
            source: "slide5.png"
            width: 467; height: 280
            fillMode: Image.PreserveAspectFit
            anchors.centerIn: parent
        }
        Text {
            anchors.horizontalCenter: background5.horizontalCenter
            anchors.top: background5.bottom
            text: "This was our fifth release, Firestarter, artwork by hendrikL<br/>"+
                  "As you may have found out, we used song names for our releases back in those days.<br/>"
            wrapMode: Text.WordWrap
            width: 800
            horizontalAlignment: Text.Center
        }
    }

    Slide {

        Image {
            id: background6
            source: "slide6.png"
            width: 467; height: 280
            fillMode: Image.PreserveAspectFit
            anchors.centerIn: parent
        }
        Text {
            anchors.horizontalCenter: background6.horizontalCenter
            anchors.top: background6.bottom
            text: "This was our christmas special, steam edition, back in 2014.<br/>"+
                  "Artwork, background by bob, which is still in use and as it was for christmas the modifications made by hendrikL.<br/>"
            wrapMode: Text.WordWrap
            width: 800
            horizontalAlignment: Text.Center
        }
    }

    Slide {

        Image {
            id: background7
            source: "slide7.png"
            width: 467; height: 280
            fillMode: Image.PreserveAspectFit
            anchors.centerIn: parent
        }
        Text {
            anchors.horizontalCenter: background7.horizontalCenter
            anchors.top: background7.bottom
            text: "Also, we want to thank all the people who helped to start this project and adventure 'siduction'!<br/>"+
                  "Have fun and <b>'apt moo'<b/>!<br/>"
            wrapMode: Text.WordWrap
            width: 800
            horizontalAlignment: Text.Center
        }
    }
}
