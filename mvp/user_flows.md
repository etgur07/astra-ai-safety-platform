# Astra User Flows

## Flow 1 – Panic Alert

1. User opens the Astra app
2. User presses the Panic Alert button
3. The system captures the user's current location
4. An alert is sent to trusted Safety Circle contacts
5. Contacts receive location and emergency notification

---

## Flow 2 – Safety Check-In

1. User activates Safety Mode
2. The system starts a timer
3. After the timer expires, Astra asks:
   "Are you safe?"
4. If the user confirms safety → session ends
5. If there is no response → alert is triggered

---

## Flow 3 – Location Sharing

1. User selects "Share Location"
2. User chooses Safety Circle contacts
3. Location updates are shared temporarily
4. User ends sharing when activity is complete

---

## Flow 4 – AI Risk Detection

1. User activates Safety Mode  
2. Astra continuously collects location and behavior data  
3. The AI system analyzes movement patterns and check-in status  
4. If abnormal behavior is detected:
   - risk score increases  
5. If risk reaches threshold:
   - Astra prompts user: "Are you safe?"  
6. If no response:
   - panic alert is automatically triggered  
7. Safety Circle contacts are notified  

This flow enables proactive safety detection without requiring manual user input.
