# catwiipi
<p>
After a bit of playing with Scratch and a Wiimote I've comes up with a simple way to use the two together. The Wiimote is a bluetooth device which can be connected
to a regular computer. The nice thing about it is that many people have already written drivers for it so we don't need to go to too much effort to get it to work.
</p>

Here's how to set it up on a Raspberry Pi, first you should make sure you're running a current version of the distribution. The following commands wil update your
system to the current version. This might take a while to run depending on how out of date your installation is.

<p class="solid">
sudo apt-get update<br>
sudo apt-get upgrade
</p>

Next you should install the bluetooth drivers for Linux.

<p class="solid">
sudo apt-get install bluetooth
</p>

I had trouble with getting my bluetooth device recognised. Initially I was using a Belkin USB bluetooth dongle but it wasn't recognised properly so I switched to a 
Cambridge Silicon Radio Ltd dongle which is working fine.

Now install the python module for communicating with the Wiimote.

<p class="solid">
sudo apt-get install python-cwiid
</p>

Download and install the wiicontroller which will allow you to use the Wiimote with Scratch as well as the Scratch support library.

<p class="solid">
wget https://raw.github.com/pilliq/scratchpy/master/scratch.py
</p>

Open the SimpleLander game in Scratch. It should tell you that remote sensor connections have been enabled.

Run the wiicontroller.py as

<p class="solid">
sudo python wiicontroller.py
</p>

Follow the instructions on screen.

When playing the game the arrow keys on the keyboard will turn left, right, up fires the rocket and space releases the rover. When using a Wiimote the B button 
fires the rockets, left and right turn left and right and the down button releases the rover.
</div>
