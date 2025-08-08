Converted Document

Converted from: Linux/0\. Set up of LAN Segments\.md

Note: This is a basic conversion\. For full formatting, use specialized tools\.

1\. Set up of LAN Segments

Introduction

\_\_Objective\_\_

At the end of this guide, you will learn how to configure network interfaces\\\.

\_\_Login\_\_

The login credential for all server and client machines:

Username: root / user

Password: Skill39@Lyon

\_\_Network Topology\_\_

| Content |

|\-\-\-\-\-\-\-\-\-|

| This will be the network topology that will be referenced for setting up the infrastructure\\\. |

| \!\[Image 1\]\(0\. Set up of LAN Segments\_images/0\. Set up of LAN Segments\_image\_01\.png\) |

Create 3 LAN Segments:

1\. INT

2\. DMZ

3\. WAN

VMs

LAN Segments

fw\\\.worldskills\\\.org

WAN

INT

DMZ

int\\\-srv01\\\.int\\\.worldskills\\\.org

INT

mail\\\.dmz\\\.worldskills\\\.org

DMZ

ha\\\-prx01\\\.dmz\\\.worldskills\\\.org

DMZ

ha\\\-prx02\\\.dmz\\\.worldskills\\\.org

DMZ

web01\\\.dmz\\\.worldskills\\\.org

DMZ

web02\\\.dmz\\\.worldskills\\\.org

DMZ

jamie\\\-ws01\\\.ext\\\.worldskills\\\.org

WAN

vim /etc/network/interfaces

| Content |

|\-\-\-\-\-\-\-\-\-|

| fw\\\.worldskills\\\.org |

| \!\[Image 2\]\(0\. Set up of LAN Segments\_images/0\. Set up of LAN Segments\_image\_02\.png\) |

| Content |

|\-\-\-\-\-\-\-\-\-|

| int\\\-srv01\\\.int\\\.worldskills\\\.org |

| \!\[Image 3\]\(0\. Set up of LAN Segments\_images/0\. Set up of LAN Segments\_image\_03\.png\) |

| Content |

|\-\-\-\-\-\-\-\-\-|

| ha\\\-prx01\\\.dmz\\\.worldskills\\\.org |

| \!\[Image 4\]\(0\. Set up of LAN Segments\_images/0\. Set up of LAN Segments\_image\_04\.png\) |

| Content |

|\-\-\-\-\-\-\-\-\-|

| ha\\\-prx02\\\.dmz\\\.worldskills\\\.org |

| \!\[Image 5\]\(0\. Set up of LAN Segments\_images/0\. Set up of LAN Segments\_image\_05\.png\) |

| Content |

|\-\-\-\-\-\-\-\-\-|

| mail\\\.dmz\\\.worldskills\\\.org |

| \!\[Image 6\]\(0\. Set up of LAN Segments\_images/0\. Set up of LAN Segments\_image\_06\.png\) |

| Content |

|\-\-\-\-\-\-\-\-\-|

| web01\\\.dmz\\\.worldskills\\\.org |

| \!\[Image 7\]\(0\. Set up of LAN Segments\_images/0\. Set up of LAN Segments\_image\_07\.png\) |

| Content |

|\-\-\-\-\-\-\-\-\-|

| web02\\\.dmz\\\.worldskills\\\.org |

| \!\[Image 8\]\(0\. Set up of LAN Segments\_images/0\. Set up of LAN Segments\_image\_08\.png\) |

| Content |

|\-\-\-\-\-\-\-\-\-|

| jamie\\\-ws01\\\.ext\\\.worldskills\\\.org |

| \!\[Image 9\]\(0\. Set up of LAN Segments\_images/0\. Set up of LAN Segments\_image\_09\.png\) |

