import processing.serial.*;

Serial myport;
PrintWriter output;

void setup()
{
  
  //println(Serial.list());
  myport = new Serial(this,Serial.list()[0],9600);
  output = createWriter("y.txt");
}

void draw()
{
  while(myport.available()>0)
  {
    String data = myport.readStringUntil('\n');
    if(!(data==null))
      output.println(data);
      
  }
}

void keyPressed() {
  output.flush(); // Writes the remaining data to the file
  output.close(); // Finishes the file
  exit(); // Stops the program
}
