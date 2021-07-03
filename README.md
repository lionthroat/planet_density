# Planet Density Calculator
A basic calculator in Python using a Kivy interface that takes a user input, and finding the best fit to known densities of planets in our Solar System.  

### Case 1: Exact Match
<img src="https://github.com/wrongenvelope/planet_density/blob/python-proj/screen_1.png?raw=true" width="300">
- When the user's input float matched the density of a planet, they'd be informed of the match, and relevant information displays.  
- The user may input new density values as many times as they like before using "q" to quit.

### Case 2: Closest Match
<img src="https://github.com/wrongenvelope/planet_density/blob/python-proj/screen_2.png?raw=true" width="300">
- When the user's input float did not match any known values, the algorithm searches for the next closest match. Note that no real error handling on data was implemented, so
it's up to the user to follow the guidance on recommended range. For example, if a user inputs 1.26, their closest match should be Uranus (1.27 g/cm^3). Critically, the user
can find out whether a given density likely results in a Gas Giant or Rocky planet.

##### Why did this interest me?
<blockquote>The density of a planetary body provides insight into its chemical composition. For example, Earth is not only the densest planet, but is denser than the sun! This is because
Earth is composed of heavier metal elements. While the Earth has fewer heavy elements than Mercury (by g/cm^3), the gravitational pressure on our magnetically active molten core
compresses the Earth enough to overtake Mercury in density.</blockquote>

##### What did I hope to learn?
<blockquote>I used this exercise to learn Kivy's GUI library, as it represents a more modern alternative to tkinter and others.
Kivy is open source and runs on Mac, Windows, Linux, and Raspberry Pi. It seems to be a decent "middleware" for a lightweight GUI without a whole production in Unity.
There was also audio and video support that I did not test. I also wanted to work with basic functions to find "best fit" answers when a user's exact input is not found.
</blockquote>

##### How could this be improved?
<blockquote>I'd like to add more planetary bodies for comparison, such as the Sun, asteroids, and even other stars. Having graphical representations, and showing the user's
input on a number line from "Least Dense" to "Most Dense" would also be interesting. Obviously the use cases for having a density and needing to find a planet are somewhat limited,
but the idea of building out a celestial almanac would be a lot of fun. I would port the project to Unity or React if I wanted to build a more interactive experience.
</blockquote>

- Heather
7/3/21
