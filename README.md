# Test-BL-Auth
This is a Django app I made quickly to test authQuery.php. It's pretty simple. Once you've got the app running, there's a text box on the index page. Put your Blockland username in that, then hit "send data," which will send that and your IP in a POST request to authQuery.php, which will then return a positive or negative depending on whether or not you put in a username that corresponds to your IP on the Blockland master server.

It's meant to be online, so it would typically use the IP of the machine that connected to it, but if you're running it in the dev server locally, it'll send an invalid value for the IP (at least it does for me. specifically, it uses "::1"), which the auth tool will ignore, and instead choose to use the IP of the machine that sent the request, which would, in this case, be your actual IP. So it should be fine.

As far as the license is concerned, I guess it's just in the public domain. Why not.
