# IoT Wifi controlled car tutorial
__Author__: Emil Karlsson, ek224hy

## Project overview
This is project I developed when taking the [Applied IoT course at Linnéuniversitet](https://lnu.se/en/course/introduction-to-applied-internet-of-things/distance-international-summer/). The project goal is to create a car/robot that can be controlled via a simple webapp when both devices are connected to the same Wifi. The car have 2 motors (its possible to add more motors, you would have to create more motor objects in main.py and have a motor driver card capable of handling more motors) that is controlled via a webserver running [WebSocket protocol](https://en.wikipedia.org/wiki/WebSocket#:~:text=WebSocket%20is%20a%20computer%20communications,as%20RFC%206455%20in%202011) on the Pico board. The server is connected to a client that controls the car. The car can also make use various optional sensors.

__Time effort:__ 4-12 hours, highly depending on your current knowledge. 
__Difficulty:__ Medium for beginners, Easy for experienced

## Objective

My main reason for choosing this project is that it seemed like a fun challenge. I am a web development student at BTH and I have decent understanding of networking, protocols and general coding. So I wanted to create a project that challenged me on both a coding and hardware level. I also hope it will inspire my daughter (or anyone interested) to see that building somewhat advanced projects on your own is achievable and not as difficult as it might initially appear. Additionally, I want to provide project idea that is available for anyone to help them open their minds to the challenge of learning about IoT. 
While the project doesn't necessarily focus heavily on data collection at its current stage. The possibilites of extending its data collecting ability are endless. For example, one could create a racing track and a goalpost, that senses a passing car, and store the the track time in a highscore list or database. This project supports my own personal progress goals (of learning as much as possible both during and after this course) as I easily can expand upon this project as mentioned.
When examinating for this course the car will most likely be equiped with a one or two simple sensors, like a collision sensor or similar with the purpose of being able to visualize some basic data, like collisions and maybe track how many times the car flipped (with a tilt switch or similar).

##Material
Explain all material that is needed. All sensors, where you bought them and their specifications. Please also provide pictures of what you have bought and what you are using.

| Month    | Component |  Description |Price |
| -------- | ------- | --------| ---- |
| <img src="https://www.electrokit.com/cache/c4/700x700-product_41019_41019110_41019110.jpg" alt="Image" width="300"/> | [Raspberry Pi Pico W](https://www.electrokit.com/raspberry-pi-pico-w)   | MCU for this project. If you dont want to solder, get the [Pico WH](https://www.electrokit.com/raspberry-pi-pico-wh?gad_source=1&gclid=CjwKCAjw-O6zBhASEiwAOHeGxWUtcyZh5lel_tFE7TW0D3Foy-07vQYDlVK4v4n0q_PkLi4qekNAHBoCxjwQAvD_BwE) and use it with the breadboard listed below under "optional" | 89 SEK |
| <img src="https://www.electrokit.com/upload/product/41016/41016218/41016218.jpg" alt="Image" width="300"/> | [Motordriver L298 double H-Bridge 5-35V 2A](https://www.electrokit.com/motordrivare-l298-dubbel-h-brygga-5-35v-2a)| Controls the motor direction and speed. Can operate two different motors at the same time, independent of each other.| 79 SEK |
| <img src="https://www.electrokit.com/cache/7b/700x700-product_41013_41013133_41013133-6.jpg" alt="Image" width="300"/> | [Olimex Robot platform](https://www.electrokit.com/olimex-robotplattform-3-hjul) | Main car platform. Was one of the cheapest kits i could find. But another kit can be used as long as the specs allow it. |279 SEK |
| <img src="https://www.electrokit.com/cache/24/700x700-product_41012_41012684_41012684.jpg" alt="Image" width="300"/> | [Lab cable 40-pin 30cm male/male](https://www.electrokit.com/labbsladd-20-pin-15cm-hona/hane) |For experimenting and testing. Also perfect if you dont want to solder. You only need a few, like 5-10 |49 SEK |
| <img src="https://www.electrokit.com/upload/product/41012/41012911/41012911.jpg" alt="Image" width="300"/> | [Lab cable 40-pin 15cm male/female](https://www.electrokit.com/labbsladd-20-pin-15cm-hona/hane) |For experimenting and testing. Also perfect if you dont want to solder. You only need a few, like 5-10 |29 SEK |
| <img src="https://www.electrokit.com/upload/product/10160/10160840/10160840.jpg" alt="Image" width="300"/> | [Breadboard](https://www.electrokit.com/kopplingsdack-840-anslutningar) |For experimenting and testing. Also perfect if you dont want to solder.|69 SEK |
| __Below__ | __is__ | __optional__ | - |


List of material
What the different things (sensors, wires, controllers) do - short specifications
Where you bought them and how much they cost
Example:

IoT Thing	For this
Perhaps	a table
is a	jolly good idea?
In this project I have chosen to work with the Pycom LoPy4 device as seen in Fig. 1, it's a neat little device programmed by MicroPython and has several bands of connectivity. The device has many digital and analog input and outputs and is well suited for an IoT project.

Image Not Showing
Possible Reasons
The image file may be corrupted
The server hosting the image is unavailable
The image path is incorrect
The image format is not supported
Learn More →
Fig. 1. LoPy4 with headers. Pycom.io

Computer setup
How is the device programmed. Which IDE are you using. Describe all steps from flashing the firmware, installing plugins in your favorite editor. How flashing is done on MicroPython. The aim is that a beginner should be able to understand.

Chosen IDE
How the code is uploaded
Steps that you needed to do for your computer. Installation of Node.js, extra drivers, etc.
Putting everything together
How is all the electronics connected? Describe all the wiring, good if you can show a circuit diagram. Be specific on how to connect everything, and what to think of in terms of resistors, current and voltage. Is this only for a development setup or could it be used in production?

Circuit diagram (can be hand drawn)
*Electrical calculations
Platform
Describe your choice of platform. If you have tried different platforms it can be good to provide a comparison.

Is your platform based on a local installation or a cloud? Do you plan to use a paid subscription or a free? Describe the different alternatives on going forward if you want to scale your idea.

## Setup
__Remember to use / or \ for paths, depending on your OS.__
### Connect to Wifi 
1. Create server\src\keys.py
1. Add the variables: 
    * WIFI_SSID = <'WIFI NAME'> 
    * WIFI_PASS = <'WIFI PASSWORD'>

### Setup client connection FORTSÄTT HÄR!!
##### Get your Pico servers address: 
1. Open client/functions.js and set the variables:
    * CONNECT_TO_IP = <"Your Pico server IP">
    * CONNECT_TO_PORT = <"Prefered port (the preset one used is 3000)">



Describe platform in terms of functionality
*Explain and elaborate what made you choose this platform
The code
Import core functions of your code here, and don't forget to explain what you have done! Do not put too much code here, focus on the core functionalities. Have you done a specific function that does a calculation, or are you using clever function for sending data on two networks? Or, are you checking if the value is reasonable etc. Explain what you have done, including the setup of the network, wireless, libraries and all that is needed to understand.








import this as that

def my_cool_function():
    print('not much here')

s.send(package)

# Explain your code!
Transmitting the data / connectivity
How is the data transmitted to the internet or local server? Describe the package format. All the different steps that are needed in getting the data to your end-point. Explain both the code and choice of wireless protocols.

How often is the data sent?
Which wireless protocols did you use (WiFi, LoRa, etc …)?
Which transport protocols were used (MQTT, webhook, etc …)
*Elaborate on the design choices regarding data transmission and wireless protocols. That is how your choices affect the device range and battery consumption.
Presenting the data
Describe the presentation part. How is the dashboard built? How long is the data preserved in the database?

Provide visual examples on how the dashboard looks. Pictures needed.
How often is data saved in the database.
*Explain your choice of database.
*Automation/triggers of the data.
Finalizing the design
Show the final results of your project. Give your final thoughts on how you think the project went. What could have been done in an other way, or even better? Pictures are nice!

Show final results of the project
Pictures
*Video presentation
