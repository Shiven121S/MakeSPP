# Introduction to Arduino

**In this scenario, you can see a red, blue, and black wire.**

**The red wire in this case is connected to the 5V hole on the Arduino, the blue wire connects the black and red wires, and the black wire is connected to ground. This creates a complete circuit.**

**Important: The red wire powers the blue wire because power flows vertically, though it is stopped by the gap in the middle. Likewise, the blue wire powers the black wire back to ground, creating a complete circuit.**

**Resistors: These tiny components function by lessening the voltage that comes from the battery/arduino, and are fundamental in not frying components.**

<img title="a title" alt="Alt text" src="https://lh7-us.googleusercontent.com/2m8IOjt3S4I3AeoKDGOvBy22_Rny2WSM_TuyPg8ov8TuZ7axz9GHP29NgoN0jViy8mOJ8zieOdBHQaiXh0vehTeNNUHE8JQx5fG-V65O0PjsmgV1ebxMgdRfuOb4_FhkGUomeIYuaaknqtuSAKi_lF0">

**Above is a resistor.**

**LED Lights: Many beginner projects use LED lights to determine whether a circuit is complete, as if it is not, it will not function at all.**

<img title="a title" alt="Alt text" src="https://lh7-us.googleusercontent.com/4ZS_cexnHzedGcMeomoWVo5hd5qmtdwEscb773eIlifHmnUGklgwjK78-ehseLhCGHGwbWEWWG-yKsTim0Itk9o6Rp9dZNBBV0gWXuef3mZF_IO--OlFKPBZqFkpvUCOiTabid-qsuO-_EMou0bMtr8">

**LEDs have two pins, with one visibly longer than the other. The wire or component that directly powers the LED should be touching the cathode (the longer pin) while the power that exits the LED should be the anode (the shorter pin). LEDs are usually used with resistors to avoid burning them out and rendering them dysfunctional.**

**Now let us talk about the software you will be using. Please download the Arduino IDE. When you open up a file (sketch) in the IDE, you will see something like this:**

<img title="a title" alt="Alt text" src="https://lh7-us.googleusercontent.com/CWjX9wwU5RNILttD7OXdDUNF6pOLom-XmGFIY23-qiduirP2MEs0-ITjRvqkagrT6nH9D0e1eqF4KfFOkbvjqNdqoFPz42Uf9TVNLsLB1CKQHcLKjVCMmb6HTWWkGXk9gf6kwRAkKKqLNQLqj5fp1xk">


**As you can see, there are two distinct parts, the setup and the loop.**

**The setup is typically used to set the mode of pins while the loop is used to infinitely run code.**

**Pins can serve two functions, input and output. Output pins give power to components while input pins receive data from sensors.**

**This is how to set a pin as either input or output, case sensitive:**

<img title="a title" alt="Alt text" src="https://lh7-us.googleusercontent.com/zmflpO5HP4-DYyfGU3sKwpcf7ZmMKcirav_t0vMOAR47RTQ2UzDoJ5nHSQH-otiNdFpr3otj1RPlRRUv3KcYaR2f5Orc5Xo4B2KJPlG08_DOn8LocB9ILKiKftAfWiBFUaT-BgQ0YNs211oyDX4TgWQ">


**For an input pin, replace OUTPUT on line 6 with INPUT**

**Next, to turn a pin on, you can do this**

<img title="a title" alt="Alt text" src="https://lh7-us.googleusercontent.com/X0J0pCgPXxe-0HcDeUXbSrdO59uhorMW_J9PnTB9NB_gQiWRUdsWx9g2hlNklwihNqgHSHbzx0rF1J8zdqSyGT6x4g2DRJOTAklQU5TZ2u2SbiPQWwjofEZUnryR6IZA12BgP62Kz8rPLtnx5or-fIU">

**Alternatively, you can turn power off by replacing HIGH with LOW.**

**For the first challenge, you will also need to know this:**

<img title="a title" alt="Alt text" src="https://lh7-us.googleusercontent.com/xsBlLjpzG-LY4BUwOGGmAWZ0vxHPCBOLNMDDBqJgH2hlsmqAOEO6gsyk_oEM62YrG6Dxg8E_umhgi4f-J3TdV0c_tCTzQPOZzmkb2HGIfY3OQ2fLp9YPetU7xLjkjkyQQehnd-Mn5R4JPslh0c9byEM">

**This line of code will delay for 1000 milliseconds (1 second), which you will need momentarily**

**Your arduino should come with a blue cable which connects to the arduino and a usb port. When you plug it in, go to Tools and make sure you are using the correct board and the arduino is connected to the right port. If it is not, then you can remedy this by changing either the selected port in the IDE or manually switching the USB port.**

<img title="a title" alt="Alt text" src="https://lh7-us.googleusercontent.com/4WH1Wq3z0ZutDm-ZSBGzMtP-5oPkZNZIhd1PM7x6dHbbkWbFwXIEft9wjc_SoLJG07DWK0k-Ruqt_LBMotzb5mmtJdFlQPhD-lnwSen6gg3dhHD_cStCV4uY9jPfgDSHV0cyUr-wgm-7R69hKvTeR4k">

**A complete circuit may look like this**
