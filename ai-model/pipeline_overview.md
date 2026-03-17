# AI Pipeline Overview

1. User activates Safety Mode  
2. App collects location and behavior data  
3. Data is sent to backend  
4. Python risk model evaluates data  
5. Risk score is calculated  
6. System decides:

- safe → do nothing  
- medium risk → prompt user  
- high risk → trigger alert  

7. Alert sent to Safety Circle
