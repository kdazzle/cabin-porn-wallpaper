**cabin-porn-wallpaper** is a python script for Windows 7 that changes your wallpaper to a random [cabin porn](http://cabinporn.com/) comic.

Credits
=======
Forked from the [xkcd-wallpaper](https://github.com/abody/xkcd-wallpaper) project
Wallpaper code is by [ AKM](http://gabbpuy.blogspot.gr/2007/02/set-windows-wallpaper-from-python.html).

Installing
==========
cabin-porn-wallpaper is a script for Windows only tested under Windows 7.

 * Install the required packages (in requirements.txt)
 * [pywin32](http://sourceforge.net/projects/pywin32/) might have to be install manually
 * Open the Windows Task Scheduler. In the Start menu type "Task Scheduler"
 * Create a new task with the following settings:
   * Run only **when user is logged in**
   * Triggers: 
        ** Begin Task: At log on 
        ** Repeat Task every 15 minutes (or whatever)
        ** For a duration of Indefinitely
        ** Enabled
   * Actions: **Start program**
   * Program/script: Your virtual environment's path to python.exe or "C:\python27\python.exe" ** include quotation marks **
   * Arguments: Full path to your location of the script file; ** include quotation marks **
   * Start in: Full path to your location of the script directory ** without quotes **
   * Stop the task if it runs longer than **1 hour**

You can test that it works by selecting the task, right clicking and picking **"Run"**. Alternatively, you can import Wallpaper.xml from the repository into the Windows Task Scheduler and modify the settings accordingly.

License
=======
xkcd-wall is licensed under the MIT license. See the file LICENSE for more information.
