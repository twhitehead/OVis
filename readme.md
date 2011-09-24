OVis: Orlando Visualization Software
====================================

Orlando: Women’s Writing in the British Isles from the Beginnings to the Present (ed. Brown, Clements and Grundy; published version at [orlando.cambridge.org](http://orlando.cambridge.org/)) is an extensive literary historical textbase that provides a rich testbed for XML data mining and visualization. An experiment in the use of custom, domain-specific XML markup to support new ways of engaging in and supporting scholarly enquiry, it comprises more than 1,200 core entries treating the lives and writing careers of British women writers and other writers; 13,000+ free-standing chronology entries providing rich literary, social, and broadly historical context; 12,000+ bibliographical listings; and 2.3 million tags embedded in 8.5 million words of born-digital text. It provides a corpus for investigating everything from writers’ relationships with publishers to their involvement in political activities or their use of imagery. While the version published by Cambridge University Press delivers the content of Orlando in XHTML, the Orlando Visualization software is developed as part of a range of experimental interfaces for the Orlando materials.

The Orlando Visualization software makes use of the [Visualization Toolkit](http://www.vtk.org/), a computer library first created in 1993 by Will Schroeder, Ken Martin and Bill Lorensen, GE corporate R&D employees at the time.  It is an open-source library, meaning that all source code is open to the public to use, improve upon and add to.  VTK tends to focus on 3D rendering, particularly in the fields of medical imaging, engineering and physics, but more recently an informatics sub-library has been added to it specifically aimed at visualizing information in the form of mathematical graphs.

OVis uses this aspect of VTK in order to translate the myriad of relationships between authors and their associations in the Orlando project into an interactive, visual picture. Specifically, authors and other associated people are represented by nodes (dots, circles or symbols). and relationships between two people are represented by edges (lines connecting two nodes).  The VTK toolkit is used to strategically place the nodes on a graph such that the edges provide some insight into the overall inter-connectivity of a group of authors and/or associations.

The relationship between OVis and the data contained within the Orlando project is therefore an interactive visualization of marked-up or tagged text.  OVis provides a way to visually display the huge amount of information contained within the Orlando database into a single picture.  Since no one picture will (helpfully) describe the full information contained within that database, the tool has been made interactive in order to investigate specific relationships, broad or narrow, within the data.  Interactivity includes restricting the visible authors and relationships, highlighting particular authors and relationships, arranging the layout of the nodes/edges representing authors and relationships in multiple ways and zooming, padding, coloring the graph in a number of different ways.
